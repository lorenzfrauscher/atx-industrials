# Entscheidungslog und Pipeline-Architektur

**Zweck.** Vorbereitung auf Fachinterviews. Jede Entscheidung dieses Projekts mit
Auslöser, Begründung und den Zahlen, die dahinterstehen. Wer das Dokument liest, kann
die Pipeline erklären, ohne den Code zu öffnen.

Stand: 04.09.2026. Ergänzt nach jedem Arbeitsschritt.

---

## 1. Der Satz, um den es geht

> Der Anbieter lieferte reproduzierbar HTTP 503 für einzelne Chunks. Also habe ich die
> Anfragen verkleinert, das Denkbudget abgeschaltet und eine dokumentierte Modellkette
> eingebaut.

Warum dieser Satz im Interview mehr wert ist als eine glatte Ergebniszahl: Er zeigt, dass
das Projekt gegen eine echte API gelaufen ist und nicht gegen ein Tutorial. Betriebsverhalten
unter Last, Ratenlimits und Anbieterausfälle sind die Themen, an denen produktive
KI-Projekte scheitern, nicht die Promptformulierung. Wer das erlebt und gelöst hat, kann
darüber sprechen. Wer es nicht erlebt hat, merkt man in zwei Rückfragen.

---

## 2. Entscheidungen in der Reihenfolge, in der sie fielen

### 2.1 Systematikstand der Wiener Börse geklärt, statt eine Fassung zu raten

**Auslöser.** Zwei Seiten der Wiener Börse nennen unterschiedliche Strukturen. Das
Börsenlexikon spricht von 8 Branchen und 36 Subbranchen, der Download-Bereich von
10 Branchen und 41 Sektoren.

**Entscheidung.** Die 10/41-Fassung gilt.

**Beleg.** Die ATX-Segmentierungsseite verwendet die Sektorbezeichnungen
"Immobilienmanagement & -entwicklung" und "Hardware & Ausrüstung". Beide existieren
ausschließlich in der 10/41-Fassung. Die Summe der Sektoren bestätigt sie zusätzlich
rechnerisch: 6+8+5+5+4+3+3+2+3+2 = 41.

**Interviewwert.** Widersprüchliche Quellen einer Institution auflösen, statt die
bequemere zu nehmen.

### 2.2 Auswahlregel vor Datensicht festgeschrieben

**Entscheidung.** Alle ATX-Werte der Branchen Grundindustrie sowie Industriegüter &
Dienstleistungen, ausgenommen die Sektoren Erdöl & Erdgas und Transport. Ergebnis:
sieben Unternehmen.

**Die unbequeme Konsequenz.** Schoeller-Bleckmann ist inhaltlich ein Maschinenbauer, die
Wiener Börse führt das Unternehmen aber unter Erdöl & Erdgas. Der Ausschluss greift. Die
Regel wurde nicht angepasst, obwohl das Ergebnis diskutabel ist.

**Interviewwert.** Genau hier trennt sich Methodik von Cherry-Picking. Die Reihenfolge
Regel zuerst, Daten danach ist im Repository über die Dateihistorie belegbar.

### 2.3 Datenbasis: Konzernlagebericht statt Magazinteil

**Auslöser.** Der zuerst geladene Andritz-Geschäftsbericht 2025 hatte 162 Seiten Umfang
im Magazinformat.

**Prüfung.** Strukturcheck über alle sieben Dateien. Im Andritz-Dokument kam
"Konzernlagebericht" null Mal vor und "Konzernabschluss" null Mal. Zum Vergleich Strabag
456 und 121, Wienerberger 251 und 311.

**Entscheidung.** Pro Unternehmen genau das Dokument, das den Konzernlagebericht samt
Risikobericht enthält. Bei getrennter Publikation gilt der Jahresfinanzbericht. Andritz
wurde ausgetauscht.

**Interviewwert.** Datenqualität vor Extraktion prüfen, nicht danach.

