**Strategic priorities of Austrian industrials**
LLM-assisted extraction from seven annual reports of ATX-listed industrial companies, 2,217 pages. The model returns verbatim quotations only, the pipeline locates them in the source text, so citations cannot be fabricated undetected. 369 statements extracted, none fabricated. Of 134 hand-checked, 15.7% cite a real sentence that does not support the claim. English write-up: briefing_en.md.
# Strategische Prioritäten österreichischer Industrieunternehmen

LLM-gestützte Extraktion aus sieben Geschäftsberichten ATX-notierter Industrieunternehmen,
mit maschineller Zitatverifikation und einer von Hand gemessenen Fehlerquote.

Lorenz Frauscher, WU Wien, September 2026.

**Ergebnis in einem Satz:** 369 extrahierte Aussagen, null erfundene Zitate, aber 15,7 Prozent
der von Hand geprüften Aussagen stützen sich auf den falschen echten Satz. Eine automatische
Zitatprüfung beweist, dass ein Satz im Dokument steht, nicht dass er die Aussage trägt.

Das vollständige Ergebnis steht in [`briefing.pdf`](briefing.pdf), englisch in
[`briefing_en.pdf`](briefing_en.pdf).

---

## Was hier drin ist

| Datei | Inhalt |
|---|---|
| `extract.py` | PDF zu Text, Kapitelauswahl, Chunking, Modellaufruf, Zitatverortung |
| `aggregate.py` | Aggregation, zwei Charts, paarweiser Modellvergleich |
| `pruefliste.py` | erzeugt die Arbeitsliste für die Handprüfung |
| `auswertung_verifikation.py` | wertet die Handprüfung aus |
| `build_briefing_pdf.py` | erzeugt die Briefing-PDFs aus Markdown |
| `data/gemini-3.8-flash/*.json` | Ergebnisdaten je Unternehmen |
| `cache/` | Rohantworten des Modells, siehe unten |
| `results_gemini-3.8-flash.csv` | alle 369 Aussagen als Tabelle |
| `pruefliste.csv` und `.xlsx` | die 134 von Hand geprüften Elemente mit Urteil |
| `verification.md` | Verifikationsprotokoll, Stichprobenziehung, Auslegungsregeln, Ergebnisse |
| `DECISIONS.md` | Entscheidungslog mit Begründung jeder Designentscheidung |
| `charts/` | die zwei Grafiken als PNG, deutsch und englisch |

**Nicht enthalten: die Geschäftsberichte selbst.** Das ist fremdes Material. Die Bezugsquellen
stehen unten.

---

## Die zentrale Konstruktion

Das Sprachmodell gibt **keine Seitenzahlen** aus. Es liefert ausschließlich wörtliche Zitate.
`extract.py` sucht jedes Zitat anschließend selbst im Berichtstext und bestimmt daraus die Seite.

Zwei Folgen:

1. Eine Seitenangabe kann nicht halluziniert sein, weil sie kein Modelloutput ist.
2. Ein Zitat, das im Bericht nicht vorkommt, fällt bei **jeder einzelnen** Aussage auf, nicht nur
   in einer Stichprobe.

Der Vergleich läuft dreistufig: wörtlich, dann ohne Satzzeichen und Trennstriche, dann ohne
Leerzeichen. Die dritte Stufe entstand, nachdem die Handprüfung ein als erfunden gemeldetes Zitat
im Bericht nachgewiesen hatte. Die PDF-Extraktion hatte dort ein Leerzeichen mitten in ein Wort
gesetzt.

---

## Reproduktion

### Voraussetzungen

Python 3.9 oder neuer.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Die Versionen sind festgenagelt. Die PDF-Textextraktion liefert je nach `pypdf`-Version leicht
abweichende Ergebnisse, was Chunkgrenzen und damit Cache-Schlüssel verändert.

### Ohne API-Schlüssel: Auswertung nachrechnen

Alle Modellantworten liegen unter `cache/gemini-3.8-flash/`. Damit lässt sich die komplette
Auswertung ohne eigenen Zugang reproduzieren.

