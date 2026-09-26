#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
aggregate.py -- Auswertung der Extraktionsergebnisse

Liest die JSON-Dateien aus data/ und erzeugt:
  charts/heatmap_wachstumsmaerkte.png
  charts/risikokategorien.png
  befunde.md          Aggregattabellen als Text
  modellvergleich.md  paarweiser Vergleich, sofern zwei Cache-Bestaende vorliegen

Braucht keinen API-Schluessel und keine Netzverbindung.

Aufrufe
-------
  python3 aggregate.py
  python3 aggregate.py --input data/gemini-3.8-flash --suffix _38flash
  python3 aggregate.py --modellvergleich gemini-3.8-flash
"""

import argparse
import collections
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FELDER = ["strategische_prioritaeten", "wachstumsmaerkte",
          "hauptrisiken", "capex_ma_signale"]

# Farben aus der validierten Referenzpalette.
# Sequenzielles Blau fuer Groessenordnungen, ein einzelner Farbton fuer die
# einreihige Balkengrafik. Keine kategoriale Palette, weil beide Grafiken nur
# eine Serie zeigen. Zwei Farben wuerden eine Unterscheidung suggerieren, die
# in den Daten nicht steckt.
SEQ = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]
SERIE = "#2a78d6"
FLAECHE = "#fcfcfb"
TEXT = "#0b0b0b"
TEXT_SEK = "#52514e"
GITTER = "#e3e2df"

# Anzeigenamen je Sprache. Die ASCII-Schreibweise im Extraktionsschema bleibt
# unveraendert, damit die Kategorien stabil sind. Uebersetzt wird nur die Ausgabe.
ANZEIGE_DE = {
    "Oesterreich": "Österreich",
    "Europa uebrig": "Europa übrig",
    "Asien-Pazifik uebrig": "Asien-Pazifik übrig",
}
ANZEIGE_EN = {
    "Oesterreich": "Austria",
    "DACH": "DACH",
    "Europa uebrig": "Europe, other",
    "Nordamerika": "North America",
    "Lateinamerika": "Latin America",
    "China": "China",
    "Indien": "India",
    "Asien-Pazifik uebrig": "Asia-Pacific, other",
    "Naher Osten": "Middle East",
    "Afrika": "Africa",
    "Global": "Global",
}
KATEGORIE_EN = {
    "Markt": "Market", "Lieferkette": "Supply chain", "Regulierung": "Regulation",
    "Finanzierung": "Financing", "Technologie": "Technology",
}
TEXTE = {
    "de": {
        "heatmap_titel": "Genannte Wachstumsregionen je Unternehmen",
        "heatmap_unter": "Anzahl belegter Nennungen im Geschäftsbericht",
        "risiko_titel": "Nennungen je Risikokategorie, alle Unternehmen",
        "risiko_unter": "Feste Kategorienliste. Mehrfachnennungen eines Unternehmens zählen einzeln.",
    },
    "en": {
        "heatmap_titel": "Growth regions named, by company",
        "heatmap_unter": "Number of quote-verified mentions in the annual report",
        "risiko_titel": "Mentions per risk category, all companies",
        "risiko_unter": "Fixed category list. Repeated mentions by one company counted separately.",
    },
}
SPRACHE = ["de"]   # wird von main() gesetzt


def t(schluessel):
    return TEXTE[SPRACHE[0]][schluessel]


def anzeige(name):
    if SPRACHE[0] == "en":
        return ANZEIGE_EN.get(name, KATEGORIE_EN.get(name, name))
    return ANZEIGE_DE.get(name, name)

REIHENFOLGE_REGIONEN = [
    "Oesterreich", "DACH", "Europa uebrig", "Nordamerika", "Lateinamerika",
    "China", "Indien", "Asien-Pazifik uebrig", "Naher Osten", "Afrika", "Global",
]

# ---------------------------------------------------------------------------


def daten_laden(verzeichnis, nur_geschaeftsbericht=False):
    firmen = []
    for pfad in sorted(glob.glob(os.path.join(verzeichnis, "*.json"))):
        d = json.load(open(pfad))
        if nur_geschaeftsbericht:
            for f in FELDER:
                d[f] = [e for e in d.get(f, [])
                        if e.get("quelle_abschnitt") == "Geschaeftsbericht"]
        firmen.append(d)
    if not firmen:
        sys.exit("Keine JSON-Dateien in %s gefunden." % verzeichnis)
    return firmen


def _stil(ax):
    """Zurueckhaltend: kein Rahmen, ein feines Gitter, Beschriftung in Textfarbe."""
    for seite in ("top", "right", "left", "bottom"):
        ax.spines[seite].set_visible(False)
    ax.tick_params(colors=TEXT_SEK, length=0, labelsize=9)
    ax.set_facecolor(FLAECHE)


# ---------------------------------------------------------------------------
# Grafik 1: Heatmap Unternehmen mal genannte Wachstumsregion
# ---------------------------------------------------------------------------

def heatmap(firmen, ziel):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.colors import LinearSegmentedColormap

    namen = [f["unternehmen"] for f in firmen]
    zaehler = {}
    for f in firmen:
        for e in f.get("wachstumsmaerkte", []):
            r = e.get("region")
            if r:
                zaehler[(f["unternehmen"], r)] = zaehler.get((f["unternehmen"], r), 0) + 1
    regionen = [r for r in REIHENFOLGE_REGIONEN
                if any((n, r) in zaehler for n in namen)]
    if not regionen:
        print("  Heatmap uebersprungen, keine Regionen vorhanden.")
        return

    werte = [[zaehler.get((n, r), 0) for r in regionen] for n in namen]
    maxwert = max(max(z) for z in werte) or 1

    cmap = LinearSegmentedColormap.from_list("blau", SEQ)
    cmap.set_bad(FLAECHE)
    import numpy as np
    matrix = np.array(werte, dtype=float)
    # Null bedeutet "nicht genannt". Als hellster Blauton gelesen wirkte das wie
    # ein schwacher Wert. Maskiert wird die Zelle zur Flaeche und liest sich als
    # Abwesenheit.
    matrix = np.ma.masked_where(matrix == 0, matrix)

    fig, ax = plt.subplots(figsize=(1.4 + 0.78 * len(regionen), 0.46 * len(namen) + 2.0))
    fig.patch.set_facecolor(FLAECHE)
    ax.imshow(matrix, cmap=cmap, vmin=0, vmax=maxwert, aspect="auto")

    ax.set_xticks(range(len(regionen)))
    ax.set_xticklabels([anzeige(r) for r in regionen], rotation=35, ha="right")
    ax.set_yticks(range(len(namen)))
    ax.set_yticklabels(namen)
    # 2px Flaechenabstand zwischen den Zellen statt Gitterlinien
    ax.set_xticks([x - 0.5 for x in range(1, len(regionen))], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, len(namen))], minor=True)
    ax.grid(which="minor", color=FLAECHE, linewidth=2.5)
    ax.tick_params(which="minor", length=0)
    _stil(ax)

    for i in range(len(namen)):
        for j in range(len(regionen)):
            v = werte[i][j]
            if v:
                hell = v / float(maxwert) > 0.55
                ax.text(j, i, str(v), ha="center", va="center", fontsize=9,
                        color=FLAECHE if hell else TEXT)

    ax.set_title(t("heatmap_titel"), color=TEXT, fontsize=11, pad=14, loc="left")
    ax.text(0, -0.20, t("heatmap_unter"),
            transform=ax.transAxes, color=TEXT_SEK, fontsize=8.5, va="top")
    fig.tight_layout()
    # bbox_inches mit Rand, sonst schneidet die gedrehte Achsenbeschriftung die
    # rechte Spalte an.
    fig.savefig(ziel, dpi=200, facecolor=FLAECHE, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
    print("  geschrieben: %s" % os.path.relpath(ziel, HERE))


# ---------------------------------------------------------------------------
# Grafik 2: Haeufigkeit der Risikokategorien
# ---------------------------------------------------------------------------

def risikochart(firmen, ziel):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    z = collections.Counter()
    for f in firmen:
        for e in f.get("hauptrisiken", []):
            if e.get("kategorie"):
                z[e["kategorie"]] += 1
    if not z:
        print("  Risikochart uebersprungen, keine Risiken vorhanden.")
        return

    paare = z.most_common()
    labels = [anzeige(p[0]) for p in paare][::-1]
    werte = [p[1] for p in paare][::-1]

    fig, ax = plt.subplots(figsize=(6.6, 0.40 * len(labels) + 1.35))
    fig.patch.set_facecolor(FLAECHE)
    # Eine Serie, deshalb ein Farbton und keine Legende. Der Titel benennt sie.
    balken = ax.barh(range(len(labels)), werte, color=SERIE, height=0.46)
    for b in balken:
        b.set_joinstyle("round")

    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels)
    ax.set_xticks([])
    ax.xaxis.grid(False)
    _stil(ax)

    for i, v in enumerate(werte):
        ax.text(v + max(werte) * 0.015, i, str(v), va="center",
                fontsize=9, color=TEXT)

    ax.set_xlim(0, max(werte) * 1.10)
    ax.set_title(t("risiko_titel"), color=TEXT, fontsize=11, pad=14, loc="left")
    ax.set_ylim(-0.7, len(labels) - 0.3)
    ax.text(0, -0.13, t("risiko_unter"),
            transform=ax.transAxes, color=TEXT_SEK, fontsize=8.5, va="top")
    fig.tight_layout()
    # bbox_inches mit Rand, sonst schneidet die gedrehte Achsenbeschriftung die
    # rechte Spalte an.
    fig.savefig(ziel, dpi=200, facecolor=FLAECHE, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
    print("  geschrieben: %s" % os.path.relpath(ziel, HERE))


# ---------------------------------------------------------------------------
# Tabellen
# ---------------------------------------------------------------------------

def _tab(kopf, zeilen):
    aus = ["| " + " | ".join(kopf) + " |",
           "|" + "|".join(["---"] * len(kopf)) + "|"]
    for z in zeilen:
        aus.append("| " + " | ".join(str(x) for x in z) + " |")
    return "\n".join(aus)


def befunde_schreiben(alle, gb_only, ziel):
    t = ["# Aggregierte Befunde\n",
         "Erzeugt von `aggregate.py`. Alle Zahlen beziehen sich auf Elemente mit "
         "auffindbarem Beleg im Quelldokument.\n"]

    t.append("\n## 1. Umfang je Unternehmen\n")
    z = []
    for f in alle:
        n = dict((x, len(f.get(x, []))) for x in FELDER)
        av = f.get("abschnittsverteilung", {})
        ges = sum(n.values())
        nh = av.get("elemente_nachhaltigkeitsberichterstattung", 0)
        z.append([f["unternehmen"], f["gruppe"], ges,
                  n["strategische_prioritaeten"], n["wachstumsmaerkte"],
                  n["hauptrisiken"], n["capex_ma_signale"],
                  "%d (%.0f%%)" % (nh, 100.0 * nh / ges) if ges else "0"])
    t.append(_tab(["Unternehmen", "Gruppe", "gesamt", "Strategie", "Wachstum",
                   "Risiken", "Capex/M&A", "davon ESRS"], z))

    t.append("\n\n## 2. Belegqualität je Unternehmen\n")
    z = []
    for f in alle:
        p = f.get("zitatpruefung", {})
        ges = sum(p.values()) or 1
        woertlich = (p.get("exakt", 0) + p.get("exakt_nach_normalisierung", 0)
                     + p.get("exakt_mehrdeutig", 0))
        z.append([f["unternehmen"], sum(p.values()),
                  "%.0f%%" % (100.0 * woertlich / ges),
                  p.get("teilweise", 0), p.get("nicht_gefunden", 0),
                  ", ".join(f.get("tatsaechlich_benutzte_modelle", []))])
    t.append(_tab(["Unternehmen", "Elemente", "wörtlich belegt",
                   "nur teilweise", "nicht auffindbar", "Modell(e)"], z))

    t.append("\n\n## 3. Wachstumsregionen, nur Geschäftsbericht\n")
    zr = collections.Counter()
    firmen_je_region = collections.defaultdict(set)
    for f in gb_only:
        for e in f.get("wachstumsmaerkte", []):
            if e.get("region"):
                zr[e["region"]] += 1
                firmen_je_region[e["region"]].add(f["unternehmen"])
    t.append(_tab(["Region", "Nennungen", "Unternehmen"],
                  [[r, n, len(firmen_je_region[r])] for r, n in zr.most_common()]))

    t.append("\n\n## 4. Risikokategorien nach Gruppe\n")
    t.append("**Achtung bei der Lesart.** Bei sieben Unternehmen in einer "
             "Aufteilung von vier zu drei sind Häufigkeitsvergleiche zwischen den "
             "Gruppen statistisch nicht belastbar. Die Tabelle beschreibt, sie "
             "beweist nicht.\n")
    kat = collections.defaultdict(collections.Counter)
    for f in gb_only:
        for e in f.get("hauptrisiken", []):
            if e.get("kategorie"):
                kat[e["kategorie"]][f["gruppe"]] += 1
    z = [[k, v.get("Hersteller", 0), v.get("Bau", 0), sum(v.values())]
         for k, v in sorted(kat.items(), key=lambda x: -sum(x[1].values()))]
    t.append(_tab(["Kategorie", "Hersteller (n=4)", "Bau (n=3)", "gesamt"], z))

    open(ziel, "w").write("\n".join(t) + "\n")
    print("  geschrieben: %s" % os.path.relpath(ziel, HERE))


# ---------------------------------------------------------------------------
# Paarweiser Modellvergleich
# ---------------------------------------------------------------------------

def modellvergleich(referenzmodell, ziel):
    """Vergleicht je Gegenmodell NUR die Chunks, die beide bearbeitet haben.

    Ein Vergleich ueber alle Chunks eines Modells gegen alle Chunks eines anderen
    waere kein paarweiser Vergleich: Die Modelle haetten unterschiedliche Texte
    gesehen, und Unterschiede in der Belegqualitaet koennten von der Schwierigkeit
    des Textes statt vom Modell kommen. Deshalb wird je Gegenmodell die Schnittmenge
    gebildet und beide Modelle werden auf genau dieser Schnittmenge ausgewertet.
    """
    sys.path.insert(0, HERE)
    import extract as E

    ref_dir = os.path.join(HERE, "cache", referenzmodell)
    if not os.path.isdir(ref_dir):
        sys.exit("Kein Referenzcache unter %s" % ref_dir)

    korpora = {}

    def korpus(firma):
        if firma not in korpora:
            meta = E.REPORTS[firma]
            korpora[firma] = E.Korpus(E.seiten_laden(os.path.join(E.PDF_DIR, meta["datei"])))
        return korpora[firma]

    def bewerten(pfad, firma):
        d = json.load(open(pfad))
        k = korpus(firma)
        s = {"n": 0, "woertlich": 0, "teilweise": 0, "nicht": 0}
        for f in FELDER:
            for e in d.get(f, []):
                t = k.suche(e.get("zitat", ""))[1]
                s["n"] += 1
                if t.startswith("exakt"):
                    s["woertlich"] += 1
                elif t == "teilweise":
                    s["teilweise"] += 1
                else:
                    s["nicht"] += 1
        return d.get("_modell", "?"), s

    # Paare sammeln, gruppiert nach dem Modell des Gegenstuecks
    paare = collections.defaultdict(list)
    for firma in sorted(os.listdir(ref_dir)):
        gemischt = os.path.join(HERE, "cache", firma)
        if not os.path.isdir(gemischt):
            continue
        for datei in sorted(os.listdir(os.path.join(ref_dir, firma))):
            partner = os.path.join(gemischt, datei)
            if not (datei.endswith(".json") and os.path.exists(partner)):
                continue
            m_partner, s_partner = bewerten(partner, firma)
            if m_partner == referenzmodell:
                continue          # identisches Modell, kein Vergleich
            _, s_ref = bewerten(os.path.join(ref_dir, firma, datei), firma)
            paare[m_partner].append((s_ref, s_partner))

    def summe(liste, index):
        g = {"n": 0, "woertlich": 0, "teilweise": 0, "nicht": 0}
        for eintrag in liste:
            for k in g:
                g[k] += eintrag[index][k]
        return g

    def quote(g, feld):
        return "%.0f%%" % (100.0 * g[feld] / g["n"]) if g["n"] else "-"

    t = ["# Paarweiser Modellvergleich\n",
         "Verglichen werden Antworten auf **identische Chunks**: gleicher Prompt, gleicher "
         "Quelltext, gleiche Chunkgrenzen. Der Cache-Dateiname enthält den Prompt-Hash, "
         "gleiche Dateinamen bedeuten also identische Eingabe.\n",
         "Je Gegenmodell wird nur die Schnittmenge ausgewertet, also genau die Chunks, die "
         "beide Modelle bearbeitet haben. Ein Vergleich über unterschiedliche Chunks wäre "
         "kein Modellvergleich, sondern könnte die Schwierigkeit des Textes messen.\n",
         "Referenzmodell: **%s**\n" % referenzmodell]

    zeilen = []
    for m, liste in sorted(paare.items(), key=lambda x: -len(x[1])):
        a = summe(liste, 0)
        b = summe(liste, 1)
        zeilen.append([m, len(liste),
                       "%d / %d" % (a["n"], b["n"]),
                       "%s / %s" % (quote(a, "woertlich"), quote(b, "woertlich")),
                       "%s / %s" % (quote(a, "teilweise"), quote(b, "teilweise")),
                       "%s / %s" % (quote(a, "nicht"), quote(b, "nicht"))])
    t.append(_tab(["Gegenmodell", "gemeinsame Chunks", "Elemente Ref/Gegen",
                   "wörtlich belegt", "nur teilweise", "nicht auffindbar"], zeilen))
    t.append("\nJede Zelle nennt zuerst den Wert des Referenzmodells, dann den des "
             "Gegenmodells, gemessen an denselben Textabschnitten.\n")
    open(ziel, "w").write("\n".join(t) + "\n")
    print("  geschrieben: %s" % os.path.relpath(ziel, HERE))


# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description="Auswertung der Extraktionsergebnisse")
    p.add_argument("--input", default=os.path.join(HERE, "data"))
    p.add_argument("--suffix", default="", help="Anhang an die Ausgabedateinamen")
    p.add_argument("--lang", default="de", choices=["de", "en"],
                   help="Sprache der Grafikbeschriftung")
    p.add_argument("--modellvergleich", metavar="MODELL",
                   help="paarweiser Vergleich gegen diesen Referenzcache")
    a = p.parse_args()

    SPRACHE[0] = a.lang

    if a.modellvergleich:
        modellvergleich(a.modellvergleich,
                        os.path.join(HERE, "modellvergleich%s.md" % a.suffix))
        return

    alle = daten_laden(a.input)
    gb = daten_laden(a.input, nur_geschaeftsbericht=True)
    print("%d Unternehmen aus %s" % (len(alle), a.input))

    os.makedirs(os.path.join(HERE, "charts"), exist_ok=True)
    heatmap(gb, os.path.join(HERE, "charts", "heatmap_wachstumsmaerkte%s.png" % a.suffix))
    risikochart(gb, os.path.join(HERE, "charts", "risikokategorien%s.png" % a.suffix))
    befunde_schreiben(alle, gb, os.path.join(HERE, "befunde%s.md" % a.suffix))


if __name__ == "__main__":
    main()