### 2.4 Sprachfassung und Berichtsjahr fixiert

Alle sieben Berichte in deutscher Fassung. Grund: Seitenzahlen weichen zwischen
Sprachfassungen ab, ohne Festlegung wäre die Belegangabe nicht reproduzierbar. Die
zunächst geladene englische voestalpine-Fassung wurde ersetzt.

voestalpine hat ein abweichendes Geschäftsjahr vom 1. April bis 31. März. Verwendet wird
der Geschäftsbericht 2025/26 mit Stichtag 31.03.2026, die übrigen sechs mit Stichtag
31.12.2025. Das Sample ist damit zeitlich uneinheitlich. Diese Abweichung steht in den
Limitationen und wird nicht versteckt.

### 2.5 Textebenen-Prüfung vor jedem Modellaufruf

Alle 2.217 Seiten haben eine maschinenlesbare Textschicht, kein OCR nötig. Seiten unter
200 Zeichen sind Trenn- und Bildseiten. Der Check kostete zwei Minuten und hätte im
Fehlerfall eine Stunde gespart.

---

## 3. Die zentrale Architekturentscheidung

### 3.1 Das Modell gibt keine Seitenzahlen an

**Ausgangslage im ursprünglichen Schema.** Das Modell sollte `beleg_seite` und `zitat`
gemeinsam liefern. Beide Felder können unabhängig voneinander falsch sein. In der
Verifikation lässt sich dann nicht mehr unterscheiden, ob das Modell halluziniert hat oder
nur die Seite verwechselt.

**Entscheidung.** Das Modell liefert ausschließlich das wörtliche Zitat. Die Pipeline sucht
das Zitat anschließend im normalisierten Berichtstext und berechnet die Seite selbst.

**Drei Konsequenzen:**

1. Seitenangaben sind nicht mehr halluzinierbar. Sie sind kein Modelloutput, sondern ein
   Suchergebnis.
2. Der Versatz zwischen gedruckter Seitenzahl und PDF-Index entfällt als Fehlerquelle.
   Gemessen: Andritz minus 1, Porr minus 2, bei Lenzing gar nicht ermittelbar, weil dort
   Seitenzahlen nicht als eigene Textzeile stehen.
3. Erfundene Zitate werden für 100 Prozent der Extraktionen automatisch erkannt, nicht nur
   in der Stichprobe von drei Unternehmen. Ein Zitat, das im Quelltext nicht vorkommt, ist
   per Definition erfunden.

**Validierung.** 120 echte Sätze aus bekannten Seiten gezogen und zurückgesucht.
110 exakt und auf der richtigen Seite, 10 als mehrdeutig markiert, null stillschweigend
falsche Seitenzahlen. Ein erfundenes Kontrollzitat wurde abgelehnt, eine Paraphrase mit
echtem Satzanfang korrekt als "teilweise" eingestuft.

**Interviewwert.** Das ist die stärkste Aussage des Projekts. Statt Halluzinationen per
Stichprobe zu schätzen, macht die Architektur eine ganze Fehlerklasse maschinell
nachweisbar. Die Handprüfung in Schritt 3 misst danach nur noch, was eine Maschine nicht
sehen kann: inhaltliche Verzerrung und falsche Kategorienzuordnung.

### 3.2 Mehrdeutige Fundstellen werden ausgewiesen, nicht stillschweigend aufgelöst

**Auslöser.** Im ersten Anlauf nahm die Zitatsuche bei mehrfach vorkommenden Textbausteinen
einfach die erste Fundstelle. Ergebnis: 7 von 120 Testzitaten landeten auf einer falschen
Seite.

**Analyse.** Alle sieben Fälle waren Zitate, die zwei- bis viermal wortgleich im Bericht
stehen. Kopfzeilen, Textbausteine, wiederholte Absätze.

**Entscheidung.** Treffertyp `exakt_mehrdeutig` plus Liste aller Fundstellen.

