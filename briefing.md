# Wo sucht die österreichische Industrie 2026 Wachstum, und welche Risiken nennt sie?

Eine LLM-gestützte Auswertung von sieben Geschäftsberichten ATX-notierter Industrieunternehmen.
Lorenz Frauscher, September 2026.

---

## Universum und Methode

Ausgewertet wurden alle ATX-Werte der Branchen **Grundindustrie** sowie **Industriegüter &
Dienstleistungen**, ausgenommen die Sektoren Erdöl & Erdgas, dessen Wachstum dem Rohstoffpreis
folgt, und Transport, einer Dienstleistung ohne eigene Fertigung. Grundlage ist die
Branchen-Einteilung der Wiener Börse in der gültigen Fassung mit 10 Branchen und 41 Sektoren.
Die Regel wurde vor der ersten Extraktion festgeschrieben, die Reihenfolge ist über die
Versionshistorie belegbar.

**Sieben Unternehmen, 2.217 Seiten.** Exportgetriebene Hersteller: voestalpine, Lenzing,
Andritz, PALFINGER. Bau und Baustoffe: Strabag, Porr, Wienerberger.

Eine Python-Pipeline extrahiert vier Feldtypen je Unternehmen und liefert **369 Aussagen**, jede
mit wörtlichem Zitat. **Die zentrale Konstruktion: Das Sprachmodell gibt keine Seitenzahlen aus.**
Es liefert nur Zitate, die Pipeline sucht sie anschließend selbst im Berichtstext und bestimmt
daraus die Seite. Eine Seitenangabe ist damit nicht halluzinierbar, und ein nicht vorhandenes
Zitat fällt bei jeder einzelnen Aussage auf statt nur in einer Stichprobe.

Zusätzlich wurden 134 Aussagen aus drei zufällig gezogenen Unternehmen von Hand gegen das
Original geprüft. Die Ziehung erfolgte mit dokumentiertem Zufallsstartwert, bevor Ergebnisdaten
vorlagen.

---

## Befund 1: Automatische Belegprüfung hat eine messbare Grenze

| | |
|---|---|
| maschinell geprüfte Zitate | 369 |
| davon wörtlich im Bericht auffindbar | **364 (99 %)** |
| **erfundene Zitate** | **0** |
| von Hand geprüfte Aussagen | 134, davon 111 korrekt (83 %) |
| **Fehler, die nur die Handprüfung fand** | **23** |

Das Modell erfindet keine Zitate. In **15,7 Prozent** der geprüften Fälle zitiert es jedoch den
**falschen echten Satz**: Die Aussage stimmt inhaltlich und steht im Bericht, nur nicht in dem
Satz, der als Beleg dient. Beispiel Andritz, Seite 143: Das Zitat berichtet vom Ausweis als zur
Veräußerung gehalten Ende 2024, die Aussage vom Verkauf 2025. Diese Information steht im
Folgesatz.

**Eine automatische Zitatverifikation beweist, dass ein Satz im Dokument steht. Sie beweist nicht,
dass er die daraus abgeleitete Aussage trägt.**

| Feldtyp | geprüft | korrekt | Beleg stützt nicht |
|---|---|---|---|
| Strategische Prioritäten | 28 | 89 % | 2 |
| Capex und M&A | 42 | 83 % | 7 |
| Hauptrisiken | 56 | 80 % | 11 |
| Wachstumsmärkte | 8 | 75 % | 1 |

Nebenbefund zur Vorsicht bei eigenen Messungen: Der erste Durchlauf wies 4,1 Prozent
Halluzinationen aus. Die Handprüfung zeigte, dass alle 15 Fälle Messfehler der eigenen
Zitatsuche waren, verursacht durch Leerzeichen, die die PDF-Extraktion in Wörter setzt. Nach
Korrektur: null. **Eine gemessene Fehlerquote misst zuerst die eigene Pipeline.**

---

## Befund 2: Zwei getrennte Wachstumsgeografien

Die Hersteller nennen Wachstumsmärkte außerhalb Europas. PALFINGER nennt Indien dreimal, dazu
Nordamerika und den Nahen Osten. voestalpine nennt China und Indien, Andritz Nordamerika,
Lateinamerika und China.

