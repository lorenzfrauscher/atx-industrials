#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract.py -- LLM-gestuetzte Extraktion aus Geschaeftsberichten
Projekt: Strategische Prioritaeten oesterreichischer Industrieunternehmen (ATX)

Grundprinzip
------------
Das Sprachmodell liefert AUSSCHLIESSLICH woertliche Zitate. Es gibt keine
Seitenzahlen an. Die Seite wird anschliessend deterministisch bestimmt, indem
das Zitat im normalisierten Berichtstext gesucht wird. Ein Zitat, das dort
nicht vorkommt, ist erfunden und wird als solches markiert.

Damit sind Seitenangaben nicht halluzinierbar, und erfundene Zitate werden
fuer 100 Prozent der Extraktionen erkannt statt nur in der Stichprobe.

Aufrufe
-------
  python3 extract.py --list-models
  python3 extract.py --company palfinger --dry-run
  python3 extract.py --company palfinger
  python3 extract.py --all

Der API-Schluessel wird aus der Umgebungsvariable GEMINI_API_KEY gelesen.
Er steht nirgends im Code.
"""

import warnings

# Zwei bekannte, folgenlose Warnungen der Abhaengigkeiten unterdruecken, damit die
# Ausgabe lesbar bleibt:
#   1. google-auth warnt, dass Python 3.9 das Supportende erreicht hat.
#   2. urllib3 warnt, dass macOS LibreSSL statt OpenSSL verwendet.
# Beide sind in der README als Umgebungsbedingung dokumentiert.
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", message=".*LibreSSL.*")

# pypdf meldet bei den PALFINGER-Schriften fehlendes fontTools. Getestet: fontTools
# aendert die Extraktion nicht, die Kodierung bleibt identisch fehlerhaft. Die
# Reparatur in _text_reparieren bleibt daher zustaendig, die Meldung ist Rauschen.
import logging
logging.getLogger("pypdf").setLevel(logging.ERROR)

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import time
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
PDF_DIR = os.path.dirname(HERE)          # Berichte liegen eine Ebene ueber pipeline/
CACHE_DIR = os.path.join(HERE, "cache")
DATA_DIR = os.path.join(HERE, "data")

# Bewusst eine feste Version statt eines "latest"-Alias. Ein Alias zeigt zu einem
# spaeteren Zeitpunkt auf ein anderes Modell, damit waere der Lauf nicht mehr
# reproduzierbar. Genau das ist der Anspruch dieses Projekts.
DEFAULT_MODEL = "gemini-3.8-flash"

# Reihenfolge fuer --probe. Neue Modelle sind haeufig ueberlastet (HTTP 503),
# aeltere laufen stabiler. Gewaehlt wird eines, und zwar fuer alle sieben
# Unternehmen dasselbe, sonst ist der Lauf nicht vergleichbar.
MODELL_KANDIDATEN = [
    "gemini-3.8-flash",
    "gemini-3.7-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-3-flash-preview",
    "gemini-2.5-flash",
]

# ---------------------------------------------------------------------------
# 1. Universum
# ---------------------------------------------------------------------------
# Abgeleitet nach der Auswahlregel in ATX_Schritt1_Universum_und_Methodik.md
REPORTS = {
    "voestalpine":  {"datei": "voestalpine_2025_26.pdf", "name": "voestalpine AG", "jahr": "2025/26", "gruppe": "Hersteller"},
    "lenzing":      {"datei": "lenzing_2025.pdf",        "name": "Lenzing AG",     "jahr": "2025",    "gruppe": "Hersteller"},
    "andritz":      {"datei": "andritz_2025.pdf",        "name": "Andritz AG",     "jahr": "2025",    "gruppe": "Hersteller"},
    "palfinger":    {"datei": "palfinger_2025.pdf",      "name": "PALFINGER AG",   "jahr": "2025",    "gruppe": "Hersteller"},
    "wienerberger": {"datei": "wienerberger_2025.pdf",   "name": "Wienerberger AG","jahr": "2025",    "gruppe": "Bau"},
    "strabag":      {"datei": "strabag_2025.pdf",        "name": "Strabag SE",     "jahr": "2025",    "gruppe": "Bau"},
    "porr":         {"datei": "porr_2025.pdf",           "name": "Porr AG",        "jahr": "2025",    "gruppe": "Bau"},
}

# ---------------------------------------------------------------------------
# 2. Feste Kategorienlisten. Das Modell darf nicht frei erfinden.
# ---------------------------------------------------------------------------
RISIKO_KATEGORIEN = ["Markt", "Lieferkette", "Regulierung", "Finanzierung", "Technologie"]

REGIONEN = [
    "Oesterreich", "DACH", "Europa uebrig", "Nordamerika", "Lateinamerika",
    "China", "Indien", "Asien-Pazifik uebrig", "Naher Osten", "Afrika", "Global",
]

# Schlagworte fuer die Kapitelauswahl. Bewusst breit, die Praezision macht das Modell.
KEYWORDS = {
    "strategie": ["strategie", "strategisch", "prioritaet", "priorität", "zielbild",
                  "transformation", "roadmap", "fokus", "ausrichtung", "programm"],
    "wachstum":  ["wachstum", "wachsen", "markt", "maerkte", "märkte", "nachfrage",
                  "expansion", "region", "absatz", "nordamerika", "asien", "china",
                  "indien", "europa", "usa"],
    "risiko":    ["risiko", "risiken", "risikomanagement", "unsicherheit",
                  "volatil", "gefaehrd", "gefährd", "chancen- und risiko"],
    "capex":     ["investition", "investiert", "capex", "akquisition", "uebernahme",
                  "übernahme", "zukauf", "beteiligung", "desinvest", "m&a",
                  "sachanlagen"],
}

TOP_SEITEN_JE_FELD = 14      # wie viele Seiten je Feldtyp ausgewaehlt werden
CHUNK_ZEICHEN = 45000        # rund 13.000 Tokens. Bewusst klein: bei 90.000 Zeichen
                             # lieferte die API reproduzierbar 503 fuer einzelne
                             # Chunks, kleinere Anfragen laufen stabil durch.
MAX_ZIFFERNANTEIL = 0.30     # Seiten oberhalb sind reine Zahlentabellen

# ---------------------------------------------------------------------------
# 3. PDF einlesen
# ---------------------------------------------------------------------------

# In der Symbolschrift des PALFINGER-Berichts liegen diese Zeichen oberhalb von
# U+F07E. Dort gilt der ASCII-Versatz NICHT, die Zuordnung wurde je Zeichen am
# Fliesstext geprueft (Belege in verification.md).
PUA_SONDERZEICHEN = {
    0xF0DE: "fi",   # Rueckläufige, Nettofinanzverschuldung, Asien-Pazifik
    0xF0DF: "fl",   # Cashflow, Konflikt, Inflationsraten. NICHT "ss".
    0xF0A7: "\u2022",  # Aufzaehlungspunkt, nicht das Paragrafenzeichen
    0xF0B7: "\u2022",  # Aufzaehlungspunkt im Lenzing-Bericht, 18 Vorkommen
    0xF0E4: "\u2191",  # Symbol fuer Chancen in der Wesentlichkeitstabelle
    0xF0E6: "\u2193",  # Symbol fuer Risiken in derselben Tabelle
}

_unbekannte_pua = {}


def _text_reparieren(text):
    """Repariert die fehlerhafte Zeichenkodierung des PALFINGER-Berichts.

    Der Bericht liefert 27.717 Zeichen in der Private Use Area. Zwei Bereiche
    mit unterschiedlicher Logik:

    1. U+F020 bis U+F07E entspricht dem ASCII-Bereich mit Versatz 0xF000.
       Betrifft im Bestand ausschliesslich Ziffern, etwa U+F032 fuer "2".
       27.605 Vorkommen.

    2. Oberhalb davon liegt eine Symbolzuordnung, in der der Versatz falsche
       Zeichen erzeugt. Der erste Anlauf dieser Pipeline hat daraus "Cashflow"
       zu "Cashss ow" gemacht und in der Folge ein korrektes Zitat faelschlich
       als erfunden markiert. Diese Zeichen werden ueber PUA_SONDERZEICHEN
       einzeln zugeordnet.

    Unbekannte Zeichen werden entfernt und gezaehlt, damit sie nicht unbemerkt
    als falsche Buchstaben in Zitate wandern.
    """
    if not text:
        return ""
    if not any(0xE000 <= ord(c) <= 0xF8FF for c in text):
        return text
    aus = []
    for c in text:
        o = ord(c)
        if 0xF020 <= o <= 0xF07E:
            aus.append(chr(o - 0xF000))
        elif o in PUA_SONDERZEICHEN:
            aus.append(PUA_SONDERZEICHEN[o])
        elif 0xE000 <= o <= 0xF8FF:
            _unbekannte_pua[o] = _unbekannte_pua.get(o, 0) + 1
        else:
            aus.append(c)
    return "".join(aus)


def pua_bericht():
    """Meldet Zeichen, die keiner Regel zugeordnet werden konnten."""
    if _unbekannte_pua:
        teile = ", ".join("U+%04X (%dx)" % (k, v)
                          for k, v in sorted(_unbekannte_pua.items()))
        print("    HINWEIS: nicht zuordenbare Sonderzeichen entfernt: %s" % teile)


def seiten_laden(pdf_pfad):
    """Gibt eine Liste zurueck. Index 0 entspricht PDF-Seite 1."""
    import pypdf
    reader = pypdf.PdfReader(pdf_pfad)
    return [_text_reparieren(seite.extract_text() or "") for seite in reader.pages]

# ---------------------------------------------------------------------------
# 4. Normalisierung und Zitatsuche
# ---------------------------------------------------------------------------

_WS = re.compile(r"\s+")

def normalisieren(text):
    """Vereinheitlicht Text so, dass ein Zitat aus dem Modell wiedergefunden wird,
    auch wenn Zeilenumbrueche, Trennstriche oder Anfuehrungszeichen abweichen."""
    if not text:
        return ""
    t = unicodedata.normalize("NFKC", text)
    t = t.replace("­", "")                 # weiches Trennzeichen
    t = re.sub(r"-\s*\n\s*", "", t)             # Trennung am Zeilenende aufloesen
    t = t.replace("’", "'").replace("‘", "'")
    t = t.replace("“", '"').replace("”", '"').replace("„", '"')
    t = t.replace("–", "-").replace("—", "-").replace("−", "-")
    t = _WS.sub(" ", t)
    return t.strip().lower()


_NUR_ALNUM = re.compile(r"[^0-9a-zäöüß ]+", re.UNICODE)


def normalisieren_hart(text):
    """Zweite Stufe: entfernt alles ausser Buchstaben, Ziffern und Leerzeichen.

    Begruendung aus dem Vollauf: Ein Grossteil der zunaechst nur teilweise
    gefundenen Zitate war korrekt, scheiterte aber an Formatierung. Drei
    beobachtete Muster:
      1. Trennstriche ohne Zeilenumbruch, "Pro-dukte" statt "Produkte"
      2. Aufzaehlungszeichen im Original, die das Modell als Komma wiedergibt
      3. Semikolon im Original, Punkt in der Modellausgabe
    Keines davon ist eine erfundene Aussage. Ohne diese Stufe wuerden
    Formatierungsartefakte als Belegfehler gezaehlt.
    """
    return _WS.sub(" ", _NUR_ALNUM.sub(" ", normalisieren(text))).strip()


class Korpus(object):
    """Haelt den normalisierten Gesamttext eines Berichts plus Seitenindex."""

    def __init__(self, seiten):
        self.seiten_roh = seiten
        teile = []
        self.offsets = []      # (start, ende, seitennummer_1basiert)
        pos = 0
        for i, s in enumerate(seiten):
            n = normalisieren(s)
            teile.append(n)
            self.offsets.append((pos, pos + len(n), i + 1))
            pos += len(n) + 1
        self.text = " ".join(teile)

        teile_hart = []
        self.offsets_hart = []
        pos = 0
        for i, s in enumerate(seiten):
            h = normalisieren_hart(s)
            teile_hart.append(h)
            self.offsets_hart.append((pos, pos + len(h), i + 1))
            pos += len(h) + 1
        self.text_hart = " ".join(teile_hart)

    def _seite_von_position(self, p, hart=False):
        for start, ende, nr in (self.offsets_hart if hart else self.offsets):
            if start <= p < ende:
                return nr
        return None

    def suche(self, zitat):
        """Liefert (seite, treffertyp, alle_fundstellen).

        treffertyp:
          exakt             genau eine woertliche Fundstelle
          exakt_mehrdeutig  woertlich, aber mehrfach im Bericht (Textbausteine,
                            Kopf- und Fusszeilen). Die Seitenangabe ist dann
                            nicht eindeutig und wird in der Verifikation
                            gesondert behandelt.
          teilweise         nur ein Wortpraefix passt. Typisch fuer Paraphrasen.
          nicht_gefunden    kommt im Bericht nicht vor, also erfunden.
          zu_kurz           unter 15 Zeichen, nicht pruefbar.
        """
        z = normalisieren(zitat)
        if len(z) < 15:
            return None, "zu_kurz", []

        stellen = []
        start = self.text.find(z)
        while start >= 0 and len(stellen) < 10:
            stellen.append(self._seite_von_position(start))
            start = self.text.find(z, start + 1)
        if stellen:
            typ = "exakt" if len(set(stellen)) == 1 else "exakt_mehrdeutig"
            return stellen[0], typ, sorted(set(s for s in stellen if s))

        # Zweite Stufe: ohne Satzzeichen, Trennstriche und Aufzaehlungszeichen
        h = normalisieren_hart(zitat)
        if len(h) >= 15:
            stellen = []
            start = self.text_hart.find(h)
            while start >= 0 and len(stellen) < 10:
                stellen.append(self._seite_von_position(start, hart=True))
                start = self.text_hart.find(h, start + 1)
            if stellen:
                typ = ("exakt_nach_normalisierung" if len(set(stellen)) == 1
                       else "exakt_mehrdeutig")
                return stellen[0], typ, sorted(set(x for x in stellen if x))

        # Fallback: laengsten passenden Wortpraefix suchen, mindestens 8 Woerter
        woerter = h.split(" ") if len(h) >= 15 else z.split(" ")
        quelle = self.text_hart if len(h) >= 15 else self.text
        untere, obere, bester = 8, len(woerter), -1
        if obere < untere:
            return None, "nicht_gefunden", []
        while untere <= obere:
            mitte = (untere + obere) // 2
            pos = quelle.find(" ".join(woerter[:mitte]))
            if pos >= 0:
                bester, untere = pos, mitte + 1
            else:
                obere = mitte - 1
        if bester >= 0:
            seite = self._seite_von_position(bester, hart=(quelle is self.text_hart))
            return seite, "teilweise", [seite] if seite else []
        return None, "nicht_gefunden", []

# ---------------------------------------------------------------------------
# 5. Kapitelauswahl und Chunking
# ---------------------------------------------------------------------------

# Marker der Nachhaltigkeitsberichterstattung nach ESRS und EU-Taxonomie.
# Dient NICHT dazu, Inhalte auszuschliessen, sondern sie zu kennzeichnen. Die
# Extraktion bleibt unveraendert, die Trennung erfolgt erst in der Aggregation.
ESRS_MARKER = [
    "esrs", "csrd", "eu-taxonomie", "taxonomiekonform", "taxonomiefaehig",
    "taxonomiefähig", "doppelte wesentlichkeit", "wesentlichkeitsanalyse",
    "nachhaltigkeitserklaerung", "nachhaltigkeitserklärung", "delegierte verordnung",
    "scope 1", "scope 2", "scope 3", "thg-emissionen", "treibhausgasemissionen",
    "nichtfinanzielle erklaerung", "nichtfinanzielle erklärung",
]
ESRS_SCHWELLE = 2   # verschiedene Marker je Seite, damit eine Seite als Anker gilt
ESRS_LUECKE = 10    # Luecken bis zu dieser Laenge zwischen Ankern fuellen


def abschnitte_klassifizieren(seiten):
    """Ordnet jede PDF-Seite deterministisch einem Abschnitt zu.

    Rueckgabe: Liste, Index 0 entspricht PDF-Seite 1, Werte
    "Geschaeftsbericht" oder "Nachhaltigkeitsberichterstattung".

    Zwei Schritte:
      1. Eine Seite mit mindestens ESRS_SCHWELLE Markern gilt als markiert.
      2. Luecken von hoechstens ESRS_LUECKE Seiten zwischen markierten Seiten
         werden gefuellt. Nachhaltigkeitsabschnitte sind zusammenhaengend, aber
         nicht jede Seite darin nennt einen Marker. Ohne Schritt 2 zerfaellt ein
         Block in Fragmente und einzelne Seiten werden falsch zugeordnet.

    Kalibrierung: Getestet wurden Schwellen 2 und 3 gegen Lueckenlaengen von 0 bis
    15, geprueft an 21 von Hand zugeordneten PALFINGER-Seiten (14 Geschaeftsteil,
    7 Nachhaltigkeitsteil). Gewaehlt wurde Schwelle 2 mit Luecke 10:
    14 von 14 Geschaeftsseiten korrekt, 6 von 7 Nachhaltigkeitsseiten korrekt.

    Die Fehlerrichtung ist bewusst gewaehlt. Der Klassifikator ordnet im Zweifel
    dem Geschaeftsbericht zu, nie umgekehrt. Der ausgewiesene Anteil der
    Nachhaltigkeitsberichterstattung ist damit eine Untergrenze. Ein zu hoch
    ausgewiesener Anteil waere die gefaehrlichere Fehlerrichtung, weil er
    Geschaeftsaussagen unsichtbar machen wuerde.

    Ergebnis ueber alle sieben Berichte: 25 bis 34 Prozent der Seiten, beim
    Andritz-Finanzbericht erwartungsgemaess 0 Prozent.

    Regelbasiert und ohne Modellaufruf, damit die Zuordnung reproduzierbar ist
    und nicht selbst zur Fehlerquelle wird.
    """
    markiert = []
    for s in seiten:
        n = normalisieren(s)
        markiert.append(sum(1 for m in ESRS_MARKER if m in n) >= ESRS_SCHWELLE)

    gefuellt = list(markiert)
    letzte = None
    for i, m in enumerate(markiert):
        if m:
            if letzte is not None and 0 < i - letzte - 1 <= ESRS_LUECKE:
                for j in range(letzte + 1, i):
                    gefuellt[j] = True
            letzte = i

    return ["Nachhaltigkeitsberichterstattung" if m else "Geschaeftsbericht"
            for m in gefuellt]


def _ziffernanteil(text):
    if not text:
        return 1.0
    ziffern = sum(1 for c in text if c.isdigit())
    return float(ziffern) / max(1, len(text))


def seiten_auswaehlen(seiten):
    """Punktet jede Seite je Feldtyp und waehlt die dichtesten aus.
    Deterministisch, nachvollziehbar, ohne Modellaufruf."""
    kandidaten = set()
    normiert = [normalisieren(s) for s in seiten]

    for feld, worte in KEYWORDS.items():
        punkte = []
        for i, n in enumerate(normiert):
            if len(n) < 400:                       # Trenn- und Bildseiten
                continue
            if _ziffernanteil(n) > MAX_ZIFFERNANTEIL:   # reine Zahlentabellen
                continue
            treffer = sum(n.count(w) for w in worte)
            if treffer:
                punkte.append((treffer * 1000.0 / len(n), treffer, i))
        punkte.sort(reverse=True)
        for _, _, i in punkte[:TOP_SEITEN_JE_FELD]:
            kandidaten.add(i)

    # Nachbarseiten mitnehmen, damit Saetze nicht mitten im Kontext abreissen
    erweitert = set()
    for i in kandidaten:
        for j in (i - 1, i, i + 1):
            if 0 <= j < len(seiten):
                erweitert.add(j)
    return sorted(erweitert)


def chunks_bauen(seiten, indizes):
    """Fasst ausgewaehlte Seiten zu Bloecken zusammen. Eine Seite wird nie geteilt."""
    chunks, aktuell, laenge = [], [], 0
    for i in indizes:
        text = seiten[i]
        kopf = "\n\n[PDF-Seite %d]\n" % (i + 1)
        stueck = kopf + text
        if laenge + len(stueck) > CHUNK_ZEICHEN and aktuell:
            chunks.append("".join(aktuell))
            aktuell, laenge = [], 0
        aktuell.append(stueck)
        laenge += len(stueck)
    if aktuell:
        chunks.append("".join(aktuell))
    return chunks

# ---------------------------------------------------------------------------
# 6. Prompt und Antwortschema
# ---------------------------------------------------------------------------

PROMPT = u"""Du wertest einen Auszug aus dem Geschaeftsbericht eines oesterreichischen
Industrieunternehmens aus. Unternehmen: {unternehmen}, Berichtsjahr: {jahr}.