**Interviewwert.** Der Unterschied zwischen einem Fehler und einer dokumentierten
Einschränkung liegt genau hier.

---

## 4. Vorverarbeitung: der Fehler, der beinahe dem Modell angelastet worden wäre

**Befund.** Der PALFINGER-Bericht liefert 27.717 Zeichen in der Private Use Area, also
kaputt kodiert. Die übrigen sechs Berichte sind sauber.

**Erster Reparaturversuch.** ASCII-Versatz von 0xF000 auf den gesamten Bereich. Für Ziffern
richtig, für Symbole falsch.

**Was dabei kaputtging.**

| Zeichen | Versatz ergab | Richtig | Betroffene Wörter |
|---|---|---|---|
| U+F0DF, 451x | ß | fl | Cashflow, Konflikt, Inflationsrate |
| U+F0DE, 1.017x | Þ | fi | Nettofinanzverschuldung, Asien-Pazifik |
| U+F0A7, 432x | § | Aufzählungspunkt | Listen im IR-Teil |
| U+F0E4 / U+F0E6, je 4x | ä / æ | Pfeil hoch / runter | Chancen-Risiko-Tabelle |

**Die Folge.** Ein korrektes Zitat auf Seite 251 wurde als erfunden markiert, weil im
verarbeiteten Text "Einßuss" statt "Einfluss" stand. Die Fehlerquote hätte 1 von 34
Halluzinationen ausgewiesen. Tatsächlich waren es 0 von 34.

**Endgültige Lösung.** Zwei Bereiche mit unterschiedlicher Logik. U+F020 bis U+F07E über
den ASCII-Versatz, darüber eine geprüfte Einzelzuordnung. Nicht zuordenbare Zeichen werden
entfernt und gezählt statt still durchgereicht.

**Geprüfte Alternative.** fontTools installiert und getestet. Ändert die Extraktion nicht,
identische 27.717 kaputte Zeichen. Die pypdf-Warnung dazu ist folgenlos.

**Interviewwert, und zwar der wichtigste des ganzen Projekts.** Eine gemessene Fehlerquote
misst zuerst die eigene Pipeline und erst danach das Modell. Wer das nicht trennt,
schreibt Vorverarbeitungsfehler dem Sprachmodell zu und zieht falsche Schlüsse über die
Zuverlässigkeit von KI.

---

## 5. Kapitelauswahl und Abschnittskennzeichnung

### 5.1 Auswahl relevanter Seiten

Nicht der ganze Bericht geht ins Modell. Je Feldtyp werden Seiten nach Schlagwortdichte
gepunktet, die dichtesten ausgewählt, Nachbarseiten ergänzt. Seiten mit über 30 Prozent
Ziffernanteil fallen als reine Zahlentabellen heraus.

Ergebnis: 803 von 2.217 Seiten, also rund 35 Prozent. Grund ist nicht die Kostenersparnis,
sondern die Präzision. Je mehr irrelevanten Kontext das Modell sieht, desto eher greift es
das falsche Zitat.

### 5.2 ESRS-Kennzeichnung statt ESRS-Ausschluss

**Auslöser.** Rund ein Viertel der PALFINGER-Treffer stammte nicht aus dem Geschäftsteil,
sondern aus der Nachhaltigkeitsberichterstattung. Vier von zehn Capex-Signalen waren reine
EU-Taxonomie-Offenlegungen wie "Konforme Investitionen betrugen 1.227 TEUR". Das ist keine
Investitionsaussage, das ist eine Meldepflicht.

**Verworfene Lösung.** Den Prompt anpassen und ESRS-Inhalte ausschließen. Das wäre eine
Änderung der Extraktionsvorschrift nach Sichtung der Ergebnisse und damit angreifbar,
selbst wenn sie sachlich richtig wäre.

