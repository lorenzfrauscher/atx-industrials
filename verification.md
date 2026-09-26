# Verifikation, Schritt 3

**Status: Stichprobe gezogen am 05.09.2026, vor Vorliegen der Ergebnisdaten.**
Die Extraktion auf gemini-3.8-flash lief zu diesem Zeitpunkt noch nicht. Die Ziehung
konnte daher nicht durch Kenntnis der Ergebnisse beeinflusst sein.

---

## 1. Stichprobe

Ziehung per `random.sample` aus dem Universum von sieben Unternehmen.

```python
firmen = ["voestalpine","lenzing","andritz","palfinger","wienerberger","strabag","porr"]
random.seed(20260905)
stichprobe = sorted(random.sample(firmen, 3))
```

**Seed: 20260905** (Datum der Ziehung). Dreimal hintereinander identisch reproduziert.

**Gezogen: andritz, voestalpine, wienerberger.**

PALFINGER wurde nicht gezogen. Das ist günstig, denn der Autor war dort tätig und eine
Prüfung ausgerechnet dieses Berichts wäre angreifbar gewesen. Der Zufall hat die
Offenlegungsfrage entschärft, nicht die Auswahl.

---

## 2. Prüfverfahren

Jedes extrahierte Element der drei Unternehmen wird gegen die angegebene PDF-Seite im
Originalbericht geprüft. `beleg_seite` ist der 1-basierte PDF-Seitenindex der deutschen
Fassung, nicht die gedruckte Seitenzahl.

Zwei Prüfebenen, weil zwei verschiedene Dinge schiefgehen können.

### Ebene A: maschinell, bereits in der Pipeline

Wird für 100 Prozent der Elemente automatisch bestimmt, nicht nur für die Stichprobe.

| Treffertyp | Bedeutung |
|---|---|
| `exakt` | Zitat steht wörtlich genau einmal im Bericht |
| `exakt_nach_normalisierung` | Zitat stimmt überein, wenn Satzzeichen, Trennstriche und Aufzählungszeichen ignoriert werden |
| `exakt_mehrdeutig` | Zitat steht wörtlich, aber mehrfach. Seitenangabe nicht eindeutig |
| `teilweise` | nur ein Wortpräfix passt. Verdacht auf Kürzung oder Paraphrase |
| `nicht_gefunden` | Zitat kommt im Bericht nicht vor. Erfunden |

### Ebene B: von Hand, nur für die drei gezogenen Unternehmen

Was eine Maschine nicht sehen kann.

| Klasse | Definition |
|---|---|
| `korrekt` | Aussage gibt den Berichtsinhalt zutreffend wieder |
| `seitenangabe_falsch` | Zitat vorhanden, aber auf einer anderen Seite als angegeben |
| `zitat_erfunden` | Zitat steht so nicht im Bericht |
| `inhalt_verzerrt` | Zitat korrekt, aber die abgeleitete Aussage verdreht oder überdehnt es |
| `kontext_entrissen` | Zitat korrekt, ergibt aber ohne Umgebung einen anderen Sinn |
| `kategorie_falsch` | Risikokategorie oder Region unpassend zugeordnet |
| `beleg_stuetzt_nicht` | Zitat echt, Aussage inhaltlich richtig, aber nicht im zitierten Satz belegt |
| `unklar` | nicht eindeutig entscheidbar, wird gesondert ausgewiesen |

Ein Element kann mehrere Klassen tragen. Gezählt wird je Klasse, nicht je Element.

---

## 2b. Auslegungsregeln, festgehalten während der Prüfung

Bei der Handprüfung traten Grenzfälle auf, die nicht aus der Klassenliste allein zu
entscheiden waren. Die Regeln wurden jeweils vor der weiteren Bearbeitung festgelegt und
danach auf alle Einträge einheitlich angewandt. Eine Regel, die erst nach Sichtung aller
Ergebnisse formuliert würde, wäre wertlos.

### Regel 1: Konjunktivisch formulierte Risiken (festgelegt 19.09.2026)