Extrahiere ausschliesslich, was im vorliegenden Text tatsaechlich steht. Erfinde nichts.
Wenn eine Kategorie im Auszug nicht vorkommt, gib eine leere Liste zurueck.

Jedes Element braucht ein Feld "zitat". Das Zitat muss WOERTLICH aus dem Text unten stammen,
zusammenhaengend, 10 bis 40 Woerter lang. Paraphrasiere nicht. Kuerze nicht mit Auslassungen.
Gib keine Seitenzahlen an, die werden separat bestimmt.

Vier Kategorien:

1. strategische_prioritaeten
   Vom Unternehmen selbst benannte strategische Schwerpunkte fuer die kommenden Jahre.
   Keine Rueckblicke auf Erreichtes.

2. wachstumsmaerkte
   Regionen oder Maerkte, in denen das Unternehmen Wachstum sucht oder erwartet.
   Feld "region" MUSS genau einer dieser Werte sein: {regionen}

3. hauptrisiken
   Vom Unternehmen genannte wesentliche Risiken.
   Feld "kategorie" MUSS genau einer dieser Werte sein: {kategorien}
   Waehle die naechstliegende Kategorie, auch wenn die Passung unvollkommen ist.

4. capex_ma_signale
   Aussagen zu Investitionen, Akquisitionen, Beteiligungen oder Desinvestitionen.

