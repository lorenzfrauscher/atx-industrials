#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pruefliste.py -- erzeugt die Arbeitsliste fuer die Handpruefung in Schritt 3

Fuer jedes extrahierte Element der gezogenen Stichprobe wird ausgegeben:
  Seite, Feldtyp, abgeleitete Aussage, woertliches Zitat und der Textausschnitt
  aus dem Bericht, der das Zitat umgibt.

Der Umgebungstext ist der eigentliche Zweck. Ohne ihn muesstest du 134 Mal im PDF
blaettern. Mit ihm laesst sich der Grossteil der Faelle direkt beurteilen, und das
PDF wird nur noch fuer Zweifelsfaelle und eine Kontrollstichprobe geoeffnet.

Ausgabe:
  pruefliste.md   zum Lesen und Abarbeiten
  pruefliste.csv  zum Eintragen der Urteile, oeffnet sich in Excel

Aufruf:
  python3 pruefliste.py --input data/gemini-3.8-flash
"""

import argparse
import csv
import io
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import extract as E

FELDER = E.FELDER
KONTEXT_ZEICHEN = 420

# Stichprobe aus verification.md, gezogen am 05.09.2026 mit Seed 20260905,
# bevor die Ergebnisdaten vorlagen.
STICHPROBE = ["andritz", "voestalpine", "wienerberger"]

URTEILE = """korrekt              Aussage gibt den Berichtsinhalt zutreffend wieder
seitenangabe_falsch  Zitat vorhanden, aber auf einer anderen Seite
zitat_erfunden       Zitat steht so nicht im Bericht
inhalt_verzerrt      Zitat korrekt, abgeleitete Aussage verdreht oder ueberdehnt es
kontext_entrissen    Zitat korrekt, ergibt ohne Umgebung einen anderen Sinn
kategorie_falsch     Risikokategorie oder Region unpassend zugeordnet
unklar               nicht eindeutig entscheidbar, wird gesondert ausgewiesen"""


def kontext(korpus, zitat, seite):
    """Liefert lesbaren Umgebungstext im Originalsatzbau.

    Zweistufige Suche auf der Seite, aus demselben Grund wie in der Zitatsuche:
      1. Woertlich, mit flexiblen Trennzeichen zwischen den ersten Woertern.
      2. Ohne Leerzeichen und Satzzeichen. Faengt Extraktionsartefakte wie
         "d as" statt "das" ab, an denen Stufe 1 scheitert.

    Stufe 2 wurde nachtraeglich ergaenzt: Bei 9 der 134 Eintraege der Stichprobe
    fand Stufe 1 das Zitat nicht, obwohl die Zitatsuche der Pipeline es als
    gefunden auswies. Ein unbrauchbarer Umgebungstext zwingt zum Blaettern im PDF
    und untergraebt den Zweck der Liste.
    """
    if not seite or not (1 <= seite <= len(korpus.seiten_roh)):
        return "[Keine Seite bestimmbar. Zitat vermutlich erfunden.]"

    roh = korpus.seiten_roh[seite - 1]
    roh_flach = re.sub(r"\s+", " ", roh).strip()

    treffer = None
    woerter = [w for w in re.split(r"\s+", zitat.strip()) if w][:6]
    if woerter:
        muster = r"[\s\-]*".join(re.escape(w) for w in woerter)
        m = re.search(muster, roh_flach, re.IGNORECASE)
        if m:
            treffer = m.start()

    if treffer is None:
        # Stufe 2: Position ueber den zeichenbereinigten Strom bestimmen und
        # zurueck auf den Rohtext abbilden.
        klein = roh_flach.lower()
        karte = [i for i, c in enumerate(klein) if c.isalnum()]
        strom = "".join(klein[i] for i in karte)
        ziel = "".join(c for c in E.normalisieren(zitat) if c.isalnum())[:60]
        if len(ziel) >= 20:
            pos = strom.find(ziel)
            if pos >= 0:
                treffer = karte[pos]

    if treffer is None:
        return "[Zitat auf dieser Seite nicht wiederfindbar. Seitenanfang:] " + \
               roh_flach[:KONTEXT_ZEICHEN]

    a = max(0, treffer - KONTEXT_ZEICHEN // 3)
    b = min(len(roh_flach), treffer + len(zitat) + KONTEXT_ZEICHEN // 2)
    return ("..." if a > 0 else "") + roh_flach[a:b] + ("..." if b < len(roh_flach) else "")


def bestehende_urteile():
    """Liest Urteile aus einer vorhandenen Liste, damit ein Neuaufbau keine
    Handarbeit vernichtet. Gelesen wird zuerst die xlsx, dann die csv.
    Spaltennamen werden case-insensitiv gesucht, weil Excel sie beim Speichern
    umbenennt (aus "id" wird "Id")."""
    for name, leser in (("pruefliste.xlsx", "xlsx"), ("pruefliste.csv", "csv")):
        pfad = os.path.join(HERE, name)
        if not os.path.exists(pfad):
            continue
        try:
            if leser == "xlsx":
                import openpyxl
                ws = openpyxl.load_workbook(pfad, data_only=True).active
                zeilen = [[c.value for c in r] for r in ws.iter_rows()]
            else:
                zeilen = list(csv.reader(io.open(pfad, encoding="utf-8-sig")))
            kopf = [str(c or "").strip().lower() for c in zeilen[0]]
            i_id, i_u, i_a = kopf.index("id"), kopf.index("urteil"), kopf.index("anmerkung")
        except Exception as e:
            print("   Hinweis: %s nicht lesbar (%s), uebersprungen." % (name, e))
            continue
        alt = {}
        for r in zeilen[1:]:
            if not r or not r[i_id]:
                continue
            u = str(r[i_u] or "").strip()
            a = str(r[i_a] or "").strip()
            if u:
                alt[str(r[i_id]).strip()] = (u, a)
        if alt:
            print("   %d bestehende Urteile aus %s uebernommen." % (len(alt), name))
            return alt
    return {}


def xlsx_schreiben(zeilen, ziel):
    """Schreibt eine arbeitsfertige Arbeitsmappe: Spaltenbreiten, Zeilenumbruch
    fuer die Textspalten, fixierte Kopfzeile. Die xlsx ist die Arbeitsdatei, die
    csv wird daraus am Ende fuer das Repository erzeugt."""
    try:
        import openpyxl
        from openpyxl.styles import Alignment, Font, PatternFill
    except ImportError:
        print("   openpyxl fehlt, xlsx uebersprungen. Installieren mit: pip install openpyxl")
        return
    kopf = list(zeilen[0].keys())
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = "pruefliste"
    ws.append([k for k in kopf])
    for z in zeilen:
        ws.append([z[k] for k in kopf])

    breiten = {"id": 10, "unternehmen": 16, "beleg_seite": 8, "feld": 24,
               "region_oder_kategorie": 16, "quelle_abschnitt": 16, "treffertyp": 22,
               "aussage": 55, "zitat": 70, "umgebung": 90, "urteil": 22, "anmerkung": 45}
    umbruch = {"aussage", "zitat", "umgebung", "anmerkung"}
    for i, k in enumerate(kopf, start=1):
        b = openpyxl.utils.get_column_letter(i)
        ws.column_dimensions[b].width = breiten.get(k, 18)
        for zelle in ws[b]:
            zelle.alignment = Alignment(wrap_text=(k in umbruch), vertical="top")
    for zelle in ws[1]:
        zelle.font = Font(bold=True)
        zelle.fill = PatternFill("solid", fgColor="E8E8E4")
        zelle.alignment = Alignment(vertical="center")
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    wb.save(ziel)
    print("   geschrieben: %s" % os.path.basename(ziel))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default=os.path.join(HERE, "data", "gemini-3.8-flash"))
    a = p.parse_args()

    md = ["# Prueferliste Schritt 3\n",
          "Stichprobe: **%s**, gezogen am 05.09.2026 mit Seed 20260905, "
          "vor Vorliegen der Ergebnisdaten.\n" % ", ".join(STICHPROBE),
          "## So arbeitest du damit\n",
          "Jeder Eintrag zeigt das Zitat und den Text, der es im Bericht umgibt. "
          "In den meisten Faellen genuegt das fuer ein Urteil. Das PDF brauchst du nur "
          "fuer Zweifelsfaelle und fuer die Kontrollstichprobe am Ende.\n",
          "Trag dein Urteil in `pruefliste.csv` in die Spalte `urteil` ein. "
          "Mehrere Urteile mit Komma trennen. Erlaubte Werte:\n",
          "```\n" + URTEILE + "\n```\n",
          "Elemente mit dem Treffertyp `nicht_gefunden` oder `teilweise` sind "
          "vorsortiert die interessanten. Sie stehen trotzdem an ihrer Seitenposition, "
          "damit du den Bericht einmal von vorne nach hinten durchgehen kannst.\n"]

    alt_urteile = bestehende_urteile()
    zeilen = []
    lfd = 0
    for key in STICHPROBE:
        pfad = os.path.join(a.input, key + ".json")
        if not os.path.exists(pfad):
            sys.exit("Fehlt: %s" % pfad)
        d = json.load(open(pfad))
        meta = E.REPORTS[key]
        korpus = E.Korpus(E.seiten_laden(os.path.join(E.PDF_DIR, meta["datei"])))

        elemente = []
        for feld in FELDER:
            for e in d.get(feld, []):
                elemente.append((feld, e))
        elemente.sort(key=lambda x: (x[1].get("beleg_seite") or 9999, x[0]))

        md.append("\n---\n\n# %s  (%s, %d Elemente)\n"
                  % (d["unternehmen"], meta["datei"], len(elemente)))

        for feld, e in elemente:
            lfd += 1
            kennung = "%s-%03d" % (key[:3].upper(), lfd)
            seite = e.get("beleg_seite")
            zusatz = e.get("region") or e.get("kategorie") or ""
            aussage = e.get("prioritaet") or e.get("risiko") or e.get("aussage") or ""
            typ = e.get("treffertyp", "")
            marke = "  **PRUEFEN**" if typ in ("nicht_gefunden", "teilweise",
                                               "exakt_mehrdeutig") else ""
            md.append("\n### %s | PDF-Seite %s | %s%s%s\n"
                      % (kennung, seite if seite else "keine", feld,
                         " / " + zusatz if zusatz else "", marke))
            md.append("**Aussage:** %s\n" % aussage)
            md.append("**Zitat:** „%s“\n" % e.get("zitat", ""))
            md.append("**Treffertyp:** `%s`%s\n"
                      % (typ, "  (weitere Fundstellen: %s)"
                         % ", ".join(str(x) for x in e["weitere_fundstellen"])
                         if e.get("weitere_fundstellen") else ""))
            umgebung = kontext(korpus, e.get("zitat", ""), seite).replace("\n", " ")
            md.append("**Umgebung im Bericht:**\n")
            md.append("> " + umgebung + "\n")

            zeilen.append({
                "id": kennung,
                "unternehmen": d["unternehmen"],
                "beleg_seite": seite if seite else "",
                "feld": feld,
                "region_oder_kategorie": zusatz,
                "quelle_abschnitt": e.get("quelle_abschnitt", ""),
                "treffertyp": typ,
                "aussage": aussage,
                "zitat": e.get("zitat", ""),
                # Der Umgebungstext steht bewusst auch in der CSV. Ohne ihn liesse
                # sich in Excel nur pruefen, ob die Aussage zum Zitat passt, nicht
                # aber, ob die Umgebung den Sinn veraendert.
                "umgebung": umgebung,
                "urteil": alt_urteile.get(kennung, ("", ""))[0],
                "anmerkung": alt_urteile.get(kennung, ("", ""))[1],
            })

    # Kontrollstichprobe: 10 Prozent, die zusaetzlich im echten PDF geprueft werden.
    # Zweck ist nicht das Element, sondern der Nachweis, dass der extrahierte Text
    # mit dem Dokument uebereinstimmt.
    random.seed(20260905)
    kontrolle = sorted(random.sample([z["id"] for z in zeilen],
                                     max(5, len(zeilen) // 10)))
    for z in zeilen:
        if z["id"] in kontrolle and not z["anmerkung"]:
            z["anmerkung"] = "KONTROLLE: zusaetzlich im PDF pruefen"
    md.append("\n---\n\n## Kontrollstichprobe\n")
    md.append("Diese %d Eintraege bitte zusaetzlich im echten PDF nachschlagen. "
              "Geprueft wird dabei nicht das Element, sondern ob der extrahierte "
              "Text mit dem Dokument uebereinstimmt. Seed 20260905.\n" % len(kontrolle))
    md.append("`" + "`, `".join(kontrolle) + "`\n")

    io.open(os.path.join(HERE, "pruefliste.md"), "w",
            encoding="utf-8").write("\n".join(md) + "\n")
    # utf-8-sig statt utf-8: Das BOM zwingt Excel unter macOS zur richtigen
    # Kodierung. Ohne es liest Excel die Datei als MacRoman und zeigt aus
    # "Geschaeftsbericht" ein "Gesch√§ftsbericht".
    with io.open(os.path.join(HERE, "pruefliste.csv"), "w",
                 encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(zeilen[0].keys()))
        w.writeheader()
        w.writerows(zeilen)
    xlsx_schreiben(zeilen, os.path.join(HERE, "pruefliste.xlsx"))
    print("pruefliste.md und pruefliste.csv geschrieben: %d Elemente, "
          "davon %d Kontrollstichprobe" % (len(zeilen), len(kontrolle)))
    for key in STICHPROBE:
        n = sum(1 for z in zeilen if z["id"].startswith(key[:3].upper()))
        p = sum(1 for z in zeilen if z["id"].startswith(key[:3].upper())
                and z["treffertyp"] in ("nicht_gefunden", "teilweise", "exakt_mehrdeutig"))
        print("   %-14s %3d Elemente, davon %2d mit Auffaelligkeit" % (key, n, p))


if __name__ == "__main__":
    main()