**Gewählte Lösung.** Der Prompt bleibt unverändert. Jedes Element bekommt zusätzlich das
Feld `quelle_abschnitt` mit den Werten Geschäftsbericht oder
Nachhaltigkeitsberichterstattung. Die Zuordnung trifft ein deterministischer
Seitenklassifikator, nicht das Modell. Getrennt wird erst in der Aggregation, per Schalter,
und im Briefing werden beide Zahlen gezeigt.

**Kalibrierung.** 21 PALFINGER-Seiten von Hand zugeordnet, davon 14 Geschäftsteil und
7 Nachhaltigkeitsteil. Getestet wurden Markerschwellen 2 und 3 gegen Lückenlängen von 0
bis 15.

| Parameter | Geschäftsseiten korrekt | Nachhaltigkeitsseiten korrekt |
|---|---|---|
| Schwelle 2, Lücke 10 | 14 von 14 | 6 von 7 |
| Schwelle 2, Lücke 15 | 10 von 14 | 6 von 7 |
| Schwelle 3, Lücke 3 | 14 von 14 | 1 von 7 |

Gewählt: Schwelle 2, Lücke 10.

**Fehlerrichtung bewusst gewählt.** Der Klassifikator ordnet im Zweifel dem
Geschäftsbericht zu, nie umgekehrt. Der ausgewiesene ESRS-Anteil ist damit eine
Untergrenze. Die andere Richtung wäre gefährlicher, weil sie echte Geschäftsaussagen
unsichtbar machen würde.

**Kontrollergebnis.** 25 bis 34 Prozent der Seiten je Bericht, beim Andritz-Finanzbericht
0 Prozent. Letzteres ist der beste Beleg, dass die Regel greift, denn Andritz publiziert
seinen Nachhaltigkeitsteil in einem anderen Dokument.

**Interviewwert.** Aus einem Störfaktor wird ein Befund. Die Aussage "ein Viertel dessen,
was formal wie eine strategische Priorität aussieht, stammt aus der ESRS-Pflichtberichterstattung"
ist analytisch wertvoller als eine bereinigte Heatmap.

---

## 6. Betriebsverhalten der API

### 6.1 Modellversion festgenagelt

Statt `gemini-flash-latest` eine feste Version. Ein Alias zeigt in drei Monaten auf ein
anderes Modell und liefert bei Dritten andere Ergebnisse als die im Briefing. Ein Projekt,
dessen Verkaufsargument Reproduzierbarkeit ist, darf sich nicht auf einen wandernden Alias
stützen.

### 6.2 429 und 503 sind nicht dasselbe

Der erste Wiederholungsmechanismus behandelte beide gleich und wartete zehn Minuten ins
Leere.

- **429** ist das eigene Kontingent. Warten hilft.
- **503** ist Überlastung beim Anbieter. Warten hilft selten, ein anderes Modell fast immer.

Getrennte Behandlung eingebaut.

### 6.3 Modellauswahl nach Antwortzeit, nicht nach Versionsnummer

Der `--probe`-Befehl schickt an sechs Modelle eine Minimalanfrage. Messwerte:

| Modell | Antwortzeit für 16 Tokens |
|---|---|
| gemini-3.5-flash | 0,6s |
| gemini-3-flash-preview | 0,6s |
| gemini-3.8-flash | 1,8s |
| gemini-3.6-flash | 21,6s |
| gemini-3.7-flash | 39,8s |

Vierzig Sekunden für sechzehn Tokens bedeutet interne Warteschlangen. Genau dort kippt eine
Anfrage mit 25.000 Tokens in einen 503. Die Empfehlung sortiert deshalb nach Latenz, nicht
nach Neuheit.

### 6.4 Drei Maßnahmen gegen den wiederkehrenden 503

**Befund.** Chunk 2 scheiterte zweimal reproduzierbar, obwohl er mit rund 89.000 Zeichen
nicht größer war als die anderen drei.

1. **Chunkgröße halbiert**, von 90.000 auf 45.000 Zeichen. Aus vier Anfragen werden acht
   kleinere.