TEXTAUSZUG:
{text}
"""

SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "strategische_prioritaeten": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {"prioritaet": {"type": "STRING"}, "zitat": {"type": "STRING"}},
                "required": ["prioritaet", "zitat"],
            },
        },
        "wachstumsmaerkte": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "region": {"type": "STRING", "enum": REGIONEN},
                    "aussage": {"type": "STRING"},
                    "zitat": {"type": "STRING"},
                },
                "required": ["region", "aussage", "zitat"],
            },
        },
        "hauptrisiken": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "risiko": {"type": "STRING"},
                    "kategorie": {"type": "STRING", "enum": RISIKO_KATEGORIEN},
                    "zitat": {"type": "STRING"},
                },
                "required": ["risiko", "kategorie", "zitat"],
            },
        },
        "capex_ma_signale": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {"aussage": {"type": "STRING"}, "zitat": {"type": "STRING"}},
                "required": ["aussage", "zitat"],
            },
        },
    },
    "required": ["strategische_prioritaeten", "wachstumsmaerkte", "hauptrisiken", "capex_ma_signale"],
}

FELDER = ["strategische_prioritaeten", "wachstumsmaerkte", "hauptrisiken", "capex_ma_signale"]

# ---------------------------------------------------------------------------
# 7. Modellaufruf mit Cache und Wiederholung
# ---------------------------------------------------------------------------

def _client():
    schluessel = os.environ.get("GEMINI_API_KEY")
    if not schluessel:
        sys.exit("FEHLER: Umgebungsvariable GEMINI_API_KEY ist nicht gesetzt.")
    from google import genai
    return genai.Client(api_key=schluessel)


def modelle_auflisten():
    client = _client()
    print("Verfuegbare Modelle fuer diesen Schluessel:\n")
    for m in client.models.list():
        aktionen = getattr(m, "supported_actions", None) or []
        if not aktionen or "generateContent" in aktionen:
            print("  " + str(m.name))


def modelle_pruefen():
    """Sendet an jeden Kandidaten eine winzige Anfrage und meldet, wer antwortet.
    Kostet praktisch nichts und beantwortet die Frage, welches Modell gerade
    verfuegbar ist, in unter einer Minute."""
    client = _client()
    from google.genai import types
    config = types.GenerateContentConfig(temperature=0.0, max_output_tokens=16)
    print("Teste Modelle mit einer Minimalanfrage:\n")
    brauchbar = []
    for name in MODELL_KANDIDATEN:
        start = time.time()
        try:
            client.models.generate_content(
                model=name, contents="Antworte mit dem Wort OK.", config=config)
            dauer = time.time() - start
            print("  %-26s OK   (%.1fs)" % (name, dauer))
            brauchbar.append((dauer, name))
        except Exception as e:
            m = str(e)
            if "503" in m or "UNAVAILABLE" in m:
                grund = "ueberlastet (503)"
            elif "429" in m or "RESOURCE_EXHAUSTED" in m:
                grund = "Kontingent erschoepft (429)"
            elif "404" in m or "NOT_FOUND" in m:
                grund = "nicht freigeschaltet (404)"
            else:
                grund = m.split("\n")[0][:70]
            print("  %-26s --   %s" % (name, grund))
    if brauchbar:
        # Nicht der neueste, sondern der schnellste. Eine hohe Latenz schon bei
        # einer 16-Token-Antwort zeigt an, dass der Endpunkt unter Last steht.
        # Genau dort kippt die echte Anfrage mit 25.000 Tokens in einen 503.
        brauchbar.sort()
        print("\nEmpfehlung: --model %s (schnellste Antwort)" % brauchbar[0][1])
        if len(brauchbar) > 1:
            print("Ausweich: --model %s" % brauchbar[1][1])
    else:
        print("\nKein Kandidat antwortet. Spaeter erneut versuchen.")


def _fehler_protokollieren(cache_pfad, model, fehler):
    """Schreibt die vollstaendige Fehlermeldung neben den Cache. Ein abgebrochener
    Chunk soll spaeter erklaerbar sein, nicht nur gezaehlt."""
    try:
        pfad = os.path.splitext(cache_pfad)[0] + ".fehler.txt"
        with open(pfad, "a") as f:
            f.write("%s | %s | %s\n\n" % (time.strftime("%Y-%m-%d %H:%M:%S"),
                                            model, str(fehler)))
    except Exception:
        pass


def _config(mit_denkbudget):
    from google.genai import types
    kwargs = dict(temperature=0.0,
                  response_mime_type="application/json",
                  response_schema=SCHEMA)
    if mit_denkbudget:
        # Fuer eine schematisierte Extraktion bringt langes internes Nachdenken
        # wenig, erhoeht aber Rechenzeit je Anfrage und damit die Wahrscheinlichkeit
        # eines 503. Wird vom Modell der Parameter nicht akzeptiert, faellt der
        # Aufruf automatisch auf die Konfiguration ohne Denkbudget zurueck.
        try:
            kwargs["thinking_config"] = types.ThinkingConfig(thinking_budget=0)
        except Exception:
            pass
    return types.GenerateContentConfig(**kwargs)


# Wartezeiten im strikten Modus, in Sekunden. Danach gilt der Chunk als gescheitert.
# Summe rund 32 Minuten je Chunk. Bewusst endlich: Ein Lauf, der unbegrenzt wartet,
# haengt im Zweifel bis zum naechsten Morgen an einer einzigen Anfrage.
STRIKT_WARTEZEITEN = [20, 40, 60, 90, 120, 180, 240, 300, 300, 300, 300]

# Kennzeichen eines Tageslimits im Fehlertext von Google. Ein Minutenlimit loest
# sich durch Warten, ein Tageslimit nicht. Gemessen am Konto: 20 Anfragen pro Tag
# und Modell im kostenlosen Zugang, bei 250.000 Tokens pro Minute. Der Engpass ist
# also die Anzahl der Anfragen, nicht deren Groesse.
TAGESLIMIT_MARKER = ["perday", "per day", "requestsperday", "generaterequestsperday",
                     "daily limit", "quota_limit_value"]


class TageslimitErreicht(Exception):
    """Beendet den gesamten Lauf, statt bei jedem weiteren Chunk erneut zu warten."""
    pass


def _ist_tageslimit(meldung):
    m = meldung.lower().replace("_", "").replace(" ", "")
    return any(x.replace("_", "").replace(" ", "") in m for x in TAGESLIMIT_MARKER)


def modell_aufrufen(client, modelle, prompt, cache_pfad, versuche_je_modell=3,
                    strikt=False):
    """Fragt die Modelle der Reihe nach, bis eines antwortet.

    Cache-Schluessel ist der Prompt, nicht das Modell. Welches Modell geantwortet
    hat, steht als "_modell" in der Cache-Datei und wandert in die Ergebnisdatei.
    Ein Lauf, in dem ein Teil der Chunks von einem Ausweichmodell stammt, ist damit
    nachvollziehbar statt stillschweigend gemischt.
    """
    if os.path.exists(cache_pfad):
        with open(cache_pfad, "r") as f:
            return json.load(f), True

    if strikt:
        # Kein Modellwechsel. Ein gemischter Datensatz ist im Unternehmensvergleich
        # nicht auswertbar, weil die Zitattreue je Modellversion zwischen 64 und
        # 98 Prozent schwankt (gemessen im Lauf vom 04./05.09.2026).
        modelle = modelle[:1]
        versuche_je_modell = len(STRIKT_WARTEZEITEN) + 1

    letzter_fehler = None
    for m_index, model in enumerate(modelle):
        for versuch in range(1, versuche_je_modell + 1):
            for denkbudget in (True, False):
                try:
                    antwort = client.models.generate_content(
                        model=model, contents=prompt, config=_config(denkbudget))
                    daten = json.loads(antwort.text)
                    daten["_modell"] = model
                    with open(cache_pfad, "w") as f:
                        json.dump(daten, f, ensure_ascii=False, indent=2)
                    return daten, False
                except Exception as e:
                    meldung = str(e)
                    letzter_fehler = e
                    if ("thinking" in meldung.lower() or "thinking_config" in meldung
                            or "400" in meldung or "INVALID_ARGUMENT" in meldung):
                        # Die 400-Meldung von Google nennt den Grund nicht. Beobachtet
                        # bei gemini-3.6-flash, 19 Vorkommen. Wahrscheinlichste Ursache
                        # ist der nicht akzeptierte Denkbudget-Parameter, deshalb ein
                        # Versuch ohne ihn, bevor das Modell gewechselt wird.
                        continue
                    break            # anderer Fehler, Denkbudget ist nicht die Ursache

            meldung = str(letzter_fehler)
            ist_429 = "429" in meldung or "RESOURCE_EXHAUSTED" in meldung
            ist_503 = "503" in meldung or "UNAVAILABLE" in meldung
            if ist_429 and _ist_tageslimit(meldung):
                raise TageslimitErreicht(
                    "Tageskontingent fuer %s ist aufgebraucht." % model)
            if not (ist_429 or ist_503):
                # 400 und andere Fehler sind modellspezifisch. Statt abzubrechen wird
                # das naechste Modell der Kette probiert. Die volle Meldung landet im
                # Protokoll, damit die Ursache spaeter nachvollziehbar ist.
                _fehler_protokollieren(cache_pfad, model, letzter_fehler)
                print("    %s meldet: %s" % (model, meldung.replace("\n", " ")[:150]))
                break
            if versuch < versuche_je_modell:
                if strikt:
                    warte = STRIKT_WARTEZEITEN[min(versuch - 1,
                                                   len(STRIKT_WARTEZEITEN) - 1)]
                else:
                    warte = (30 * versuch) if ist_429 else (10 * versuch)
                print("    %s bei %s, warte %ds (%d/%d)"
                      % ("Kontingent 429" if ist_429 else "Ueberlastung 503",
                         model, warte, versuch, versuche_je_modell))
                time.sleep(warte)

        if m_index + 1 < len(modelle):
            print("    %s antwortet nicht, wechsle auf %s"
                  % (model, modelle[m_index + 1]))

    print("\n    Kein Modell hat geantwortet. Zuletzt: %s" % str(letzter_fehler)[:160])
    print("    Erfolgreiche Chunks liegen im Cache, ein Neustart setzt dort auf.")
    raise letzter_fehler


# ---------------------------------------------------------------------------
# 8. Ein Unternehmen verarbeiten
# ---------------------------------------------------------------------------

def unternehmen_verarbeiten(key, model, dry_run=False, strikt=False):
    meta = REPORTS[key]
    pdf_pfad = os.path.join(PDF_DIR, meta["datei"])
    if not os.path.exists(pdf_pfad):
        sys.exit("FEHLER: %s nicht gefunden." % pdf_pfad)

    print("\n=== %s (%s)" % (meta["name"], meta["datei"]))
    seiten = seiten_laden(pdf_pfad)
    pua_bericht()
    korpus = Korpus(seiten)
    abschnitte = abschnitte_klassifizieren(seiten)
    indizes = seiten_auswaehlen(seiten)
    chunks = chunks_bauen(seiten, indizes)

    zeichen_gesamt = sum(len(s) for s in seiten)
    zeichen_gewaehlt = sum(len(seiten[i]) for i in indizes)
    anteil = 100.0 * zeichen_gewaehlt / max(1, zeichen_gesamt)
    print("    Seiten gesamt: %d, ausgewaehlt: %d (%.1f%% der Zeichen)"
          % (len(seiten), len(indizes), anteil))
    print("    Chunks: %d, geschaetzte Eingabe: %d Tokens"
          % (len(chunks), int(zeichen_gewaehlt / 3.3)))

    if dry_run:
        print("    Trockenlauf, kein Modellaufruf.")
        return None

    # Im strikten Modus bekommt jedes Modell ein eigenes Cacheverzeichnis. Sonst
    # wuerde ein Einmodelllauf die Antworten eines frueheren gemischten Laufs
    # wiederverwenden und waere damit gar kein Einmodelllauf.
    cache_verzeichnis = (os.path.join(CACHE_DIR, model, key) if strikt
                         else os.path.join(CACHE_DIR, key))
    os.makedirs(cache_verzeichnis, exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True)
    client = _client()

    roh = dict((f, []) for f in FELDER)
    benutzte_modelle = set()
    fehlgeschlagen = []
    for nr, chunk in enumerate(chunks, start=1):
        prompt = PROMPT.format(unternehmen=meta["name"], jahr=meta["jahr"],
                               regionen=", ".join(REGIONEN),
                               kategorien=", ".join(RISIKO_KATEGORIEN),
                               text=chunk)
        sig = hashlib.sha256(prompt.encode("utf-8")).hexdigest()[:16]
        cache_pfad = os.path.join(cache_verzeichnis, "chunk%02d_%s.json" % (nr, sig))
        kette = [model] + [m for m in MODELL_KANDIDATEN if m != model]
        try:
            daten, aus_cache = modell_aufrufen(client, kette, prompt, cache_pfad,
                                               strikt=strikt)
        except TageslimitErreicht:
            raise
        except Exception as e:
            # Ein einzelner Chunk darf einen Lauf ueber Dutzende Anfragen nicht
            # beenden. Der Ausfall wird gezaehlt, protokolliert und im Ergebnis
            # ausgewiesen, damit die Abdeckung ehrlich bleibt.
            fehlgeschlagen.append({"chunk": nr, "fehler": str(e)[:300]})
            print("    Chunk %d/%d UEBERSPRUNGEN nach Fehler" % (nr, len(chunks)))
            continue
        benutzte_modelle.add(daten.get("_modell", model))
        anzahl = sum(len(daten.get(f, [])) for f in FELDER)
        hinweis = " (Cache)" if aus_cache else ""
        if daten.get("_modell") and daten["_modell"] != model:
            hinweis += " [Ausweichmodell %s]" % daten["_modell"]
        print("    Chunk %d/%d: %d Elemente%s" % (nr, len(chunks), anzahl, hinweis))
        for f in FELDER:
            roh[f].extend(daten.get(f, []))

    # Zitate verorten
    ergebnis = {
        "unternehmen": meta["name"],
        "schluessel": key,
        "berichtsjahr": meta["jahr"],
        "gruppe": meta["gruppe"],
        "quelldatei": meta["datei"],
        "modell": model,
        "tatsaechlich_benutzte_modelle": sorted(benutzte_modelle),
        "strikter_modus": strikt,
        "chunks_gesamt": len(chunks),
        "chunks_fehlgeschlagen": fehlgeschlagen,
        "seiten_im_pdf": len(seiten),
        "seiten_ausgewertet": len(indizes),
    }
    statistik = {}
    for f in FELDER:
        liste = []
        for element in roh[f]:
            seite, typ, stellen = korpus.suche(element.get("zitat", ""))
            element["beleg_seite"] = seite
            element["treffertyp"] = typ
            element["zitat_gefunden"] = typ in ("exakt", "exakt_nach_normalisierung",
                                                "exakt_mehrdeutig", "teilweise")
            if len(stellen) > 1:
                element["weitere_fundstellen"] = stellen[1:]
            if seite:
                element["quelle_abschnitt"] = abschnitte[seite - 1]
            else:
                element["quelle_abschnitt"] = "unbekannt"
            statistik[typ] = statistik.get(typ, 0) + 1
            liste.append(element)
        ergebnis[f] = liste

    ergebnis["zitatpruefung"] = statistik
    gesamt = sum(statistik.values())
    if gesamt:
        teile = ", ".join("%d %s" % (v, k) for k, v in sorted(statistik.items()))
        print("    Zitatpruefung von %d Elementen: %s" % (gesamt, teile))

    nh = sum(1 for f in FELDER for e in ergebnis[f]
             if e.get("quelle_abschnitt") == "Nachhaltigkeitsberichterstattung")
    nh_seiten = sum(1 for i in indizes if abschnitte[i] == "Nachhaltigkeitsberichterstattung")
    ergebnis["abschnittsverteilung"] = {
        "elemente_nachhaltigkeitsberichterstattung": nh,
        "elemente_geschaeftsbericht": gesamt - nh,
        "ausgewertete_seiten_nachhaltigkeitsberichterstattung": nh_seiten,
    }
    if gesamt:
        print("    Herkunft: %d aus dem Geschaeftsbericht, %d aus der "
              "Nachhaltigkeitsberichterstattung (%.0f%%)"
              % (gesamt - nh, nh, 100.0 * nh / gesamt))

    ziel = os.path.join(DATA_DIR, key + ".json")
    if strikt:
        os.makedirs(os.path.join(DATA_DIR, model), exist_ok=True)
        ziel = os.path.join(DATA_DIR, model, key + ".json")
    with open(ziel, "w") as f:
        json.dump(ergebnis, f, ensure_ascii=False, indent=2)
    print("    Geschrieben: %s" % os.path.relpath(ziel, HERE))
    return ergebnis

# ---------------------------------------------------------------------------
# 9. CSV
# ---------------------------------------------------------------------------

def csv_schreiben(unterordner=None):
    zeilen = []
    basis = os.path.join(DATA_DIR, unterordner) if unterordner else DATA_DIR
    for key in REPORTS:
        pfad = os.path.join(basis, key + ".json")
        if not os.path.exists(pfad):
            continue
        with open(pfad) as f:
            d = json.load(f)
        for feld in FELDER:
            for e in d.get(feld, []):
                zeilen.append({
                    "unternehmen": d["unternehmen"],
                    "schluessel": d["schluessel"],
                    "berichtsjahr": d["berichtsjahr"],
                    "gruppe": d["gruppe"],
                    "feld": feld,
                    "wert": e.get("prioritaet") or e.get("risiko") or e.get("aussage") or "",
                    "region": e.get("region", ""),
                    "kategorie": e.get("kategorie", ""),
                    "beleg_seite": e.get("beleg_seite", ""),
                    "treffertyp": e.get("treffertyp", ""),
                    "quelle_abschnitt": e.get("quelle_abschnitt", ""),
                    "weitere_fundstellen": " ".join(str(x) for x in e.get("weitere_fundstellen", [])),
                    "zitat_gefunden": e.get("zitat_gefunden", ""),
                    "zitat": e.get("zitat", ""),
                })
    if not zeilen:
        print("Keine Daten fuer results.csv vorhanden.")
        return
    ziel = os.path.join(HERE, "results_%s.csv" % unterordner if unterordner else "results.csv")
    with open(ziel, "w") as f:
        w = csv.DictWriter(f, fieldnames=list(zeilen[0].keys()))
        w.writeheader()
        w.writerows(zeilen)
    print("\nresults.csv geschrieben: %d Zeilen" % len(zeilen))

# ---------------------------------------------------------------------------

def _fortschritt_zeigen(keys, model=None, strikt=False):
    """Zaehlt vor dem Start, wie viele Chunks bereits im Cache liegen. Bei einem
    Tageslimit von 20 Anfragen erstreckt sich ein Vollauf ueber mehrere Tage,
    deshalb gehoert der Stand an den Anfang und nicht ans Ende."""
    offen = fertig = 0
    for k in keys:
        meta = REPORTS[k]
        pfad = os.path.join(PDF_DIR, meta["datei"])
        if not os.path.exists(pfad):
            continue
        seiten = seiten_laden(pfad)
        chunks = chunks_bauen(seiten, seiten_auswaehlen(seiten))
        for nr, c in enumerate(chunks, start=1):
            prompt = PROMPT.format(unternehmen=meta["name"], jahr=meta["jahr"],
                                   regionen=", ".join(REGIONEN),
                                   kategorien=", ".join(RISIKO_KATEGORIEN), text=c)
            sig = hashlib.sha256(prompt.encode("utf-8")).hexdigest()[:16]
            verz = os.path.join(CACHE_DIR, model, k) if strikt else os.path.join(CACHE_DIR, k)
            if os.path.exists(os.path.join(verz, "chunk%02d_%s.json" % (nr, sig))):
                fertig += 1
            else:
                offen += 1
    print("Stand: %d von %d Chunks im Cache, %d offen." % (fertig, fertig + offen, offen))
    if offen:
        print("Bei 20 Anfragen pro Tag und Modell sind das noch rund %d Tag(e).\n"
              % max(1, (offen + 19) // 20))


def main():
    p = argparse.ArgumentParser(description="Extraktion aus ATX-Geschaeftsberichten")
    p.add_argument("--company", help="Schluessel, z.B. palfinger")
    p.add_argument("--all", action="store_true", help="alle sieben Unternehmen")
    p.add_argument("--dry-run", action="store_true", help="nur Auswahl und Chunking zeigen")
    p.add_argument("--list-models", action="store_true", help="verfuegbare Modelle anzeigen")
    p.add_argument("--probe", action="store_true", help="testen, welches Modell gerade antwortet")
    p.add_argument("--strict-model", action="store_true",
                   help="kein Modellwechsel, stattdessen geduldig warten")
    p.add_argument("--model", default=DEFAULT_MODEL)
    a = p.parse_args()

    if a.list_models:
        modelle_auflisten()
        return

    if a.probe:
        modelle_pruefen()
        return

    if a.all:
        keys = list(REPORTS.keys())
        _fortschritt_zeigen(keys, a.model, a.strict_model)
    elif a.company:
        if a.company not in REPORTS:
            sys.exit("Unbekannt: %s. Moeglich: %s" % (a.company, ", ".join(REPORTS)))
        keys = [a.company]
    else:
        p.print_help()
        return

    probleme = []
    for k in keys:
        try:
            ergebnis = unternehmen_verarbeiten(k, a.model, dry_run=a.dry_run,
                                               strikt=a.strict_model)
            if ergebnis and ergebnis.get("chunks_fehlgeschlagen"):
                probleme.append("%s: %d von %d Chunks fehlgeschlagen"
                                % (k, len(ergebnis["chunks_fehlgeschlagen"]),
                                   ergebnis["chunks_gesamt"]))
        except TageslimitErreicht as e:
            print("\n" + "=" * 60)
            print("TAGESKONTINGENT AUFGEBRAUCHT: %s" % e)
            print("Der Lauf wird hier beendet, weiteres Warten waere zwecklos.")
            print("Alles bisher Erfolgreiche liegt im Cache.")
            print("Morgen denselben Befehl erneut aufrufen, er setzt genau hier auf.")
            print("=" * 60)
            probleme.append("%s: Tageskontingent aufgebraucht" % k)
            break
        except Exception as e:
            probleme.append("%s: komplett abgebrochen, %s" % (k, str(e)[:200]))
            print("\n!!! %s abgebrochen: %s\n" % (k, str(e)[:200]))

    if probleme:
        print("\n" + "=" * 60)
        print("UNVOLLSTAENDIGE VERARBEITUNG:")
        for x in probleme:
            print("  " + x)
        print("Erneuter Aufruf setzt am Cache auf und wiederholt nur die Luecken.")
        print("=" * 60)

    if not a.dry_run:
        csv_schreiben(a.model if a.strict_model else None)


if __name__ == "__main__":
    main()
