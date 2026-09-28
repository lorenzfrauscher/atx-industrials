#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_briefing_pdf.py -- erzeugt briefing.pdf aus briefing.md

Deckt genau die Markdown-Teilmenge ab, die im Briefing vorkommt: Ueberschriften
der Ebenen 1 bis 2, Absaetze, Tabellen, Trennlinien, fette und kursive Auszeichnung.
Bewusst kein universeller Konverter. Ein Werkzeug, das nur das kann, was gebraucht
wird, ist leichter zu pruefen als eines, das alles kann.

Aufruf:
  python3 build_briefing_pdf.py briefing.md briefing.pdf chart1.png chart2.png
"""

import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Frame, HRFlowable, Image,
                                KeepTogether, PageTemplate, Paragraph, Spacer,
                                Table, TableStyle)

TEXT = colors.HexColor("#0b0b0b")
SEK = colors.HexColor("#52514e")
LINIE = colors.HexColor("#d8d7d3")
KOPF_FUELL = colors.HexColor("#f0efec")
AKZENT = colors.HexColor("#2a78d6")

S_TITEL = ParagraphStyle("titel", fontName="Helvetica-Bold", fontSize=15.5,
                         leading=19.5, textColor=TEXT, spaceAfter=5)
S_UNTER = ParagraphStyle("unter", fontName="Helvetica", fontSize=8.8, leading=12.5,
                         textColor=SEK, spaceAfter=11)
S_H2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11, leading=14,
                      textColor=TEXT, spaceBefore=7.5, spaceAfter=3.5)
S_TEXT = ParagraphStyle("text", fontName="Helvetica", fontSize=8.4, leading=11.2,
                        textColor=TEXT, alignment=TA_LEFT, spaceAfter=4.4)
S_FUSS = ParagraphStyle("fuss", fontName="Helvetica-Oblique", fontSize=7.6,
                        leading=10.5, textColor=SEK, spaceBefore=7)
S_ZELLE = ParagraphStyle("zelle", fontName="Helvetica", fontSize=7.7, leading=10.0,
                         textColor=TEXT)
S_ZELLE_K = ParagraphStyle("zellek", fontName="Helvetica-Bold", fontSize=8.0,
                           leading=10.6, textColor=TEXT)


def inline(t):
    """Fett, kursiv und Code in ReportLab-Auszeichnung uebersetzen."""
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", t)
    t = re.sub(r"`(.+?)`", r'<font face="Courier" size="7.8">\1</font>', t)
    return t


def tabelle(zeilen, breite):
    kopf = [c.strip() for c in zeilen[0].strip("|").split("|")]
    daten = []
    for z in zeilen[2:]:
        daten.append([c.strip() for c in z.strip("|").split("|")])

    inhalt = [[Paragraph(inline(c), S_ZELLE_K) for c in kopf]]
    for r in daten:
        inhalt.append([Paragraph(inline(c), S_ZELLE) for c in r])

    n = len(kopf)
    # Erste Spalte breiter, die uebrigen gleich. Zahlenspalten brauchen wenig Platz.
    erste = breite * (0.40 if n <= 3 else 0.30)
    rest = (breite - erste) / max(1, n - 1)
    breiten = [erste] + [rest] * (n - 1)

    leer = not any(c.strip() for c in kopf)
    if leer:
        # Schluessel-Wert-Tabellen haben im Markdown eine leere Kopfzeile. Als
        # graues Band formatiert saehe sie aus wie ein Fehler.
        inhalt = inhalt[1:]

    t = Table(inhalt, colWidths=breiten, repeatRows=0 if leer else 1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.white if leer else KOPF_FUELL),
        ("LINEBELOW", (0, 0), (-1, 0), 0.25 if leer else 0.6, LINIE),
        ("LINEBELOW", (0, 1), (-1, -2), 0.25, LINIE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 2.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def bauen(md_pfad, pdf_pfad, charts):
    rohzeilen = open(md_pfad, encoding="utf-8").read().split("\n")

    seite_b, seite_h = A4
    rand_x, rand_o, rand_u = 17 * mm, 15 * mm, 14 * mm
    nutzbreite = seite_b - 2 * rand_x

    def fuss(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(SEK)
        canvas.drawRightString(seite_b - rand_x, 8 * mm, str(doc.page))
        canvas.setStrokeColor(LINIE)
        canvas.setLineWidth(0.4)
        canvas.line(rand_x, 11 * mm, seite_b - rand_x, 11 * mm)
        canvas.restoreState()

    doc = BaseDocTemplate(pdf_pfad, pagesize=A4,
                          leftMargin=rand_x, rightMargin=rand_x,
                          topMargin=rand_o, bottomMargin=rand_u,
                          title=rohzeilen[0].lstrip("# ").strip(),
                          author="Lorenz Frauscher")
    rahmen = Frame(rand_x, rand_u, nutzbreite, seite_h - rand_o - rand_u, id="normal",
                   leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="alle", frames=[rahmen], onPage=fuss)])

    story = []
    i = 0
    absatz = []
    chart_index = [0]

    def absatz_leeren():
        if absatz:
            story.append(Paragraph(inline(" ".join(absatz)), S_TEXT))
            absatz[:] = []

    while i < len(rohzeilen):
        z = rohzeilen[i].rstrip()

        if z.startswith("# "):
            absatz_leeren()
            story.append(Paragraph(inline(z[2:]), S_TITEL))
        elif z.startswith("## "):
            absatz_leeren()
            story.append(Paragraph(inline(z[3:]), S_H2))
        elif z.startswith("---"):
            absatz_leeren()
            story.append(Spacer(1, 3))
            story.append(HRFlowable(width="100%", thickness=0.5, color=LINIE))
            story.append(Spacer(1, 2))
        elif z.startswith("<!--chart:"):
            absatz_leeren()
            nr = int(re.search(r"\d+", z).group()) - 1
            if 0 <= nr < len(charts):
                from reportlab.lib.utils import ImageReader
                pfad = charts[nr][0]
                iw, ih = ImageReader(pfad).getSize()
                b = nutzbreite
                h = b * ih / float(iw)
                if h > 42 * mm:
                    h = 42 * mm
                    b = h * iw / float(ih)
                story.append(Spacer(1, 3))
                story.append(Image(pfad, width=b, height=h, hAlign="LEFT"))
                story.append(Spacer(1, 5))
        elif z.startswith("|"):
            absatz_leeren()
            block = []
            while i < len(rohzeilen) and rohzeilen[i].startswith("|"):
                block.append(rohzeilen[i])
                i += 1
            story.append(Spacer(1, 2))
            story.append(tabelle(block, nutzbreite))
            story.append(Spacer(1, 6))
            # Nach der ersten Tabelle eines Befunds den passenden Chart setzen
            if chart_index[0] < len(charts):
                pass
            continue
        elif z.startswith("*") and z.endswith("*") and len(z) > 2 and not z.startswith("**"):
            absatz_leeren()
            story.append(Paragraph(inline(z.strip("*")), S_FUSS))
        elif not z.strip():
            absatz_leeren()
        else:
            absatz.append(z.strip())
        i += 1
    absatz_leeren()

    doc.build(story)
    print("geschrieben: %s" % pdf_pfad)


if __name__ == "__main__":
    md, pdf = sys.argv[1], sys.argv[2]
    ch = []
    for arg in sys.argv[3:]:
        pfad, _, titel = arg.partition("::")
        ch.append((pfad, titel or ""))
    bauen(md, pdf, ch)
