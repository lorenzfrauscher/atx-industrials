# Paarweiser Modellvergleich

Verglichen werden Antworten auf **identische Chunks**: gleicher Prompt, gleicher Quelltext, gleiche Chunkgrenzen. Der Cache-Dateiname enthält den Prompt-Hash, gleiche Dateinamen bedeuten also identische Eingabe.

Je Gegenmodell wird nur die Schnittmenge ausgewertet, also genau die Chunks, die beide Modelle bearbeitet haben. Ein Vergleich über unterschiedliche Chunks wäre kein Modellvergleich, sondern könnte die Schwierigkeit des Textes messen.

Referenzmodell: **gemini-3.8-flash**

| Gegenmodell | gemeinsame Chunks | Elemente Ref/Gegen | wörtlich belegt | nur teilweise | nicht auffindbar |
|---|---|---|---|---|---|
| gemini-3-flash-preview | 19 | 106 / 149 | 83% / 64% | 14% / 26% | 3% / 10% |
| gemini-3.7-flash | 16 | 87 / 96 | 78% / 72% | 17% / 21% | 5% / 7% |
| gemini-3.5-flash | 7 | 69 / 50 | 93% / 88% | 4% / 8% | 3% / 4% |

Jede Zelle nennt zuerst den Wert des Referenzmodells, dann den des Gegenmodells, gemessen an denselben Textabschnitten.