**Fall.** Das Zitat formuliert ein Risiko im Konjunktiv ("Sollte sich das Umfeld
verschlechtern, könnten sich negative Auswirkungen ergeben"). Die abgeleitete Aussage
benennt es nominal ("Verschlechterung des makroökonomischen Umfelds").

**Regel.** Das gilt als `korrekt`, nicht als `inhalt_verzerrt`.

**Begründung.** Das Feld heißt `risiko` und verlangt die Bezeichnung eines Risikos, nicht
die Beschreibung eines eingetretenen Zustands. Ein Risiko ist per Definition hypothetisch,
und die Nominalform ist die übliche Bezeichnung in jedem Risikobericht.
"Zinsänderungsrisiko" behauptet auch nicht, dass die Zinsen gestiegen sind.

**Abgrenzung.** `inhalt_verzerrt` greift, sobald die Aussage im Indikativ einen Eintritt
behauptet, etwa "Das Umfeld hat sich verschlechtert".

**Umfang der Entscheidung.** 8 der 56 geprüften Hauptrisiken haben ein konjunktivisches
Zitat, also 6 Prozent der Stichprobe von 134. Bei Andritz 3, bei Wienerberger 5, bei
voestalpine keines. Die Gegenregel hätte die ausgewiesene Fehlerquote um bis zu sechs
Prozentpunkte erhöht.

**Offengelegte Alternative.** Die strengere Lesart ist vertretbar: Wer nur die Aussage ohne
das Zitat liest, könnte sie für eine Zustandsbeschreibung halten. Die saubere Lösung liegt
aber nicht in der Bewertung, sondern im Prompt. Das Modell könnte angewiesen werden, die
Bedingtheit in die Risikobezeichnung zu übernehmen. Das gehört in die Limitationen und in
eine nächste Version, nicht in die Fehlerquote dieser.

### Regel 2: Beleg stützt die Aussage nicht (festgelegt 19.09.2026)

**Neue Fehlerklasse `beleg_stuetzt_nicht`.**

**Fall.** Das Zitat ist echt, steht auf der angegebenen Seite und wurde maschinell als
`exakt` bestätigt. Die Aussage ist inhaltlich richtig und steht so im Bericht. Sie steht
aber **nicht im zitierten Satz**, sondern daneben.

Gefunden an AND-032: Das Zitat berichtet, dass Ende 2024 Sachanlagen in Kanada mit
0,5 MEUR als zur Veräußerung gehalten ausgewiesen wurden. Die Aussage berichtet, dass sie
2025 mit einem Gewinn von 0,8 MEUR veräußert wurden. Diese Information steht im
darauffolgenden Satz des Berichts, nicht im Zitat.

**Warum eine eigene Klasse und nicht `inhalt_verzerrt`.** Bei `inhalt_verzerrt` ist die
Aussage inhaltlich falsch. Hier ist sie richtig, nur der Beleg ist der falsche Satz. Für
die Auswertung sind das verschiedene Befunde mit verschiedenen Konsequenzen. Der eine
bedeutet, dass die Extraktion Inhalte verfälscht. Der andere bedeutet, dass die
Belegkette bricht, obwohl der Inhalt stimmt.

**Warum diese Klasse die wichtigste des Projekts ist.** Die Architektur dieser Pipeline
beruht darauf, dass jede Aussage einen maschinell überprüfbaren wörtlichen Beleg trägt.
Genau diese Zusicherung bricht hier, und zwar unsichtbar: Die Zitatsuche bestätigt das
Zitat, die Seitenangabe stimmt, und trotzdem belegt der Satz die Aussage nicht. Weder die
automatische Prüfung noch ein flüchtiger Blick findet das. Nur die Handprüfung.

**Automatischer Vorabfilter, bewusst als unvollständig ausgewiesen.** Eine Heuristik
vergleicht Zahlen in der Aussage mit Zahlen im Zitat. Steht eine Zahl nicht im Zitat, aber
in der Umgebung, liegt der Verdacht nahe. Sie findet 3 der 134 Einträge (AND-030, AND-032,
WIE-118). Sie erkennt ausschliesslich zahlenbasierte Fälle. Fälle ohne Zahlen bleiben
unentdeckt und sind nur von Hand zu finden. Die ausgewiesene Häufigkeit dieser Fehlerklasse
ist daher eine Untergrenze.

**Keine Nacharbeit nötig.** Zum Zeitpunkt der Festlegung waren 23 Einträge geprüft, keiner
davon ein Verdachtsfall der Heuristik.

---

## 3. Auswertungsraster

Trefferquote je Feldtyp, getrennt nach Herkunftsabschnitt, weil ESRS-Text und
Lageberichtstext unterschiedlich schwer zu extrahieren sind.

| Feldtyp | n | korrekt | Seite falsch | erfunden | verzerrt | Kategorie falsch |
|---|---|---|---|---|---|---|
| strategische_prioritaeten | | | | | | |
| wachstumsmaerkte | | | | | | |
| hauptrisiken | | | | | | |
| capex_ma_signale | | | | | | |

Zusätzlich getrennt ausweisen:

- Fehler der **Vorverarbeitung** (Zeichenkodierung, Seitenzuordnung, Abschnittsklassifikator)
- Fehler des **Modells** (erfundene Zitate, Verzerrung, falsche Kategorie)

Diese Trennung ist der Kern. Beim ersten Pilotlauf wurde ein Kodierungsfehler der Pipeline
zunächst als Halluzination des Modells gezählt. Ohne die Trennung entstehen falsche Aussagen
über die Zuverlässigkeit von Sprachmodellen.

---

## 4. Bekannte Einschränkungen, vor der Prüfung notiert

- Der Abschnittsklassifikator erkannte in der Kalibrierung 6 von 7 Nachhaltigkeitsseiten.
  Seite 150 des PALFINGER-Berichts wird dem Geschäftsteil zugeordnet, obwohl sie zur
  Nachhaltigkeitsberichterstattung gehört. Die Fehlerrichtung ist bewusst konservativ,
  der ausgewiesene ESRS-Anteil ist eine Untergrenze.
- Vier Sonderzeichen des PALFINGER-Berichts und 18 des Lenzing-Berichts konnten keiner
  Regel zugeordnet werden und wurden entfernt.
- Das Berichtsjahr ist nicht einheitlich. voestalpine schließt zum 31.03.2026 ab, die
  übrigen sechs zum 31.12.2025.

---

## 5. Ergebnisse der Handpruefung

Gepruefte Elemente: **134** aus drei zufaellig gezogenen Unternehmen. Ein Element kann mehrere Fehlerklassen tragen, deshalb uebersteigt die Summe der Klassen die Zahl der fehlerhaften Elemente.

**Vollstaendig korrekt: 111 von 134, also 83 Prozent.**


### Nach Unternehmen

| Unternehmen | geprueft | korrekt | Fehlerklassen |
|---|---|---|---|
| Andritz AG | 33 | 30 (91%) | kategorie_falsch 1, beleg_stuetzt_nicht 2 |
| Wienerberger AG | 36 | 31 (86%) | beleg_stuetzt_nicht 5 |
| voestalpine AG | 65 | 50 (77%) | inhalt_verzerrt 2, beleg_stuetzt_nicht 14 |


### Nach Feldtyp

| Feldtyp | geprueft | korrekt | Fehlerklassen |
|---|---|---|---|
| strategische_prioritaeten | 28 | 25 (89%) | inhalt_verzerrt 1, beleg_stuetzt_nicht 2 |
| wachstumsmaerkte | 8 | 6 (75%) | kategorie_falsch 1, beleg_stuetzt_nicht 1 |
| hauptrisiken | 56 | 45 (80%) | beleg_stuetzt_nicht 11, inhalt_verzerrt 1 |
| capex_ma_signale | 42 | 35 (83%) | beleg_stuetzt_nicht 7 |


### Nach Herkunftsabschnitt

| Abschnitt | geprueft | korrekt |
|---|---|---|
| Geschaeftsbericht | 89 | 76 (85%) |
| Nachhaltigkeitsberichterstattung | 45 | 35 (78%) |


### Fehlerklassen ueber alle geprueften Elemente

| Fehlerklasse | Faelle | Anteil an allen geprueften |
|---|---|---|
| beleg_stuetzt_nicht | 21 | 15.7% |
| inhalt_verzerrt | 2 | 1.5% |
| kategorie_falsch | 1 | 0.7% |


### Was die Maschine gesehen hat und was nicht

| Befund | Anzahl |
|---|---|
| von der Zitatsuche als erfunden gemeldet | 0 |
| nur durch Handpruefung gefunden | 23 |

Die automatische Zitatpruefung beweist, dass ein Satz im Dokument steht. Sie beweist nicht, dass er die daraus abgeleitete Aussage traegt. Diese Luecke schliesst nur die Handpruefung.

### Aufwand

Die Handprüfung von 134 Elementen aus drei Berichten verteilte sich über mehrere Sitzungen
zwischen dem 19. und 25.09.2026. Der Umgebungstext in der Prüfliste ersetzte das Blättern im
PDF für den Großteil der Fälle. Ohne ihn wäre der Aufwand ein Vielfaches gewesen.

### Korrektur einer Fehlmessung während der Prüfung

Die Handprüfung deckte einen Fehler der automatischen Zitatsuche auf. Bei AND-033 meldete
die Pipeline ein Zitat als nicht auffindbar. Es steht auf Seite 89, die PDF-Extraktion hatte
dort ein Leerzeichen mitten in ein Wort gesetzt ("d as" statt "das"), woran der wortweise
Vergleich scheiterte.

Nach Einbau einer dritten Vergleichsstufe, die Leerzeichen ignoriert, sank die maschinell
gemessene Zahl nicht auffindbarer Zitate über alle 369 Elemente von 15 auf 0. **Alle
zunächst gemeldeten Halluzinationen waren Messfehler der eigenen Pipeline.**

Die Richtung des Fehlers ist bemerkenswert: Die erste Messung überschätzte die
Unzuverlässigkeit des Modells. Ohne die Handprüfung wäre eine Fehlerquote von 4,1 Prozent
veröffentlicht worden, die es nicht gibt.