2. **Denkbudget auf null.** Bei schematisierter Extraktion bringt internes Nachdenken wenig,
   erhöht aber die Rechenzeit je Anfrage. Akzeptiert das Modell den Parameter nicht, läuft
   der Aufruf automatisch ohne.
3. **Dokumentierte Modellkette.** Antwortet ein Modell nach drei Versuchen nicht, wechselt
   die Pipeline selbstständig zum nächsten. Welches Modell geantwortet hat, steht pro Chunk
   im Cache und in der Ergebnisdatei unter `tatsaechlich_benutzte_modelle`. Ein gemischter
   Lauf ist damit ausgewiesen statt heimlich.

### 6.5 Cache und Wiederaufnahme

Jede Modellantwort wird sofort auf Platte geschrieben, der Schlüssel ist der Prompt und
nicht das Modell. Ein Abbruch kostet damit nur den laufenden Chunk. Entwicklungsiterationen
verbrauchen kein Kontingent, weil sie aus dem Cache bedient werden. Ändert sich der
Berichtstext, etwa durch die Kodierungsreparatur, ändert sich der Schlüssel und der Chunk
wird korrekt neu abgefragt.

### 6.6 Datenschutz

Der kostenlose Zugang von Google nutzt Eingaben zur Produktverbesserung. Geschäftsberichte
sind öffentliche Dokumente, deshalb unkritisch. Bei Mandantendaten wäre derselbe Aufbau
nicht zulässig. Der API-Schlüssel liegt als Umgebungsvariable auf dem eigenen Rechner und
steht in keiner Datei des Repositories.

---

## 6b. Ergebnis des Pilotlaufs PALFINGER, 04.09.2026

Erster vollstaendiger Lauf nach allen Korrekturen. Modell gemini-3.5-flash,
acht Chunks, 102 von 286 Seiten ausgewertet.

| Kennzahl | Wert |
|---|---|
| extrahierte Elemente | 51 |
| Zitat exakt und eindeutig belegt | 47 |
| Zitat exakt, aber mehrfach im Bericht | 1 |
| nur Wortpraefix passend, Pruefung noetig | 2 |
| Zitat nicht im Bericht auffindbar | 1 |
| **maschinell nachgewiesene Halluzinationsrate** | **1 von 51, also 2,0 Prozent** |

Zum Vergleich: Der Lauf mit doppelt so grossen Chunks lieferte nur 34 Elemente.
Kleinere Anfragen finden mehr, weil das Modell weniger Kontext gleichzeitig
verarbeiten muss.

**Der eine erfundene Beleg.** Zum Risiko "US-Zoelle" lieferte das Modell das Zitat
"Im Jahr 2025 wurde eine Krisen-Taskforce als Reaktion auf die US-Zoelle eingerichtet,
um die negativen finanziellen Auswirkungen zu minimieren." Dieser Satz steht nicht im
Bericht. Das Risiko selbst ist belegt und taucht ueber ein anderes Element korrekt mit
Seite 46 auf. Das Modell hat also nicht das Thema erfunden, sondern den Beleg dafuer.
Genau diese Unterscheidung macht die Architektur sichtbar.

**Die Modellkette hat gegriffen.** Das Feld `tatsaechlich_benutzte_modelle` weist
gemini-3.5-flash und gemini-3.8-flash aus. Mindestens ein Chunk wurde nach wiederholten
503-Antworten vom Ausweichmodell beantwortet. Der Lauf ist damit ein dokumentiert
gemischter Lauf, keine stillschweigende Vermischung.

**Die Abschnittskennzeichnung greift.** 10 von 51 Elementen stammen aus der
Nachhaltigkeitsberichterstattung, 41 aus dem Geschaeftsteil. Die gekennzeichneten
Elemente sind erkennbar die richtigen: taxonomiefaehige CapEx-Einzelmassnahmen,
Photovoltaikanlagen, Ladestationen, CO2-Bepreisung, Scope-1-und-2-Emissionen.