Die Bauunternehmen nennen überwiegend den Heimatmarkt und pauschale Kategorien. Porr nennt
Österreich, DACH und Europa, Strabag DACH, Europa und einmal den Nahen Osten. Weder Porr noch
Strabag noch Wienerberger nennt Indien oder
China ein einziges Mal.

**Einschränkung.** Über alle sieben Unternehmen entfallen nur 27 belegte Regionsnennungen,
Lenzing nennt keine. Das Extraktionsschema verlangt die Zuordnung zu einer festen Regionenliste,
segmentbezogene Wachstumsaussagen fallen durch das Raster. Der Befund beschreibt, wo Wachstum
**geografisch benannt** wird, nicht wo es gesucht wird.

<!--chart:1-->

---

## Befund 3: Technologierisiken nennen nur die Hersteller

| Kategorie | Hersteller (n=4) | Bau (n=3) | gesamt |
|---|---|---|---|
| Finanzierung | 20 | 8 | 28 |
| Markt | 17 | 10 | 27 |
| Regulierung | 11 | 5 | 16 |
| Lieferkette | 7 | 5 | 12 |
| **Technologie** | **9** | **0** | **9** |

*Nennungen im Geschäftsbericht, ohne Nachhaltigkeitsberichterstattung.*

Technologie ist die einzige Zeile mit einem qualitativen Sprung. **Alle vier Hersteller bespielen
die Kategorie, keines der drei Bauunternehmen.** Drei Hersteller nennen Cyberangriffe und
IT-Störungen, dazu kommen Produktentwicklung, Portfoliowettbewerb und Anlagenalterung.

Zwei Einschränkungen gehören dazu. Porr und Wienerberger nennen je ein Technologierisiko in der
Nachhaltigkeitsberichterstattung, bei Wienerberger Cybersicherheit. Die Kategorie fehlt ihnen
also im Geschäftsteil, nicht im ganzen Bericht. Und die geschlossene Kategorienliste erzwingt
eine Zuordnung: Drei der neun Herstellernennungen stammen von voestalpine und beschreiben eher
Betriebsrisiken. Belastbarer als die Häufigkeit ist die Verteilung über Unternehmen, vier von
vier gegen null von drei.

<!--chart:2-->

---

## Limitationen

**Stichprobengröße.** Sieben Unternehmen, vier zu drei aufgeteilt. Die Gruppentabellen
beschreiben, sie beweisen nicht.

**Ein Drittel stammt aus der Pflichtberichterstattung.** 124 der 369 Elemente entstammen den
ESRS- und Taxonomieteilen. Sie sind gekennzeichnet, nicht entfernt. Bei Wienerberger sind es
53 Prozent, bei Andritz null, weil dort der Nachhaltigkeitsteil separat erscheint. Die
Handprüfung zeigt für ESRS-Abschnitte 78 gegen 85 Prozent Korrektheit.

**Uneinheitliches Berichtsjahr.** voestalpine schließt zum 31.03.2026 ab, die übrigen sechs zum
31.12.2025.

**Versionsabhängigkeit.** Die PDF-Textextraktion liefert je nach Bibliotheksversion leicht
abweichende Ergebnisse. Die Versionen sind in `requirements.txt` festgenagelt.

**Offenlegung.** PALFINGER war von Februar bis Juni 2025 Arbeitgeber des Autors. PALFINGER wurde
nicht in die Verifikationsstichprobe gezogen.

---

## Was daraus folgt

Eine Architektur, die das Modell zum Zitieren zwingt und die Belegstelle selbst berechnet, macht
Erfindung maschinell nachweisbar und hat sie hier auf null gedrückt. Sie ersetzt die menschliche
Prüfung nicht, sie verschiebt deren Aufgabe von der Frage "existiert dieser Satz" zu "trägt
dieser Satz diese Aussage". Das ist die Frage, die 15,7 Prozent der Fälle entscheidet.

Wer eine solche Pipeline ohne Handprüfung produktiv einsetzt, bekommt Ergebnisse, die jeder
automatischen Kontrolle standhalten und trotzdem in jedem sechsten Fall falsch belegt sind.

*Code, Rohdaten, Verifikationsprotokoll und Entscheidungslog: github.com/lorenzrauscher1-create/atx-industrials.
Die Geschäftsberichte selbst sind nicht Teil des Repositories.*