```bash
# Geschaeftsberichte eine Ebene ueber diesem Ordner ablegen, Namen siehe unten
python3 extract.py --all --model gemini-3.8-flash --strict-model
python3 aggregate.py --input data/gemini-3.8-flash --suffix _38flash
python3 auswertung_verifikation.py
```

Der erste Befehl sendet keine Anfrage, solange jeder Chunk im Cache liegt.

### Mit API-Schlüssel: Extraktion neu fahren

```bash
export GEMINI_API_KEY="..."        # niemals in eine Datei schreiben
rm -r cache/gemini-3.8-flash       # erzwingt neue Anfragen
python3 extract.py --all --model gemini-3.8-flash --strict-model --max-cost 2.00
```

Rund 60 Anfragen, geschätzt 1,05 USD. `--max-cost` stoppt den Lauf bei der angegebenen Summe.

Nützliche Optionen:

| Option | Wirkung |
|---|---|
| `--dry-run` | zeigt Seitenauswahl und Chunking ohne Modellaufruf |
| `--probe` | testet, welches Modell gerade antwortet, sortiert nach Latenz |
| `--strict-model` | kein automatischer Modellwechsel, nötig für vergleichbare Datensätze |
| `--max-requests N` | Obergrenze gesendeter Anfragen, Fehlversuche eingerechnet |

### Benötigte Dateien

Die Geschäftsberichte gehören **eine Ebene über** diesen Ordner, unter genau diesen Namen:

```
andritz_2025.pdf          Jahresfinanzbericht 2025 (nicht der Magazinteil)
lenzing_2025.pdf          Geschäfts- und Nachhaltigkeitsbericht 2025
palfinger_2025.pdf        Geschäftsbericht 2025
porr_2025.pdf             Geschäfts- und Nachhaltigkeitsbericht 2025
strabag_2025.pdf          Geschäfts- und Nachhaltigkeitsbericht 2025
voestalpine_2025_26.pdf   Geschäftsbericht 2025/26, deutsche Fassung
wienerberger_2025.pdf     Geschäftsbericht 2025
```

Jeweils die deutsche Fassung, weil Seitenzahlen zwischen Sprachfassungen abweichen und der Beleg
sonst nicht reproduzierbar ist. Alle sind über die Investor-Relations-Seiten der Unternehmen
frei verfügbar.

---

## Methodische Eckpunkte

**Universum.** Alle ATX-Werte der Branchen Grundindustrie sowie Industriegüter & Dienstleistungen,
ausgenommen die Sektoren Erdöl & Erdgas und Transport. Die Regel wurde vor der ersten Extraktion
festgeschrieben, die Reihenfolge ist über die Commit-Historie belegbar.

**Verifikationsstichprobe.** Drei von sieben Unternehmen, gezogen am 05.09.2026 mit dokumentiertem
Zufallsstartwert, bevor Ergebnisdaten vorlagen. 134 Elemente von Hand geprüft.

**Kennzeichnung statt Ausschluss.** Aussagen aus der Nachhaltigkeitsberichterstattung nach ESRS
werden gekennzeichnet, nicht entfernt. Der Prompt blieb unverändert, die Trennung erfolgt erst in
der Aggregation.

**Ein Modell für alle sieben.** Ein früherer Lauf verteilte sich über vier Modellversionen, deren
Zitattreue zwischen 64 und 88 Prozent schwankt. Der gemischte Datensatz liegt unter
`data_gemischt_*` und dient dem paarweisen Modellvergleich in `modellvergleich.md`.

Warum welche Entscheidung so fiel, steht vollständig in [`DECISIONS.md`](DECISIONS.md),
einschließlich der Fehler, die dabei gemacht und korrigiert wurden.

---

## Entstehung

Der Code wurde KI-gestützt entwickelt. Fragestellung, Universum, Auswahlregel, jede
Methodikentscheidung und die vollständige Handprüfung der 134 Elemente stammen vom Autor.
`DECISIONS.md` dokumentiert jede Entscheidung mit Begründung und Messwerten.

**Offenlegung.** PALFINGER war von Februar bis Juni 2025 Arbeitgeber des Autors im Bereich
Corporate Development. PALFINGER wurde nicht in die Verifikationsstichprobe gezogen.