Ein bekannter Fehler bleibt: Seite 150 wird dem Geschaeftsbericht zugeordnet, obwohl
sie zur Nachhaltigkeitsberichterstattung gehoert. Das ist genau der eine Fall aus der
Kalibrierung, der nicht erkannt wurde. Er steht so in den Limitationen.

---

## 6c. Tageslimit und Einmodelllauf, 05.09.2026

**Befund aus dem Kontingent-Dashboard.** Der kostenlose Zugang erlaubt **20 Anfragen pro
Tag und Modell** bei 250.000 Tokens pro Minute. Der Engpass ist also die Anzahl der
Anfragen, nicht deren Groesse. Die Token-Auslastung lag bei 18 Prozent, waehrend alle
fuenf Flash-Modelle ihr Tageslimit gerissen hatten.

**Das erklaert den gemischten Datensatz rueckwirkend.** Die Modellkette wechselte nicht
nur bei Ueberlastung, sondern auch, als die Tageskontingente nacheinander leerliefen.
Vier Modelle im Datensatz waren Folge des Limits, nicht des Zufalls.

**Zwei Korrekturen am Code:**

1. Ein 429, der auf das Tageslimit verweist, beendet den Lauf sofort statt zu warten.
   Ohne diese Unterscheidung haette der strikte Modus bei 40 offenen Chunks je 32 Minuten
   ins Leere gewartet, zusammen ueber 21 Stunden.
2. Im strikten Modus bekommt jedes Modell ein eigenes Cache- und Datenverzeichnis. Der
   Cache-Schluessel hing bis dahin nur am Prompt. Ein Einmodelllauf haette die Antworten
   des gemischten Laufs wiederverwendet und waere gar kein Einmodelllauf gewesen.

**Entscheidung.** Vollstaendiger Neulauf aller sieben Unternehmen auf gemini-3.8-flash im
strikten Modus. 49 offene Anfragen bei 20 pro Tag, also drei Tage. Der gemischte Lauf
bleibt als zweiter Datensatz erhalten.

### Der Modellvergleich, und warum die erste Fassung methodisch schwach war

Erste Auswertung ueber den gemischten Lauf, 392 Elemente:

| Modell | Elemente | woertlich belegt | Beleg nicht auffindbar |
|---|---|---|---|
| gemini-3.8-flash | 46 | 98 % | 0 % |
| gemini-3.5-flash | 50 | 88 % | 4 % |
| gemini-3.7-flash | 96 | 72 % | 7 % |
| gemini-3-flash-preview | 149 | 64 % | 10 % |

**Diese Zahlen haben einen Confounder.** Welches Modell welchen Chunk bearbeitete, entschied
nicht der Zufall, sondern welches gerade antwortete. Es ist nicht auszuschliessen, dass ein
Modell systematisch die einfacheren Abschnitte bekam, etwa Lageberichtstext statt
ESRS-Tabellen. Als Beleg fuer Modellunterschiede taugt die Tabelle daher nur bedingt.

**Der saubere Vergleich faellt als Nebenprodukt an.** Nach dem Einmodelllauf existiert fuer
alle 60 Chunks eine Antwort von gemini-3.8-flash. Der gemischte Cache enthaelt fuer
dieselben Chunks 19 Antworten von 3-flash-preview, 16 von 3.7-flash und 7 von 3.5-flash.
Identischer Prompt, identischer Quelltext, identische Chunkgrenzen, nur das Modell
unterscheidet sich. Das ergibt einen paarweisen Vergleich ohne zusaetzliche Anfragen.

**Interviewwert.** Der Unterschied zwischen einer Korrelation aus Betriebsdaten und einem
kontrollierten paarweisen Vergleich ist genau die Art von Unterscheidung, nach der in
Fallstudien gefragt wird. Die erste Tabelle war ein Hinweis, nicht ein Beleg.

