# Aggregierte Befunde

Erzeugt von `aggregate.py`. Alle Zahlen beziehen sich auf Elemente mit auffindbarem Beleg im Quelldokument.


## 1. Umfang je Unternehmen

| Unternehmen | Gruppe | gesamt | Strategie | Wachstum | Risiken | Capex/M&A | davon ESRS |
|---|---|---|---|---|---|---|---|
| Andritz AG | Hersteller | 33 | 4 | 3 | 13 | 13 | 0 (0%) |
| Lenzing AG | Hersteller | 75 | 17 | 0 | 39 | 19 | 33 (44%) |
| PALFINGER AG | Hersteller | 58 | 13 | 11 | 18 | 16 | 10 (17%) |
| Porr AG | Bau | 64 | 18 | 5 | 27 | 14 | 25 (39%) |
| Strabag SE | Bau | 38 | 8 | 6 | 12 | 12 | 11 (29%) |
| voestalpine AG | Hersteller | 65 | 18 | 4 | 27 | 16 | 26 (40%) |
| Wienerberger AG | Bau | 36 | 6 | 1 | 16 | 13 | 19 (53%) |


## 2. Belegqualität je Unternehmen

| Unternehmen | Elemente | wörtlich belegt | nur teilweise | nicht auffindbar | Modell(e) |
|---|---|---|---|---|---|
| Andritz AG | 33 | 97% | 1 | 0 | gemini-3.8-flash |
| Lenzing AG | 75 | 96% | 3 | 0 | gemini-3.8-flash |
| PALFINGER AG | 58 | 100% | 0 | 0 | gemini-3.8-flash |
| Porr AG | 64 | 100% | 0 | 0 | gemini-3.8-flash |
| Strabag SE | 38 | 97% | 1 | 0 | gemini-3.8-flash |
| voestalpine AG | 65 | 100% | 0 | 0 | gemini-3.8-flash |
| Wienerberger AG | 36 | 100% | 0 | 0 | gemini-3.8-flash |


## 3. Wachstumsregionen, nur Geschäftsbericht

| Region | Nennungen | Unternehmen |
|---|---|---|
| Europa uebrig | 10 | 4 |
| Nordamerika | 4 | 3 |
| Indien | 4 | 2 |
| Lateinamerika | 2 | 2 |
| China | 2 | 2 |
| Naher Osten | 2 | 2 |
| DACH | 2 | 2 |
| Oesterreich | 1 | 1 |


## 4. Risikokategorien nach Gruppe

**Achtung bei der Lesart.** Bei sieben Unternehmen in einer Aufteilung von vier zu drei sind Häufigkeitsvergleiche zwischen den Gruppen statistisch nicht belastbar. Die Tabelle beschreibt, sie beweist nicht.

| Kategorie | Hersteller (n=4) | Bau (n=3) | gesamt |
|---|---|---|---|
| Finanzierung | 20 | 8 | 28 |
| Markt | 17 | 10 | 27 |
| Regulierung | 11 | 5 | 16 |
| Lieferkette | 7 | 5 | 12 |
| Technologie | 9 | 0 | 9 |
