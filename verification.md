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

Ein Element kann mehrere Klassen tragen. Gezählt wird je Klasse, nicht je Element.

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

## 5. Ergebnisse

Wird nach dem Einmodelllauf gefüllt.