---

## 7. Typische Interviewfragen und die Antworten aus diesem Projekt

**Wie habt ihr Halluzinationen kontrolliert?**
Das Modell gibt keine Seitenzahlen aus. Es liefert nur wörtliche Zitate, die Pipeline sucht
sie im Quelltext. Ein Zitat, das nicht gefunden wird, ist erfunden. Das deckt 100 Prozent
der Extraktionen ab, nicht nur eine Stichprobe. Die Handprüfung misst danach nur noch
inhaltliche Verzerrung und falsche Kategorien.

**Wie hoch war die Fehlerquote?**
Im Pilotlauf PALFINGER 1 erfundener Beleg auf 51 Elemente, also 2,0 Prozent, plus zwei
Faelle mit nur teilweise passendem Zitat. Ueber alle sieben Unternehmen erst nach dem
Vollauf belastbar. Wichtig ist die Trennung: Vorverarbeitungsfehler, Zuordnungsfehler der
Pipeline und Modellfehler werden getrennt ausgewiesen. Der allererste Messwert lautete
1 von 34, war aber ein eigener Kodierungsfehler und keine Halluzination.

**Warum genau diese sieben Unternehmen?**
Auswahlregel über die Branchensystematik der Wiener Börse, festgeschrieben vor der ersten
Extraktion. Zwei Sektorausschlüsse mit je einer sachlichen Begründung. Ein unbequemer Fall,
Schoeller-Bleckmann, wurde nicht nachträglich hineingeholt.

**Warum kein besseres Modell?**
Ziel war eine gemessene Fehlerquote, nicht das bestmögliche Ergebnis. Ein sauber
dokumentierter Lauf auf einem schnellen Modell ist für die Fragestellung wertvoller. Die
Modellwahl folgte gemessener Antwortzeit, weil hohe Latenz schon bei Minimalanfragen auf
einen überlasteten Endpunkt hinweist.

**Was würdet ihr beim nächsten Mal anders machen?**
Die Kapitelauswahl läuft über feste Schlagwortlisten. Ein Modellaufruf pro
Inhaltsverzeichnis wäre robuster gegen unterschiedliche Berichtsstrukturen und würde die
Eingabemenge von 35 auf schätzungsweise 20 Prozent drücken. Außerdem gehört ein
Zeichenkodierungs-Check vor die erste Extraktion und nicht mittendrin.

**Was ist die größte Schwäche der Analyse?**
n gleich sieben, aufgeteilt in vier zu drei. Gruppenweise Häufigkeitsvergleiche sind damit
statistisch nicht belastbar. Der Kontrast zwischen exportgetriebenen Herstellern und
Bauunternehmen wird qualitativ mit Zitatbeleg dargestellt, nicht als quantitativer
Vergleich. Dazu kommt das uneinheitliche Berichtsjahr bei voestalpine.

---

## 8. Offenlegung

PALFINGER war von Februar bis Juni 2025 Arbeitgeber des Autors im Bereich Corporate
Development. Vorwissen fließt ausschließlich in die Plausibilitätsprüfung der Extraktion
ein, nicht in die Extraktion selbst. Die Offenlegung steht auch im Briefing.

---

## 9. Offene Punkte

- Einmodelllauf gemini-3.8-flash, 49 offene Anfragen, drei Tage ab 06.09.2026
- Paarweiser Modellvergleich aus dem gemischten und dem Einmodell-Cache
- Schritt 3: Handprüfung an drei zufällig gezogenen Unternehmen, Klassifikation nach
  korrekt, Seitenangabe falsch, Zitat erfunden, Inhalt verzerrt
- Schritt 4: Aggregation, Heatmap Unternehmen mal Wachstumsregion, Häufigkeit der
  Risikokategorien
- Schritt 5: Briefing, README, Repository aufräumen
- Dieses Dokument als `DECISIONS.md` ins Repository übernehmen
