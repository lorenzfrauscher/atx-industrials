# Prueferliste Schritt 3

Stichprobe: **andritz, voestalpine, wienerberger**, gezogen am 05.09.2026 mit Seed 20260905, vor Vorliegen der Ergebnisdaten.

## So arbeitest du damit

Jeder Eintrag zeigt das Zitat und den Text, der es im Bericht umgibt. In den meisten Faellen genuegt das fuer ein Urteil. Das PDF brauchst du nur fuer Zweifelsfaelle und fuer die Kontrollstichprobe am Ende.

Trag dein Urteil in `pruefliste.csv` in die Spalte `urteil` ein. Mehrere Urteile mit Komma trennen. Erlaubte Werte:

```
korrekt              Aussage gibt den Berichtsinhalt zutreffend wieder
seitenangabe_falsch  Zitat vorhanden, aber auf einer anderen Seite
zitat_erfunden       Zitat steht so nicht im Bericht
inhalt_verzerrt      Zitat korrekt, abgeleitete Aussage verdreht oder ueberdehnt es
kontext_entrissen    Zitat korrekt, ergibt ohne Umgebung einen anderen Sinn
kategorie_falsch     Risikokategorie oder Region unpassend zugeordnet
unklar               nicht eindeutig entscheidbar, wird gesondert ausgewiesen
```

Elemente mit dem Treffertyp `nicht_gefunden` oder `teilweise` sind vorsortiert die interessanten. Sie stehen trotzdem an ihrer Seitenposition, damit du den Bericht einmal von vorne nach hinten durchgehen kannst.


---

# Andritz AG  (andritz_2025.pdf, 33 Elemente)


### AND-001 | PDF-Seite 8 | wachstumsmaerkte / Lateinamerika

**Aussage:** Wiederbelebung und Initiierung von neuen Greenfield-Projekten im Wasserkraft- und Speicherbereich

**Zitat:** „Während in westlichen Märkten wie Nordamerika und Europa weiterhin Sanierungs - und Modernisierungsprojekte dominierten, wurden in Schwellen regionen wie Afrika, Asien und Lateinamerika wieder vermehrt neue Greenfield -Projekte (bspw. Pumpspeicher) initiiert.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...nterstützende Strompreisniveaus. Diese Entwicklung spiegelt den anhaltenden globalen Trend zur Elektrifizierung und Dekarbonisierung wider. Während in westlichen Märkten wie Nordamerika und Europa weiterhin Sanierungs - und Modernisierungsprojekte dominierten, wurden in Schwellen regionen wie Afrika, Asien und Lateinamerika wieder vermehrt neue Greenfield -Projekte (bspw. Pumpspeicher) initiiert. Die zunehmende Nachfrage nach Energiespeicherung sowie die steigenden Anforderungen an die Netzstabilität förderten die Investitionstätigkeit im Markt für Pumpspeicherkraftwerke und Synchronkondensatoren weite...


### AND-002 | PDF-Seite 9 | wachstumsmaerkte / Nordamerika

**Aussage:** Starke Nachfrage und Wachstumstreiber bei Neuanlagen und Modernisierungen im Bereich Clean Air Technologies

**Zitat:** „Demgegenüber entwickelten sich die Märkte für Clean Air Technologies sehr positiv. Die größten Treiber dieser Entwicklung waren die steigende Nachfrage nach Neuanlagen sowie nach Modernisierungen bestehender Anlagen, insbesondere in etablierten Industrieregionen wie den USA.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...ndeutete. Zusätzliche Projektvergaben im Bereich Green Hydrogen verzögerten sich aufgrund des weiterhin unsicheren regulatorischen Umfelds. Demgegenüber entwickelten sich die Märkte für Clean Air Technologies sehr positiv. Die größten Treiber dieser Entwicklung waren die steigende Nachfrage nach Neuanlagen sowie nach Modernisierungen bestehender Anlagen, insbesondere in etablierten Industrieregionen wie den USA. Die Märkte für Feed und Biofuel verzeichneten trotz des insgesamt unsicheren Marktumfelds ein moderates Wachstum.


### AND-003 | PDF-Seite 20 | capex_ma_signale

**Aussage:** Fokus der Investitionen auf Modernisierungen und gezielte Kapazitätserweiterungen in Kernregionen

**Zitat:** „Die Investitionsschwerpunkte betrafen – wie in den Vorjahren – insbesondere Modernisierungen von Fertigungs - stätten sowie vereinzelte Erweiterungsinvestitionen zur Unterstützung des Wachstums im Wesentlichen in Nordamerika, Europa und China.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ... 57 (48) B METALS 15 (25) B IT 13 (6) C HYDROPOWER 20 (20) C Forschung & Entwicklung 7 (11) D ENVIRONMENT & ENERGY 27 (22) D Übrige 23 (35) Die Investitionsschwerpunkte betrafen – wie in den Vorjahren – insbesondere Modernisierungen von Fertigungs - stätten sowie vereinzelte Erweiterungsinvestitionen zur Unterstützung des Wachstums im Wesentlichen in Nordamerika, Europa und China. A B C D A B C D INVESTITION EN SBA Investitionen nach Geschäftsbereichen 2025 (2024) in % Investitionen nach Kategorien 2025 (2024) in %


### AND-004 | PDF-Seite 21 | capex_ma_signale  **PRUEFEN**

**Aussage:** Erhöhte Auszahlungen für Unternehmenserwerbe im Geschäftsjahr 2025.

**Zitat:** „Die Veränderung resultiert vor allem aus dem höheren Netto -Cashflow aus Unternehmenserwerben von -328,6 MEUR (2024: -36,9 MEUR) sowie den höheren Auszahlungen für den Kauf von lang- und kurzfristigen finanziellen Vermögenswerten.“

**Treffertyp:** `exakt_mehrdeutig`  (weitere Fundstellen: 140)

**Umgebung im Bericht:**

> ...EUR) betrug der Free Cashflow 383,2 MEUR (2024: 399,0 MEUR). Der Cashflow aus Investitionstätigkeit betrug -541,6 MEUR (2024: -207,5 MEUR). Die Veränderung resultiert vor allem aus dem höheren Netto -Cashflow aus Unternehmenserwerben von -328,6 MEUR (2024: -36,9 MEUR) sowie den höheren Auszahlungen für den Kauf von lang- und kurzfristigen finanziellen Vermögenswerten. Der Cashflow aus Finanzierungstätigkeit betrug -320,6 MEUR (2024: -753,3 MEUR). Die Veränderung ist vor allem bedingt durch geringere Rückzahlungen von Schuldscheindarlehen (-127,5 MEUR 2025 gegenüber -300,0 M...


### AND-005 | PDF-Seite 22 | capex_ma_signale

**Aussage:** Übernahme der LDX-Gruppe zur Stärkung des Angebots zur Emissionsreduktion

**Zitat:** „ANDRITZ hat im Februar 2025 die in den USA ansässige Dustex LLC samt Tochtergesellschaft Western Pneumatics, LLC (gemeinsam LDX -Gruppe) erworben. LDX zählt zu den führenden Anbietern von Technologien und Dienstleistungen zur Emissionsreduktion“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> A N D R I T Z- F i n a n z b e r i c h t 2 0 25 Lagebericht 21 8. Akquisitionen ANDRITZ hat im Februar 2025 die in den USA ansässige Dustex LLC samt Tochtergesellschaft Western Pneumatics, LLC (gemeinsam LDX -Gruppe) erworben. LDX zählt zu den führenden Anbietern von Technologien und Dienstleistungen zur Emissionsreduktion für die nordamerikanische Industrie und erweitert das bestehende Produktangebot im Geschäftsbereich Environment & Energy. ANDRITZ erwarb im Juli 2025 die A.Celli Paper S.P.A. mit Sitz in Italien, samt weiteren...


### AND-006 | PDF-Seite 22 | capex_ma_signale

**Aussage:** Akquisition von A.Celli Paper zur Erweiterung der Papier- und Kartonsparte

**Zitat:** „ANDRITZ erwarb im Juli 2025 die A.Celli Paper S.P.A. mit Sitz in Italien, samt weiteren Tochtergesellschaften in Italien und China. A.Celli verfügt über jahrzehntelange Erfahrung in der Lieferung von Maschinen“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...missionsreduktion für die nordamerikanische Industrie und erweitert das bestehende Produktangebot im Geschäftsbereich Environment & Energy. ANDRITZ erwarb im Juli 2025 die A.Celli Paper S.P.A. mit Sitz in Italien, samt weiteren Tochtergesellschaften in Italien und China. A.Celli verfügt über jahrzehntelange Erfahrung in der Lieferung von Maschinen und Kernkomponenten für die Produktion von Tissue, Papier und Karton und erweitert das bestehende Produkt - angebot im Geschäftsbereich Pulp & Paper. Des weiteren hat ANDRITZ im Juli 2025 die Salico -Gruppe, m...


### AND-007 | PDF-Seite 22 | capex_ma_signale

**Aussage:** Erwerb der Salico-Gruppe zur Abrundung des Angebots bei Endbearbeitungsanlagen

**Zitat:** „Des weiteren hat ANDRITZ im Juli 2025 die Salico -Gruppe, mit Hauptsitz in Italien und Spanien erworben. Der Erwerb umfasst auch Tochtergesellschaften in Großbrita nnien, den USA und Indien.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...mponenten für die Produktion von Tissue, Papier und Karton und erweitert das bestehende Produkt - angebot im Geschäftsbereich Pulp & Paper. Des weiteren hat ANDRITZ im Juli 2025 die Salico -Gruppe, mit Hauptsitz in Italien und Spanien erworben. Der Erwerb umfasst auch Tochtergesellschaften in Großbrita nnien, den USA und Indien. Salico ist auf die Entwicklung und Herstellung von hochentwickelten Endbear beitungsanlagen für die Ve rarbeitung von Metallbändern spezialisiert. Diese Übernahme stellt einen weiteren wichtigen Schritt in der...


### AND-008 | PDF-Seite 22 | capex_ma_signale

**Aussage:** Mehrheitserwerb an Baoding Sanzheng Electrical Equipment zur Stärkung bei Induktionserwärmung

**Zitat:** „ANDRITZ hat im Dezember 2025 51% der Anteile an Boading Sanzheng Electrical Equipment Co., Ltd. mit dem Hauptsitz in China unterzeichnet. Die Integration von Sanzheng bringt ANDRITZ ein vollständiges Portfolio von Induktionserwärmungstechnologien“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ... mit Ersatzteilen, Wartungsleistungen und Systemmodernisierungen und stärkt das bestehende Produktangebot im Geschäftsbereich Pulp & Paper. ANDRITZ hat im Dezember 2025 51% der Anteile an Boading Sanzheng Electrical Equipment Co., Ltd. mit dem Hauptsitz in China unterzeichnet. Die Integration von Sanzheng bringt ANDRITZ ein vollständiges Portfolio von Induktionserwärmungstechnologien und stärkt die Kompetenz des Unternehmens, Komplettlösungen für die Verarbeitung von Elektroband, Verzinkung, Glühen und Schmieden zu liefern. Die Akquisition erweitert das bestehende Produktangebot im Geschäf...


### AND-009 | PDF-Seite 24 | hauptrisiken / Regulierung

**Aussage:** Nachträgliche Steuer- und Zollbelastungen durch Gesetzesänderungen oder veränderte Auslegungen

**Zitat:** „Eine Änderung von Gesetzen oder sonstigen Bestimmungen – darunter fallen auch Regelungen zu Importzöllen etc. – sowie unterschiedliche Auslegungen der jeweils geltenden Bestimmungen können zu nachträglichen Steuer - und Zollbelastungen führen.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ... jeweiligen Ländern den lokalen Steuergesetzen unterworfen und müssen sowohl Ertragsteuern, Einfuhrzölle, als auch andere Steuern bezahlen. Eine Änderung von Gesetzen oder sonstigen Bestimmungen – darunter fallen auch Regelungen zu Importzöllen etc. – sowie unterschiedliche Auslegungen der jeweils geltenden Bestimmungen können zu nachträglichen Steuer - und Zollbelastungen führen. Dementsprechend können die Steuern und Zölle etwaigen positiven oder negativen Schwankungen ausgesetzt sein. In Österreich und in anderen Ländern, in denen die ANDRITZ -Gruppe tätig ist, sind eine Reihe von re...


### AND-010 | PDF-Seite 25 | hauptrisiken / Markt

**Aussage:** Intensive Wettbewerbssituation und Preiskampf um wenige Großaufträge mit Auswirkungen auf Margen

**Zitat:** „Die ANDRITZ -Gruppe agiert in sehr wettbewerbsintensiven Märkten, in denen einige wenige große Anbieter um einige wenige Großaufträge bieten. Darüber hinaus gibt es lokal eine Vielzahl kleiner konkurrierenden Unternehmen, die über eine vergleichsweise niedrige Kostenbasis verfügen.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> A N D R I T Z- F i n a n z b e r i c h t 2 0 25 Lagebericht 24 c) Wettbewerbsposition Die ANDRITZ -Gruppe agiert in sehr wettbewerbsintensiven Märkten, in denen einige wenige große Anbieter um einige wenige Großaufträge bieten. Darüber hinaus gibt es lokal eine Vielzahl kleiner konkurrierenden Unternehmen, die über eine vergleichsweise niedrige Kostenbasis verfügen. Einen Großkunden zu verlieren, stellt ein zusätzliches Risiko dar . Diese Wettbewerbssituation oder eine mögliche Änderung der Wettbewerbsstruktur können sich negativ auf den Auftragseingang sowie die Umsatzma...


### AND-011 | PDF-Seite 25 | hauptrisiken / Markt

**Aussage:** Volatilität des Auftragseingangs durch konjunkturelle Schwankungen und Abhängigkeit von der Endproduktnachfrage

**Zitat:** „Mögliche Preisschwankungen können daher einen direkten Einfluss auf die Investitionsentscheidungen von Kunden und in weiterer Folge auf den Auftragseingang der Gruppe haben. Dies könnte daher zu einer Volatilität in der Entwicklung des Auftragseingangs führen.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...mit dem Verhältnis von Angebot und Nachfrage der Endprodukte, die mit den von ANDRITZ gelieferten Anlagen und Produkten hergestellt werden. Mögliche Preisschwankungen können daher einen direkten Einfluss auf die Investitionsentscheidungen von Kunden und in weiterer Folge auf den Auftragseingang der Gruppe haben. Dies könnte daher zu einer Volatilität in der Entwicklung des Auftragseingangs führen. Der künftige Erfolg der Gruppe hängt unter anderem davon ab, ob neue Aufträge in ausreichendem Umfang erhalten werden können. Es ist teilweise schwierig vorherzusagen, wann genau ein Auftrag, für den die Grupp...


### AND-012 | PDF-Seite 26 | hauptrisiken / Finanzierung

**Aussage:** Fehlende Verfügbarkeit geeigneter Akquisitionsziele oder mangelnde Finanzierungsmittel für M&A-Vorhaben

**Zitat:** „Es kann jedoch nicht garantiert werden, dass die Gruppe auch künftig in der Lage sein wird, geeignete Akquisitionsziele zu identifizieren und zu erwerben, dass überhaupt geeignete Unternehmen zur Verfügung stehen und ausreichend Finanzmittel für große Akquisitionen aufgebracht werden können.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...ng dieser Strategie akquirierte die Gruppe seit 1990 eine Vielzahl von weltweit tätigen Unternehmen und gliederte diese in den Konzern ein. Es kann jedoch nicht garantiert werden, dass die Gruppe auch künftig in der Lage sein wird, geeignete Akquisitionsziele zu identifizieren und zu erwerben, dass überhaupt geeignete Unternehmen zur Verfügung stehen und ausreichend Finanzmittel für große Akquisitionen aufgebracht werden können. ANDRITZ war bei der Integration neuer Unternehmen bisher weitestgehend erfolgreich. Es kann jedoch nicht garantiert werden, dass die angestrebten Ziele und Synergien bei allen zukünftigen Akquisitionen (wie au...


### AND-013 | PDF-Seite 26 | strategische_prioritaeten

**Aussage:** Erreichen der Position eines Komplettanbieters in allen Geschäftsbereichen durch organisches Wachstum und komplementäre Zukäufe

**Zitat:** „Eines der wesentlichen strategischen Ziele der ANDRITZ -Gruppe besteht darin, durch organisches Wachstum und komplementäre Akquisitionen in allen Geschäftsbereichen zum Komplettanbieter zu werden.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ... vieler Länder stellt mittel - bis langfristig ebenfalls ein Risiko dar. f) Akquisition und Integration von komplementären Geschäftsfeldern Eines der wesentlichen strategischen Ziele der ANDRITZ -Gruppe besteht darin, durch organisches Wachstum und komplementäre Akquisitionen in allen Geschäftsbereichen zum Komplettanbieter zu werden. In Umsetzung dieser Strategie akquirierte die Gruppe seit 1990 eine Vielzahl von weltweit tätigen Unternehmen und gliederte diese in den Konzern ein. Es kann jedoch nicht garantiert werden, dass die Gruppe auc...


### AND-014 | PDF-Seite 27 | hauptrisiken / Technologie

**Aussage:** Risiko langsamer Produktentwicklung im Bereich Digitalisierung sowie Cyberangriffe

**Zitat:** „Die rasanten Entwicklungen im Bereich der Digitalisierung stellen jedoch auch ein Risiko dar, falls es ANDRITZ nicht gelingen sollte, die am Markt nachgefragten Produkte und Lösungen in der gebotenen Geschwindigkeit zu entwickeln und anzubieten.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ... liegt dabei auf Cybersicherheit, der Verwendung von Künstlicher Intelligenz (KI) sowie auf den neuesten am Markt verfügbaren Technologien. Die rasanten Entwicklungen im Bereich der Digitalisierung stellen jedoch auch ein Risiko dar, falls es ANDRITZ nicht gelingen sollte, die am Markt nachgefragten Produkte und Lösungen in der gebotenen Geschwindigkeit zu entwickeln und anzubieten. Darüber hinaus kann die Erhöhung des Digitalisierungsgrads zu einem größeren Risiko von Cyberangriffen auf ANDRITZ und auf Kunden führen. Um dieses Risiko zu minimieren, wendet ANDRITZ die Cybersicherheit -Sta...


### AND-015 | PDF-Seite 27 | strategische_prioritaeten

**Aussage:** Fokus auf Entwicklung digitaler Produkte und Lösungen mit Schwerpunkt Cybersicherheit, KI und neue Technologien

**Zitat:** „ANDRITZ sieht in der Digitalisierung ein wesentliches Wachstumsfeld für die Zukunft und wird daher weiterhin stark auf die Entwicklung digitaler Produkte und Lösungen fokussiert sein. Das Hauptaugenmerk liegt dabei auf Cybersicherheit, der Verwendung von Künstlicher Intelligenz“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...n stets dem neuesten Stand der Technik, werden laufend weiterentwickelt und können auf individuelle Kundenbedürfnisse zugeschnitten werden. ANDRITZ sieht in der Digitalisierung ein wesentliches Wachstumsfeld für die Zukunft und wird daher weiterhin stark auf die Entwicklung digitaler Produkte und Lösungen fokussiert sein. Das Hauptaugenmerk liegt dabei auf Cybersicherheit, der Verwendung von Künstlicher Intelligenz (KI) sowie auf den neuesten am Markt verfügbaren Technologien. Die rasanten Entwicklungen im Bereich der Digitalisierung stellen jedoch auch ein Risiko dar, falls es ANDRITZ nicht gelingen sollte, die am Markt...


### AND-016 | PDF-Seite 28 | hauptrisiken / Lieferkette

**Aussage:** Ausfälle von Lieferanten aufgrund geopolitischer Krisen, Konflikte oder Naturkatastrophen

**Zitat:** „Globale und regionale Krisen, politische bzw. wirtschaftliche Konflikte oder Naturkatastrophen können dazu führen, dass Lieferanten nicht in der Lage sind, von ANDRITZ bestellte Produkte rechtzeitig zu fertigen und zu liefern“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...bleibt die ANDRITZ -Gruppe vollumfänglich handlungsfähig und kann die Einhaltung rechtlicher und gesellschaftlicher Vorgaben sicherstellen. Globale und regionale Krisen, politische bzw. wirtschaftliche Konflikte oder Naturkatastrophen können dazu führen, dass Lieferanten nicht in der Lage sind, von ANDRITZ bestellte Produkte rechtzeitig zu fertigen und zu liefern, was wiederum zur Folge haben könnte, dass ANDRITZ den Verpflichtungen gegenüber seinen Kunden nicht zeitgerecht nachkommen kann. Der Krieg in der Ukraine und die daraus resultierenden Sanktionen gegenüber Rus...


### AND-017 | PDF-Seite 30 | hauptrisiken / Finanzierung

**Aussage:** Währungs- und Wechselkursrisiken durch Auftragsabwicklung in Fremdwährungen

**Zitat:** „Obwohl die Gruppe bestrebt ist, die Nettowährungsposition von nicht in der jeweiligen funktionalen Währung der Konzerngesellschaft abgeschlossenen Aufträge durch den Abschluss von Termingeschäften abzusichern, können sich Währungsschwankungen mit Wechselkursverlusten im Konzernabschluss niederschlagen.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...en, werden durch die Verwendung von derivativen Finanzinstrumenten – insbesondere Devisentermingeschäfte und Swaps – bestmöglich minimiert. Obwohl die Gruppe bestrebt ist, die Nettowährungsposition von nicht in der jeweiligen funktionalen Währung der Konzerngesellschaft abgeschlossenen Aufträge durch den Abschluss von Termingeschäften abzusichern, können sich Währungsschwankungen mit Wechselkursverlusten im Konzernabschluss niederschlagen. Die Entwicklung der Wechselkurse kann sich auch auf den in Euro umgerech neten Umsatz und das Ergebnis der Gruppe sowohl positiv als auch negativ auswirken. Wechselkursänderungen können auch dazu führen, dass ...


### AND-018 | PDF-Seite 34 | capex_ma_signale

**Aussage:** Investitionen in eine neue Dry Molded Fiber (DMF) Pilotanlage am Standort Montbonnot in Frankreich

**Zitat:** „ANDRITZ forciert seinen Eintritt in die Dry Molded Fiber (DMF) Technologie durch Investitionen in eine neue DMF Pilotanlage am Standort in Montbonnot in Frankreich.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...ertigen EPC Projekten. Damit bedient das Unternehmen sowohl den Markt für textile Garne als auch den Markt für Fasern im Vliesstoffbereich. ANDRITZ forciert seinen Eintritt in die Dry Molded Fiber (DMF) Technologie durch Investitionen in eine neue DMF Pilotanlage am Standort in Montbonnot in Frankreich. Die Anlage ist mit mehreren Innovationen ausgestattet, um nächste Generationen von Lösungen zu entwickeln, die Kunststoff in der Verpackungsindustrie ersetzen können. Zudem nutzt ANDRITZ seine Zellstoff Expert...


### AND-019 | PDF-Seite 37 | strategische_prioritaeten

**Aussage:** Ausrichtung der F&E auf Netzstabilität, Systemflexibilität und Dekarbonisierung

**Zitat:** „Die Forschungs - und Entwicklungsaktivitäten richten sich konsequent auf die zukünftigen Anforderungen an Netzstabilität und Systemflexibilität aus. Die Entwicklungen orientieren sich nicht nur am heutigen Markt, sondern antizipieren die technischen Herausforderungen einer vollständig dekarbonisierten Energieversorgung.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...euerungs - und Überwachungsfunktionen in einem einheitlichen System, das speziell für die Anforderungen der Netzstabilität optimiert wurde. Die Forschungs - und Entwicklungsaktivitäten richten sich konsequent auf die zukünftigen Anforderungen an Netzstabilität und Systemflexibilität aus. Die Entwicklungen orientieren sich nicht nur am heutigen Markt, sondern antizipieren die technischen Herausforderungen einer vollständig dekarbonisierten Energieversorgung. Durch kontinuierliche Verbesserung von Wirkungsgraden, Regelgeschwindigkeiten und Systemintegration wird die technologische Basis geschaffen, damit die Kunden ihre Nachhaltigkeitsziele erreichen und gleichzeit...


### AND-020 | PDF-Seite 40 | wachstumsmaerkte / China

**Aussage:** Im Bereich Metals Forming werden strukturelle Herausforderungen im Automobilsektor unter anderem durch Wachstum in China abgefedert.

**Zitat:** „Im Bereich Metals Forming werden strukturelle Herausforderungen im Automobilsektor durch relativ stabile Nachfrage nach Nicht‑Automobil ‑Anwendungen sowie durch Wachstum in China abgefedert.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...erungen, Modifikationen und Nachhaltigkeitsverbesserungen bestehender Kapazitäten wird voraussichtlich zufriedenstellend bleiben. ▪ Metals: Im Bereich Metals Forming werden strukturelle Herausforderungen im Automobilsektor durch relativ stabile Nachfrage nach Nicht‑Automobil ‑Anwendungen sowie durch Wachstum in China abgefedert. Im Bereich Metals Processing wird f ür 2026 ein weiterhin robustes Marktumfeld erwartet. ▪ Hydropower: Im Geschäftsbereich Hydropower wird mit einem weiteren Anstieg der Projekt ‑ und Sanierungs - aktivitäten,...


### AND-021 | PDF-Seite 41 | hauptrisiken / Markt

**Aussage:** Verschlechterung des makroökonomischen und geopolitischen Umfelds sowie Zunahme globaler Handelsbarrieren

**Zitat:** „Sollte sich das makroökonomische und geopolitische Umfeld deutlich verschlechtern, globale Handelsbarrieren weiter zunehmen oder der Euro weiter deutlich aufwerten, könnten sich negative Auswirkungen auf die Abwicklung und den Eingang von Aufträgen ergeben“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...2026 strebt die ANDRITZ - Gruppe eine vergleichbare EBITA -Marge (exkl. nicht-operativer Effekte) in einer Bandbreite von 8,7% bis 9,1% an. Sollte sich das makroökonomische und geopolitische Umfeld deutlich verschlechtern, globale Handelsbarrieren weiter zunehmen oder der Euro weiter deutlich aufwerten, könnten sich negative Auswirkungen auf die Abwicklung und den Eingang von Aufträgen ergeben , was die finanzielle Entwicklung von ANDRITZ negativ beeinflussen könnte. In diesem Fall könnten zusätzliche Kapazitätsanpassungen über die derzeitigen Maßnahmen hinaus erforderlich werden, welche finanzielle...


### AND-022 | PDF-Seite 46 | capex_ma_signale  **PRUEFEN**

**Aussage:** Im Geschäftsjahr 2025 betrugen die Auszahlungen für Sachanlagen und immaterielle Vermögenswerte 198,1 MEUR und der Netto-Cashflow aus Unternehmenserwerben 328,6 MEUR.

**Zitat:** „Auszahlungen für Sachanlagen und immaterielle Vermögenswerte -198,1 -179,5 Einzahlungen aus dem Verkauf von Sachanlagen und immateriellen Vermögenswerten 27,4 16,5 Auszahlungen für lang- und kurzfristige finanzielle Vermögenswerte -562,4 -362,3 Einzahlungen aus dem Verkauf von lang- und kurzfristigen finanziellen Vermögenswerten 520,1 354,7 Netto-Cashflow aus Unternehmenserwerben -328,6 -36,9“

**Treffertyp:** `teilweise`

**Umgebung im Bericht:**

> ...e Zinsen -36,3 -38,9 Erhaltene Dividenden 1,3 2,3 Gezahlte Ertragsteuern -149,8 -152,3 CASHFLOW AUS BETRIEBLICHER TÄTIGKEIT 39. 652,7 636,5 Auszahlungen für Sachanlagen und immaterielle Vermögenswerte -198,1 -179,5 Einzahlungen aus dem Verkauf von Sachanlagen und immateriellen Vermögenswerten 27,4 16,5 Auszahlungen für lang- und kurzfristige finanzielle Vermögenswerte -562,4 -362,3 Einzahlungen aus dem Verkauf von lang- und kurzfristigen finanziellen Vermögenswerten 520,1 354,7 Netto-Cashflow aus Unternehmenserwerben 39. -328,6 -36,9 CASHFLOW AUS INVESTITIONSTÄTIGKEIT 39. -541,6 -207,5 Einzahlungen aus Bank- und sonstigen Finanzverbindlichkeiten 39. 241,4 161,4 Auszahlungen für Bank- und sonstige Finanzverbindlichkeiten 39. -265,9 -493...


### AND-023 | PDF-Seite 82 | capex_ma_signale

**Aussage:** Die vertraglichen Verpflichtungen für den Erwerb von Sachanlagen beliefen sich zum 31. Dezember 2025 auf 53,0 MEUR.

**Zitat:** „Vertragliche Verpflichtungen für den Kauf von Sachanlagen sind nur im gewöhnlichen Geschäftsumfang vorhanden. Zum 31. Dezember 2025 betrugen diese Verpflichtungen 53,0 MEUR (31. Dezember 2024: 22,1 MEUR).“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...ten Sachanlagen in Höhe von 1,8 MEUR wurden zum 31. Dezember 2025 als Sicherheiten gestellt (31. Dezember 2024: 1,9 MEUR). b) Bestellobligo Vertragliche Verpflichtungen für den Kauf von Sachanlagen sind nur im gewöhnlichen Geschäftsumfang vorhanden. Zum 31. Dezember 2025 betrugen diese Verpflichtungen 53,0 MEUR (31. Dezember 2024: 22,1 MEUR). c) Fremdkapitalkosten Weder im Geschäftsjahr 2025 noch im Geschäftsjahr 2024 wurden Fremdkapitalkosten auf qualifizierte Vermögenswerte aktiviert, weil die zu aktivierenden Beträge unwesentlich waren. d) Zuwen...


### AND-024 | PDF-Seite 89 | capex_ma_signale

**Aussage:** Closing der Akquisition von Sanzheng im Dezember 2025

**Zitat:** „Das Closing der Akquisition Sanzheng fand im Dezember 2025 nach dem jährlichen Werthaltigkeitstest zum 30. September 2025 statt. Diese ZGE wurde zum 31. Dezember 2025 getestet.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...ndern Pulp & Paper: Pulp and Power PP 29,3 12,80 2,13 Lieferung gesamter Zellstofffabriken und der damit verbundenen Technologien 1.130,3 * D as Closing der Akquisition Sanzheng fand im Dezember 2025 nach dem jährlichen Werthaltigkeitstest zum 30. September 2025 statt. Diese ZGE wurde zum 31. Dezember 2025 getestet. 2024 ZGE Geschäfts- bereich Geschäfts- oder Firmenwert Diskon- tierungssatz vor Steuern Langfristige Wachstums- rate Beschreibung (in MEUR) (in %) (in %) Pulp & Paper: Service PP 283,4 11,70 2,24 Markenunabhä...


### AND-025 | PDF-Seite 90 | hauptrisiken / Regulierung

**Aussage:** Risiken des Klimawandels (physische Risiken sowie Übergangsrisiken)

**Zitat:** „Zu den Risiken des Klimawandels für die ANDRITZ -Gruppe zählen einerseits physische Risiken sowie auch Übergangsrisiken. Diesen Risiken begegnet ANDRITZ durch ein breites Produktportfolio im Bereich der „nachhaltigen Technologien“.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...t -Ebene bzw. nach regionalen Gesichtspunkten anhand der besten Schätzungen bezüglich künftiger Entwicklungen nach Relevanz berücksichtigt. Zu den Risiken des Klimawandels für die ANDRITZ -Gruppe zählen einerseits physische Risiken sowie auch Übergangsrisiken. Diesen Risiken begegnet ANDRITZ durch ein breites Produktportfolio im Bereich der „nachhaltigen Technologien“. Das Unternehmen generiert bereits heute rund 45% seines Gesamtumsatzes aus Produkten und Lösungen, die zur Herstellung von erneuerbarer Energie, zu Umweltschutz, Kreislaufwirtschaft und E -Mobilität beitragen....


### AND-026 | PDF-Seite 90 | strategische_prioritaeten

**Aussage:** Steigerung des Anteils nachhaltiger Technologien am Gesamtumsatz durch neue Produkte wie Green Hydrogen und Carbon Storage

**Zitat:** „Dieser Anteil soll künftig durch neue Produkte (zB Green Hydrogen und Carb on Storage) noch gesteigert werden. Aktuell sehen wir auf der Produktseite keine wesentlichen Risiken, da unsere Produkte unseren Kunden helfen ihre Klimaziele zu erreichen.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ... aus Produkten und Lösungen, die zur Herstellung von erneuerbarer Energie, zu Umweltschutz, Kreislaufwirtschaft und E -Mobilität beitragen. Dieser Anteil soll künftig durch neue Produkte (zB Green Hydrogen und Carb on Storage) noch gesteigert werden. Aktuell sehen wir auf der Produktseite keine wesentlichen Risiken, da unsere Produkte unseren Kunden helfen ihre Klimaziele zu erreichen. In den zukünftigen Cashflows sind erwartete Kostenvolatilitäten bzw. -steigerungen und die entsprechenden Möglichkeiten (u.a. Anpassungen der Verkaufspreise sowie Preisgleitklauseln), diese Steigerungen an Kun...


### AND-027 | PDF-Seite 129 | hauptrisiken / Finanzierung

**Aussage:** Risiken aus Finanzinstrumenten sowie strategische und operative Risiken

**Zitat:** „Als global tätiges Unternehmen, das verschiedenste Märkte und Kunden bedient, ist die Gruppe Risiken in Verbindung mit Finanzinstrumenten sowie strategischen und operativen Risiken ausgesetzt.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ... I T Z- F i n a n z b e r i c h t 2 0 2 5 K o n z e r n a n h a n g 128 38. Risikomanagement – Risiken in Verbindung mit Finanzinstrumenten Als global tätiges Unternehmen, das verschiedenste Märkte und Kunden bedient, ist die Gruppe Risiken in Verbindung mit Finanzinstrumenten sowie strategischen und operativen Risiken ausgesetzt. ANDRITZ hat ein bewährtes, konzernweites Kontroll - und Risikomanagementsystem implementiert, dessen Hauptaufgabe es ist, entstehende Risiken bereits in einem frühen Stadium zu identifizieren und rasch Gegenma...


### AND-028 | PDF-Seite 131 | hauptrisiken / Finanzierung

**Aussage:** Kredit- und Ausfallrisiko einzelner Kontrahenten

**Zitat:** „Das Risiko eines möglichen Ausfalls (Insolvenz) einzelner oder mehrerer Kontrahenten wird durch ein internes Kontrahentenlimitsystem minimiert.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...er Ausweis der Wertberichtigung. Für Veränderungen nach dem Zugang ist eine gesonderte Risikovorsorge notwendig. Risikominderungsstrategien Das Risiko eines möglichen Ausfalls (Insolvenz) einzelner oder mehrerer Kontrahenten wird durch ein internes Kontrahentenlimitsystem minimiert. Dabei wird unter Berücksichtigung der jeweiligen Bonität des Kontrahenten (Ratings von internationalen Rating -Agenturen wie Moody’s, Standard & Poor’s, Fitch) und der publizierten Credit Default Swap -Spreads...


### AND-029 | PDF-Seite 135 | hauptrisiken / Finanzierung

**Aussage:** Zahlungsausfallrisiken bei Kundenprojekten

**Zitat:** „Es kann jedoch nicht ausgeschlossen werden, dass es einzelne Zahlungsausfälle gibt, die im Eintrittsfall einen wesentlichen negativen Einfluss auf die Ergebnis - und Liquiditätsentwicklung der Gruppe haben.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...allrisiko von Kunden bestmöglich durch Besicherung von Zahlungen durch Banken sowie durch Abschluss von Exportversicherungen zu reduzieren. Es kann jedoch nicht ausgeschlossen werden, dass es einzelne Zahlungsausfälle gibt, die im Eintrittsfall einen wesentlichen negativen Einfluss auf die Ergebnis - und Liquiditätsentwicklung der Gruppe haben. — Mehr Informationen in Kapitel 3 8. a) Ausfallrisiken. Die ANDRITZ-Gruppe ist hinsichtlich Liquidität sehr gut positioniert und verfügt über hohe Liquiditätsreserven. Die Gruppe vermeidet es, von einer einzig...


### AND-030 | PDF-Seite 136 | hauptrisiken / Markt

**Aussage:** Marktrisiken durch Zins- und Währungsschwankungen

**Zitat:** „Das Marktrisiko umfasst das Risiko, dass sich die Marktpreise, zum Beispiel Währungskurse, Zinssätze oder Aktienkurse, ändern und dadurch die Erträge des Konzerns oder der Wert der gehaltenen Finanzinstrumente beeinflusst werden.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...74,9 Derivative finanzielle Schulden 74,3 51,9 14,9 4,7 3,0 0,4 0,0 74,9 1.902,7 1.360,9 217,5 197,0 81,5 20,6 76,6 1.954,1 c) Marktrisiken Das Marktrisiko umfasst das Risiko, dass sich die Marktpreise, zum Beispiel Währungskurse, Zinssätze oder Aktienkurse, ändern und dadurch die Erträge des Konzerns oder der Wert der gehaltenen Finanzinstrumente beeinflusst werden. Ziel des Marktrisikomanagements ist es, das Marktrisiko innerhalb akzeptabler Bandbreiten zu steuern und zu kontrollieren und gleichzeitig die Rendite zu optimieren. Zu den für die ANDRITZ -Gruppe wesentlichen...


### AND-031 | PDF-Seite 142 | capex_ma_signale

**Aussage:** Im Geschäftsbereich Metals leitete Andritz 2025 den Verkauf von Sachanlagen in Deutschland mit einem Buchwert von 4,0 MEUR ein, dessen Abschluss für 2026 erwartet wird.

**Zitat:** „Im Geschäftsbereich Metals wurde 2025 der Verkauf von Sachanlagen (Grundstücke, Gebäude und technische n Anlagen) in Deutschland eingeleitet. Es wurden 2025 Vermögenswerte von 4,0 MEUR als zur Veräußerung gehalten angesetzt“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ... Immaterielle Vermögenswerte außer Geschäfts- oder Firmenwerte 0,0 0,0 Sachanlagen 4,0 8,2 ZUR VERÄUßERUNG GEHALTENE VERMÖGENSWERTE 4,0 8,2 Im Geschäftsbereich Metals wurde 2025 der Verkauf von Sachanlagen (Grundstücke, Gebäude und technische n Anlagen) in Deutschland eingeleitet. Es wurden 2025 Vermögenswerte von 4,0 MEUR als zur Veräußerung gehalten angesetzt und keine Wertminderungsaufwendungen erfasst. Der Verkauf der Sachanlagen wird voraussichtlich 2026 abgeschlossen sein.


### AND-032 | PDF-Seite 143 | capex_ma_signale

**Aussage:** Ein Ende 2024 im Geschäftsbereich Metals eingeleiteter Verkauf von Sachanlagen in Deutschland wurde 2025 mit einem Veräußerungsgewinn von 2,8 MEUR vollzogen.

**Zitat:** „Es wurden 2024 Vermögenswerte von 7,7 MEUR als zur Veräußerung gehalten angesetzt und keine Wertminderungsaufwendungen erfasst. Der Verkauf der Sachanlagen wurde 2025 mit einem Veräußerungsgewinn von 2,8 MEUR abgeschlossen .“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...n h a n g 142 Im Geschäftsbereich Metals wurde Ende 202 4 der Verkauf von Sachanlagen (Grundstücke und Gebäude) in Deutschland eingeleitet. Es wurden 2024 Vermögenswerte von 7,7 MEUR als zur Veräußerung gehalten angesetzt und keine Wertminderungsaufwendungen erfasst. Der Verkauf der Sachanlagen wurde 2025 mit einem Veräußerungsgewinn von 2,8 MEUR abgeschlossen . Im Geschäftsbereich Pulp & Paper w urden Ende 2024 Sachanlagen in Kanada in der Höhe von 0,5 MEUR als zur Veräußerung gehalten ausgewiesen. Aus der vorgelagerten Bewertung wurde keine Wertminderung erfasst. 20...


### AND-033 | PDF-Seite 143 | capex_ma_signale

**Aussage:** Im Geschäftsbereich Pulp & Paper wurden 2025 Sachanlagen in Kanada mit einem Veräußerungsgewinn von 0,8 MEUR veräußert.

**Zitat:** „Im Geschäftsbereich Pulp & Paper w urden Ende 2024 Sachanlagen in Kanada in der Höhe von 0,5 MEUR als zur Veräußerung gehalten ausgewiesen. Aus der vorgelagerten Bewertung wurde keine Wertminderung erfasst.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ... keine Wertminderungsaufwendungen erfasst. Der Verkauf der Sachanlagen wurde 2025 mit einem Veräußerungsgewinn von 2,8 MEUR abgeschlossen . Im Geschäftsbereich Pulp & Paper w urden Ende 2024 Sachanlagen in Kanada in der Höhe von 0,5 MEUR als zur Veräußerung gehalten ausgewiesen. Aus der vorgelagerten Bewertung wurde keine Wertminderung erfasst. 2025 wurden die Anlagen mit einem Veräußerungsgewinn von 0,8 MEUR veräußert. VERWENDUNG VON ERMESSENSENTSCHEIDUNGEN UND SCHÄTZUNGEN Bei der Bestimmung des beizulegenden Zeitwerts, abzüglich Veräußerungskosten,...


---

# voestalpine AG  (voestalpine_2025_26.pdf, 65 Elemente)


### VOE-034 | PDF-Seite 60 | hauptrisiken / Markt

**Aussage:** Intensiver globaler Wettbewerb und Preisdruck

**Zitat:** „Dieser Bereich verzeichnete über das gesamte Geschäftsjahr 2025/26 hinweg einen intensiven globalen Wettbewerb und damit einhergehenden Preisdruck.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...arktsegment Tooling umfasst Lieferungen von Werkzeugstahl und stellt sowohl mengen- als auch wertmäßig das größte Segment der Division dar. Dieser Bereich verzeichnete über das gesamte Geschäftsjahr 2025/26 hinweg einen intensiven globalen Wettbewerb und damit einhergehenden Preisdruck. Die Division legte ihren Fokus daher noch weiter verstärkt auf Produktsegmente im obers ten Qualitätsspektrum sowie auf Wertschöpfungs- und Service-Aktivitäten, wie beispielsweise Wärme- und Oberflächenbehandl...


### VOE-035 | PDF-Seite 60 | strategische_prioritaeten

**Aussage:** Fokus auf Spitzenqualität und Service-Aktivitäten

**Zitat:** „Die Division legte ihren Fokus daher noch weiter verstärkt auf Produktsegmente im obersten Qualitätsspektrum sowie auf Wertschöpfungs- und Service-Aktivitäten, wie beispielsweise Wärme- und Oberflächenbehandlungen.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...ereich verzeichnete über das gesamte Geschäftsjahr 2025/26 hinweg einen intensiven globalen Wettbewerb und damit einhergehenden Preisdruck. Die Division legte ihren Fokus daher noch weiter verstärkt auf Produktsegmente im obers ten Qualitätsspektrum sowie auf Wertschöpfungs- und Service-Aktivitäten, wie beispielsweise Wärme- und Oberflächenbehandlungen. Während die Nachfrage in Europa über das gesamte Geschäftsjahr 2025/26 hinweg stabil, jedoch gedämpft blieb, war die Geschäftsentwicklung in Nordamerika nicht zuletzt aufgrund der US-Zölle von vorsichtigem Be...


### VOE-036 | PDF-Seite 65 | hauptrisiken / Regulierung

**Aussage:** US-Handelszölle und regulatorische Handelsmaßnahmen

**Zitat:** „Seit Juni 2025 erschweren erhöhte Importzölle auf Stahlprodukte die Absatzmöglichkeiten in den USA erheblich.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...u. Das Produktsegment Tubulars (Nahtlosrohre) war im Geschäftsjahr 2025/26 von den tiefgreifenden Auswirkungen der US-Handelszölle geprägt. Seit Juni 2025 erschweren erhöhte Importzölle auf Stahl- produkte die Absatzmöglichkeiten in den USA erheblich. Diese Maßnahmen erforderten eine schritt- weise Rücknahme der Produktionskapazitäten in Verbindung mit Einsparungsprogrammen sowie einer bereits längerfristig vorbereiteten regionalen Diversifizierung in Ric...


### VOE-037 | PDF-Seite 65 | strategische_prioritaeten

**Aussage:** Regionale Diversifizierung im Bereich Nahtlosrohre

**Zitat:** „Diese Maßnahmen erforderten eine schrittweise Rücknahme der Produktionskapazitäten in Verbindung mit Einsparungsprogrammen sowie einer bereits längerfristig vorbereiteten regionalen Diversifizierung in Richtung MENA.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...er US-Handelszölle geprägt. Seit Juni 2025 erschweren erhöhte Importzölle auf Stahl- produkte die Absatzmöglichkeiten in den USA erheblich. Diese Maßnahmen erforderten eine schritt- weise Rücknahme der Produktionskapazitäten in Verbindung mit Einsparungsprogrammen sowie einer bereits längerfristig vorbereiteten regionalen Diversifizierung in Richtung MENA. Das Produktsegment Wire (Draht) war über das gesamte Geschäftsjahr 2025/26 hinweg mit einer ver- haltenen Marktstimmung in den Kernbranchen Automobil, Bau und Maschinenbau konfrontiert. Ledig- lich Spezialan...


### VOE-038 | PDF-Seite 72 | strategische_prioritaeten

**Aussage:** Klimafreundliche Stahlerzeugung durch das Transformationsprojekt greentec steel

**Zitat:** „An den österreichischen Stahlstandorten Linz und Donawitz lag der Fokus der Investitionstätigkeit auf der Umsetzung des Transformationsprojektes greentec steel.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...Wachstumsvorhaben in Verarbeitungs- bereichen. An internationalen Standorten wurden zahlreiche Projekte gestartet oder bereits umge- setzt. An den österreichischen Stahlstandorten Linz und Donawitz lag der Fokus der Investitionstätig- keit auf der Umsetzung des Transformationsprojektes greentec steel. Darüber hinaus wurde mit dem offiziellen Spatenstich für die Demonstrationsanlage Hy4Smelt im Herbst 2025 gemeinsam mit inter- nationalen Partner:innen ein weiteres Entwicklungsprojekt im Bereich der klimafr...


### VOE-039 | PDF-Seite 74 | capex_ma_signale

**Aussage:** Investitionen in Höhe von rund 70 Mio. EUR zur Kapazitätserweiterung am Standort Jeffersonville.

**Zitat:** „Das Investitionsvolumen für die zusätzlichen Profilier- und Weiterverarbeitungsanlagen beläuft sich auf rund 70 Mio. EUR.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...erfolgte bereits gegen Ende des Geschäftsjahres 2025/26. Im Endausbau ist eine Verdoppelung des Leistungspotenzials des Standortes geplant. Das Investitionsvolumen für die zusätzlichen Profilier- und Weiterverarbeitungsanlagen beläuft sich auf rund 70 Mio. EUR. Darüber hinaus in vestierte der brasilianische Standort Meincol in Caxias do Sul in die Erweiterung der Ferti- gungskapazitäten. Der Projektabschluss ist für das Geschäftsjahr 2026/27 vorgesehen. In Belgien st...


### VOE-040 | PDF-Seite 74 | wachstumsmaerkte / Nordamerika

**Aussage:** Die Rollforming Corporation baut am Standort Jeffersonville die Produktionskapazitäten aus und plant eine Verdoppelung des Leistungspotenzials.

**Zitat:** „Am Standort Jeffersonville, USA, trieb die nordamerikanische Gesellschaft Rollforming Corporation die Erweiterung der Produktionskapazitäten weiter voran.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...elektive Ersatzinvestitionen. Der Geschäftsbereich Tubes & Sections stellt hingegen einen strategischen Wachstumsbereich der Division dar . Am Standort Jeffersonville, USA, trieb die nordamerikanische Gesellschaft Rollforming Corporation die Erweiterung der Produktionskapazitäten weiter voran. Der Hochlauf für die erste Expansionss tufe erfolgte bereits gegen Ende des Geschäftsjahres 2025/26. Im Endausbau ist eine Verdoppelung des Leistungspotenzials des Standortes geplant. Das Investitionsvolumen f...


### VOE-041 | PDF-Seite 75 | capex_ma_signale

**Aussage:** Akquisition von 100 % der Anteile an HIRD Rail Services Limited im Bereich Railway Systems.

**Zitat:** „Im Juli 2025 erwarb der Geschäftsbereich Railway Systems 100 % der Anteile an der Gesellschaft HIRD Rail Services Limited mit Sitz in Doncaster, Großbritannien.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...tion im Ber eich Railway Systems auch Devestitionen in der Steel Division sowie der High Performance Metals Division erfolgreich umgesetzt. Im Juli 2025 erwarb der Geschäftsbereich Railway Systems 100 % der Anteile an der Gesellschaft HIRD Rail Services Limited mit Sitz in Doncaster, Großbritannien. Das britische Unternehmen ist Hersteller von hochwertigen Isolierstößen für die lokale Eisenbahninfrastruktur. Die Übernahme stärkt die stra- tegische Position auf dem britischen Markt im sicherheitskritischen...


### VOE-042 | PDF-Seite 75 | capex_ma_signale

**Aussage:** Verkauf von voestalpine BÖHLER Profil an Kadant Inc.

**Zitat:** „Im Rahmen der Neuorganisation der High Performance Metals Division beschloss das Management der Division aus strategischen Gründen den Verkauf von voestalpine BÖHLER Profil.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...industrie. Zuletzt waren hier 47 Mitarbeiter:innen beschäftigt, die im Geschäftsjahr 2024/25 einen Umsatz von 14 Mio. EUR erwirtschafteten. Im Rahmen der Neuorganisation der High Performance Metals Division beschloss das Management der Division aus strategischen Gründen den Verkauf von voestalpine BÖHLER Profil. Ende Januar 2026 erfolgte der Vertragsabschluss mit dem Erwerber Kadant Inc. voestalpine BÖHLER Profil in Bruckbach, Österreich, liefert Spezialprofile in unterschiedliche Industriefelder und ist darüber hinau...


### VOE-043 | PDF-Seite 75 | capex_ma_signale

**Aussage:** Verkauf der voestalpine Camtec Gruppe durch die Steel Division.

**Zitat:** „Im August 2025 veräußerte die Steel Division die voestalpine Camtec Gruppe.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...In der Steel Division und in der High Performance Metals Division kam es im abgelaufenen Geschäfts- jahr 2025/26 zu Portfoliobereinigungen. Im August 2025 veräußerte die Steel Division die voestalpine Camtec Gruppe. Diese ist auf die Herstellung von Schiebern und wartungsfreien Gleitelementen aus Messing, Kupfer und Aluminium spezialisiert und beliefert vor allem die Automobil- und Automobil - zulie fer- sowie die Maschin...


### VOE-044 | PDF-Seite 86 | hauptrisiken / Markt

**Aussage:** Handelspolitisch motivierte Markteingriffe, insbesondere US-Zölle auf Stahlprodukte

**Zitat:** „Neben geopolitischen Konflikten beeinflussen auch handelspolitisch motivierte Eingriffe in Märkte – etwa in Form von Zöllen und Gegenzöllen bzw. Sanktionen – das Wirtschaftswachstum. So war der voestalpine-Konzern von US-Zöllen auf Stahlimporte beim Export aus dem EU-Raum in die USA betroffen“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...ran-Krieges bestehende Vorkehrungen zur Versorgungssicherheit lau- fend auf ihre Wirksamkeit geprüft und bei Bedarf entsprechend angepasst. Neben geopolitischen Konflikten beeinflussen auch handelspolitisch motivierte Eingriffe in Märkte – etwa in Form von Zöllen und Gegenzöllen bzw. Sanktionen – das Wirtschaftswachstum. So war der voestalpine-Konzern von US-Zöllen auf Stahlimporte beim Export aus dem EU-Raum in die USA be- troffen (Erhöhung der Section 232-Zölle für Stahl von 25 % auf 50 % und der zusätzlichen Einführung der reziproken Zölle (IEEPA-Zölle) von 15 % auf Produkte aus Stahl). Im abgelaufenen Geschäftsjahr belief sich der ...


### VOE-045 | PDF-Seite 92 | hauptrisiken / Technologie

**Aussage:** Projektrisiken, insbesondere Hochlauf- und Kostensteigerungsrisiken bei Großprojekten

**Zitat:** „Etwaigen Risiken aus Projekten (wie z. B. aus Großprojekten, aus Investitionen) wird durch den Einsatz unterschiedlichster Projektmanagement-Tools sowie durch ein entsprechendes Projekt-Monitoring – und je nach Größe des Projektes auch durch regelmäßige Projektaufsichtssitzungen unter Einbindung des Top-Managements – entgegengewirkt.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...etaillierte Prozessdokumentationen, insbesondere auch im IT-gestützten Bereich, tragen ebenfalls zur Sicherung des vorhandenen Wissens bei. Etwaigen Risiken aus Projekten (wie z. B. aus Großprojekten, aus Investitionen) wird durch den Einsatz unterschiedlichster Projektmanagement-Tools sowie durch ein entsprechendes Projekt-Monitoring – und je nach Größe des Projektes auch durch regelmäßige Projektaufsichtssitzungen unter Einbin- dung des Top-Managements – entgegengewirkt. Dies betrifft insbesondere auch etwaige Hochlauf- bzw. Kostensteigerungsrisiken. Erkenntnisse aus früheren Aktivitäten werden im Sinne von „Lessons Learned“ gesammelt und bilden die Basis der kontinuierliche...


### VOE-046 | PDF-Seite 93 | hauptrisiken / Regulierung

**Aussage:** Belastung des Standorts Europa durch politische Spannungen, hohe Kosten und regulatorische Hürden

**Zitat:** „Politische Spannungen auf europäischer Ebene, hohe Energie- und Arbeitskosten, strenge Umweltanforderungen, bürokratische Hürden sowie regulatorische Unsicherheiten belasten den Standort Europa weiterhin und können z. B. zu einer zunehmenden Abwanderung der Produktion und von Investitionen, zu einem Anstieg bei Insolvenzen und zu deutlichen Wettbewerbsnachteilen infolge einseitiger Regulierungen führen.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...en weiterhin laufend beobachtet sowie bewertet und geplante Maßnahmen konsequent umgesetzt. » S TRUKTURWANDEL IN DER EUROPÄISCHEN INDUSTRIE Politische Spannungen auf europäischer Ebene, hohe Energie- und Arbeitskosten, strenge Umwelt- anforderungen, bürokratische Hürden sowie regulatorische Unsicherheiten belasten den Standort Europa weiterhin und können z. B. zu einer zunehmenden Abwanderung der Produktion und von In vestitionen, zu einem Anstieg bei Insolvenzen und zu deutlichen Wettbewerbsnachteilen infolge einseitiger Regulierungen führen. In diesem Umfeld sind Schutzmaßnahmen zur Sicherung der Wett- bewerbsfähigkeit und Stabilität der europäischen Industrie von erheblicher Bedeutung. Entwicklun- gen werden weiterhin laufend beobachtet sowie ...


### VOE-047 | PDF-Seite 93 | hauptrisiken / Regulierung

**Aussage:** Mehraufwand und Haftungsrisiken durch Lieferkettensorgfaltspflichtengesetze

**Zitat:** „Die erforderlichen Aktivitäten zur Erfüllung des deutschen Lieferkettensorgfaltspflichtengesetzes wurden initiiert. Prozessvorgaben an betroffenen Standorten sind ausgerollt und werden laufend abgearbeitet. Zur Vorbereitung auf das europäische Lieferkettensorgfaltspflichtengesetz wurden erste Umsetzungsmaßnahmen gestartet.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...che Auswirkungen, Risiken und Chancen und ihr Zusammenspiel mit Strategie und Geschäfts - modell sowie in den themenspezifischen Kapiteln). Die erforderlichen Aktivitäten zur Erfüllung des deutschen Lieferkettensorgfaltspflichtengesetzes wurden initiiert. Prozessvorgaben an betroffenen Standorten sind ausgerollt und werden laufend abgearbeitet. Zur Vorbereitung auf das europäische Lieferkettensorgfaltspflichtengesetz wurden erste Umsetzungsmaßnahmen gestartet. Die gesetzlichen Entwicklungen ergeben einen erhöhten Mehraufwand, da die Umsetzungsverantwortung ohne vorgegebenen Mindest-Standard auf die großen Unternehmen abgeschoben wurde. Gesetzliche Entwicklungen werd...


### VOE-048 | PDF-Seite 93 | hauptrisiken / Finanzierung

**Aussage:** Liquiditätsrisiko und Nichterfüllung finanzieller Verpflichtungen

**Zitat:** „Liquiditätsrisiken bestehen im Allgemeinen darin, dass ein Unternehmen möglicherweise nicht in der Lage ist, den finanziellen Verpflichtungen nachzukommen. Die bestehenden Liquiditätsreserven versetzen die Gesellschaft in die Lage, auch in Krisenzeiten ihre Verpflichtungen fristgerecht zu erfüllen.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...t einem Grundgeschäft verwendet werden. Im Einzelnen werden Finanzierungsrisiken durch folgende Maßnahmen abgesichert: » Liquidit ätsrisiko Liquiditätsrisiken bestehen im Allgemeinen darin, dass ein Unternehmen möglicherweise nicht in der Lage ist, den finanziellen Verpflichtungen nachzukommen. Die bestehenden Liquiditätsreserven versetzen die Gesellschaft in die Lage, auch in Krisenzeiten ihre Verpflichtungen fristgerecht zu erfüllen. Wesentliches Instrument zur Steuerung des Liquiditätsrisikos ist neben der Liquiditätsreserve


### VOE-049 | PDF-Seite 94 | hauptrisiken / Finanzierung

**Aussage:** Bonitätsrisiko und Ausfall von Forderungen gegenüber Geschäftspartnern

**Zitat:** „Das Bonitätsrisiko bezeichnet Vermögensverluste, die aus der Nichterfüllung von Vertragsverpflichtungen einzelner Geschäftspartner:innen entstehen können. Das Bonitätsrisiko der Grundgeschäfte ist durch einen hohen Anteil an Kreditversicherungen und bankmäßigen Sicherheiten (Garantien, Akkreditive) weitestgehend abgesichert.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...m Klumpenrisiken zu ver - meiden. Es wird weiterhin hoher Wert auf die Steigerung der internen Finanzierungskraft gelegt. » Bonit ätsrisiko Das Bonitätsrisiko bezeichnet Vermögensverluste, die aus der Nichterfüllung von Vertragsverpflich- tungen einzelner Geschäftspartner:innen entstehen können. Das Bonitätsrisiko der Grundgeschäfte ist durch einen hohen Anteil an Kreditversicherungen und bankmäßigen Sicherheiten (Garantien, Akkreditive) weitestgehend abgesichert. Das Ausfallrisiko für das verbleibende Eigenrisiko wird durch definierte Prozesse der Bonitätsbeurteilung, Risikobewertung, Risikoklassifizierung und Bonitäts überw achung gemanagt. Durch den aktuellen Ukrai...


### VOE-050 | PDF-Seite 95 | hauptrisiken / Finanzierung

**Aussage:** Währungs- und Zinsrisiken im Finanzbereich

**Zitat:** „Die Zinsrisikobeurteilung erfolgt für den gesamten Konzern zentral in der voestalpine AG. Hier wird insbesondere das Cashflow-Risiko (Risiko, dass sich der Zinsaufwand bzw. Zinsertrag zum Nachteil verändert) gemanagt.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> 95 GESCHÄFTSBERICHT 2025/26 » Zinsrisik o Die Zinsrisikobeurteilung erfolgt für den gesamten Konzern zentral in der voestalpine AG. Hier wird insbesondere das Cashflow-Risiko (Risiko, dass sich der Zinsaufwand bzw. Zinsertrag zum Nachteil verändert) gemanagt. Mit Stichtag 31. März 2026 würde die Erhöhung des Zinsniveaus um einen Prozentpunkt zu einer Verminderung des Nettozinsaufwands aus Bankdarlehen und Kapitalmarkt- verbindlichkeiten im nächsten Geschäftsjahr in...


### VOE-051 | PDF-Seite 122 | strategische_prioritaeten

**Aussage:** Fokussiertes Wachstum in renditestarken Bereichen wie Schieneninfrastruktur, Luftfahrtindustrie, Spezialprofilen und Lagertechnik

**Zitat:** „Entsprechend unserem übergeordneten strategischen Ziel der Wertsteigerung und damit der Erhöhung des Unternehmenswerts ist das fokussierte Wachstum in attraktiven, renditestarken Bereichen wie der Schieneninfrastruktur, der Luftfahrtindustrie sowie bei Spezialprofilen und in der Lagertechnik ein wesentlicher strategischer Pfeiler.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...rt im Konzernverbund. Zudem führt unsere stabile Eigentümerstruktur zu strategischer Eigenständigkeit im Interesse aller Stakeholder:innen. Entsprechend unserem übergeordneten strategischen Ziel der Wertsteigerung und damit der Erhöhung des Unternehmenswerts ist das fokussierte Wachstum in attraktiven, r enditestarken Bereichen wie der Schieneninfrastruktur, der Luftfahrtindustrie sowie bei Spezialprofilen und in der L agertechnik ein wesentlicher strategischer Pfeiler. Wir entwickeln unser Angebotsportfolio mit inno- vativen Lösungen weiter, stärken unsere Differenzierungsfaktoren in unseren Kernmärkten und setzen auf eine weitere zielgerichtete Internationalisierung in Wa...


### VOE-052 | PDF-Seite 122 | strategische_prioritaeten

**Aussage:** Aktives Portfoliomanagement, Effizienzfokus und Reorganisation renditeschwacher Geschäftsbereiche

**Zitat:** „Ein aktives und konsequentes Management unseres Portfolios mit Fokus auf Effizienz in allen Bereichen und Stärkung der Wettbewerbsfähigkeit unserer (Produktions-)Standorte sowie der Reorganisation renditeschwacher Geschäftsbereiche sichert zudem die Zukunftsfähigkeit und Resilienz des Unternehmens und bildet damit den zweiten wesentlichen Pfeiler unserer Strategie.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...zierungsfaktoren in unseren Kernmärkten und setzen auf eine weitere zielgerichtete Internationalisierung in Wachstumsmärkten und -regionen. Ein aktives und konsequentes Management unseres Portfolios mit Fokus auf Effizienz in allen Bereichen und Stärkung der Wettbewerbsfähigkeit unserer (Produktions-)Standorte sowie der Reorganisation renditeschwacher Geschäftsbereiche sichert zudem die Zukunftsfähigkeit und Resilienz des Unterneh- mens und bildet damit den zweiten wesentlichen Pfeiler unserer Strategie. Die wirtschaftlich erfolg - r eiche Dekarbonisierung der hochofenbasierten Stahlerzeugung mit dem klaren Ziel von Net-Zero- Emissionen bis 2050 und dem weiteren Auf- und Ausbau der Kreislaufwirtschaft bildet...


### VOE-053 | PDF-Seite 122 | strategische_prioritaeten

**Aussage:** Wirtschaftlich erfolgreiche Dekarbonisierung der Stahlerzeugung mit dem Ziel Net-Zero bis 2050 und Ausbau der Kreislaufwirtschaft

**Zitat:** „Die wirtschaftlich erfolgreiche Dekarbonisierung der hochofenbasierten Stahlerzeugung mit dem klaren Ziel von Net-Zero-Emissionen bis 2050 und dem weiteren Auf- und Ausbau der Kreislaufwirtschaft bildet den dritten wesentlichen Pfeiler unserer Strategie.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...e sichert zudem die Zukunftsfähigkeit und Resilienz des Unterneh- mens und bildet damit den zweiten wesentlichen Pfeiler unserer Strategie. Die wirtschaftlich erfolg - r eiche Dekarbonisierung der hochofenbasierten Stahlerzeugung mit dem klaren Ziel von Net-Zero- Emissionen bis 2050 und dem weiteren Auf- und Ausbau der Kreislaufwirtschaft bildet den dritten wesentlichen Pfeiler unserer Strategie. Als internationaler Konzern bekennen wir uns zu den globalen Klimazielen und arbeiten intensiv an Technologien zur Reduktion von Treibhausgasemissionen sowie an der langfristigen Dekarbonisierung. NACHHAL...


### VOE-054 | PDF-Seite 123 | capex_ma_signale

**Aussage:** Investitionen in zukunftsweisende und wasserstoffbasierte Technologien

**Zitat:** „Die voestalpine investiert in wasserstoffbasierte und zukunftsweisende Technologien, um eine emissionsarme Produktion zu ermöglichen.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...otwen- digkeit, den Klimawandel einzudämmen, müssen Stahlhersteller:innen alternative Wege für eine umw eltfreundlichere Produktion finden. Die voestalpine investiert in wasserstoffbasierte und zukunfts- weisende Technologien, um eine emissionsarme Produktion zu ermöglichen. Die voestalpine bekennt sich zu klaren Nachhaltigkeitszielen und sieht bis 2050 Net-Zero-Emissionen vor. Im Rahmen der Science Based Targets initiative (SBTi) verpflichtet sich das Unternehmen, die Sum- me d...


### VOE-055 | PDF-Seite 124 | capex_ma_signale

**Aussage:** Investition von 1,5 Mrd. EUR in zwei grünstrombetriebene Elektrolichtbogenöfen an den Standorten Linz und Donawitz

**Zitat:** „In der ersten Phase werden bereits 1,5 Mrd. EUR in einen grünstrombetriebenen Elektrolichtbogenofen in Linz und in eine grünstrombetriebene Elektrolichtbogenofenanlage in Donawitz investiert, die jeweils einen Hochofen ersetzen sollen.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...bei wird die hochofenbasierte Stahlerzeugung in der Steel Division und der Metal Engineering Division schrittweise bis 2050 dekarbonisiert. In der ersten Phase werden bereits 1,5 Mrd. EUR in einen grünstrombetriebenen Elektrolichtbogenofen in Linz und in eine grüns trombetriebene Elektrolichtbogenofenanlage in Donawitz investiert, die je- weils einen Hochofen ersetzen sollen. Je nach Qualitäts an forderungen kommt dabei ein Materialmix aus Schrott, flüssigem R oheisen und Hot Briquetted Iron (HBI) zum Einsatz. Diese sich bereits in Bau befindlichen Elektrolichtbogenöfen werden 2...


### VOE-056 | PDF-Seite 124 | strategische_prioritaeten

**Aussage:** Schrittweise Dekarbonisierung der Stahlerzeugung im Rahmen des Klimaschutzprogramms greentec steel bis 2050

**Zitat:** „Um der Herausforderung dieser Dekarbonisierung der Stahlerzeugung unter Erhalt der Wirtschaftlichkeit und Wettbewerbsfähigkeit zu begegnen und das Net-Zero-Ziel bis 2050 zu erreichen, hat die voestalpine das ambitionierte Klimaschutzprogramm greentec steel als ein Kernelement in der Konzern- und Nachhaltigkeitsstrategie entwickelt.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> 124 GESCHÄFTSBERICHT 2025/26 Um der Herausforderung dieser Dekarbonisierung der Stahlerzeugung unter Erhalt der Wirtschaftlich- keit und Wettbewerbsfähigkeit zu begegnen und das Net-Zero-Ziel bis 2050 zu erreichen, hat die v oestalpine das ambitionierte Klimaschutzprogramm greentec steel als ein Kernelement in der Konzern- und Nachhaltigkeitsstrategie entwickelt. Dabei wird die hochofenbasierte Stahlerzeugung in der Steel Division und der Metal Engineering Division schrittweise bis 2050 dekarbonisiert. In der ersten Phase werden bereits 1,5 Mrd. EUR in einen grünstr...


### VOE-057 | PDF-Seite 124 | strategische_prioritaeten

**Aussage:** Ausbau der Kreislaufwirtschaft und Erhöhung des Schrotteinsatzes bis 2030

**Zitat:** „Um diese Herausforderungen zu adressieren, hat sich die voestalpine die strategischen Ziele gesetzt, die Versorgung der Produktionsstandorte mit den benötigten Rohstoffen und Energien langfristig und wirtschaftlich abzusichern sowie die Kreislaufwirtschaft weiter auszubauen und den Einsatz von Schrott als Sekundärrohstoff in der Stahlerzeugung bis 2030 um 50 % zu erhöhen.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ... in der Sicherung der benötigten Rohstoffe und Energieträger, deren Bedarfe sich im Zuge der Transfor- mation der Stahlerzeugung verändern. Um diese Herausforderungen zu adressieren, hat sich die v oestalpine die strategischen Ziele gesetzt, die Versorgung der Produktionsstandorte mit den benö- tigten Rohstoffen und Energien langfristig und wirtschaftlich abzusichern sowie die Kreislaufwirtschaft weiter auszubauen und den Einsatz von Schrott als Sekundärrohstoff in der Stahlerzeugung bis 2030 um 50 % zu erhöhen. Entsprechende Maßnahmenpakete werden bereits umgesetzt und werden wei- terhin entwickelt. Weitere Informationen dazu finden Sie in den Kapiteln E1 und E5. Eine weitere strategische Herausforderung für die v...


### VOE-058 | PDF-Seite 124 | strategische_prioritaeten

**Aussage:** Senkung der Unfallhäufigkeitsquote bis 2030

**Zitat:** „Daher wird kontinuierlich an der weiteren Reduktion der Unfallhäufigkeit sowie der Erhöhung der Gesundheitsquote gearbeitet, um sich der Vision von „Zero Accidents“ anzunähern. Strategisch soll die Unfallhäufigkeitsquote bis 2030 auf 5,5 gesenkt werden.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...innen und die laufende Sicherstellung und Erhö- hung der Arbeitssicherheit zentrale Grundwerte der voestalpine und haben oberste Priorität. Daher wird kontinuierlich an der weiteren Reduktion der Unfallhäufigkeit sowie der Erhöhung der Gesund- heitsquote gearbeitet, um sich der Vision von „Zero Accidents“ anzunähern. Strategisch soll die Unfall - häufigk eitsquote bis 2030 auf 5,5 gesenkt werden. Konzernweite Sicherheitsstandards bilden das Fundament einer erfolgreichen health & safety-Unternehmenskultur. Weitere Informationen dazu fin - den Sie im Kapitel S1. Die voestalpine adressiert auch die ...


### VOE-059 | PDF-Seite 134 | hauptrisiken / Technologie

**Aussage:** Sicherstellung der Produktqualität bei vermehrtem Schrotteinsatz

**Zitat:** „Dem Risiko der „Sicherstellung der Produktqualität bei vermehrtem Schrotteinsatz“ begegnet die voestalpine mit einem breiten Maßnahmenbündel. Kern dieser Maßnahmen ist der verstärkte Forschungsfokus, um nach Umstellung von der Hochofen- auf die Elektrolichtbogenofenroute weiterhin Stahlgüten in höchster Qualität herstellen zu können (siehe Kapitel I, F&E).“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...des Strategiereviewprozesses regelmäßig analysiert und bewertet. Angaben hinsichtlich des Klima- wandels finden sich im Abschnitt SBM-3 E1. Dem Risiko der „Sicherstellung der Produktqualität bei vermehrtem Schrotteinsatz“ begegnet die voestalpine mit einem breiten Maßnahmenbündel. Kern dieser Maßnahmen ist der verstärkte Forschungsfokus, um nach Umstellung von der Hochofen- auf die Elektrolichtbogenofenroute weiterhin Stahlgüten in höchster Qualität herstellen zu können (siehe Kapitel I, F&E). In Bezug auf das Risiko durch Verstöße gegen Compliance-Richtlinien und Wirtschafts- kriminalität liegen ausreichend Konzepte und Verfahren vor. Nähere Informationen dazu finden sich im Kapitel G1-1 und G1-3. ...


### VOE-060 | PDF-Seite 135 | hauptrisiken / Regulierung

**Aussage:** Höhere Kosten durch CO2-Bepreisung und Wettbewerbsnachteile

**Zitat:** „CO2e-Bepreisungsmechanismen wie das EU-Emissionshandelssystem (ETS) und der CO2 -Grenzausgleichsmechanismus (CBAM) führen zu steigenden finanziellen Belastungen, die potenziell Wettbewerbsnachteile gegenüber Nicht-EU-Wettbewerber:innen verursachen und einen strukturellen Wandel, wie Abwanderung von Abnehmerindustrien und einen höheren Preiswettbewerb, in der Industrie auslösen können.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...htlich der identifizierten transitorischen Klima risik en wurden geplante und aktuelle Mitigationsmaßnahmen mitberücksichtigt (siehe E1-3). CO2e-Bepreisungsmechanismen wie das EU-Emissionshandelssystem (ETS) und der CO2 -Grenzaus- gleichsmechanismus (CBAM) führen zu steigenden finanziellen Belastungen, die potenziell Wettbe- werbsnachteile gegenüber Nicht-EU-Wettbewerber:innen verursachen und einen strukturellen Wan- del, wie Abwanderung von Abnehmerindustrien und einen höheren Preiswettbewerb, in der Industrie auslösen können. Ein Kernelement der strategischen Ausrichtung der voestalpine stellt die Dekarbonisierung der Stahl- erzeugung dar (siehe SBM-1), unter anderem, um dem Risiko der höheren Kosten für CO2-Zertifikate entsp...


### VOE-061 | PDF-Seite 135 | hauptrisiken / Lieferkette

**Aussage:** Engpässe in der Energieversorgung und höhere Beschaffungskosten

**Zitat:** „Gleichzeitig können damit verbundene transitorische Risiken entstehen – insbesondere in Bezug auf Lieferengpässe für Energie, wichtige Rohstoffe und damit einhergehende höhere Kosten und sich verändernden Wettbewerb –, denen mit laufenden Maßnahmen entgegengewirkt wird (siehe E1-3).“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ... bereits berücksichtigt (siehe E1-1 und E1-3), womit die voestalpine die Anpassung des Geschäftsmodells an den Klimawandel sicher - stellt. Gleichzeitig können damit verbundene transitorische Risiken entstehen – insbesondere in Bezug auf Lieferengpässe für Energie, wichtige Rohstoffe und damit einhergehende höhere Kosten und sich ver- ändernden Wettbewerb –, denen mit laufenden Maßnahmen entgegengewirkt wird (siehe E1-3).


### VOE-062 | PDF-Seite 145 | hauptrisiken / Lieferkette

**Aussage:** Lieferkettenprobleme durch klimabedingte Pegelschwankungen

**Zitat:** „Ein chronisches Klimarisiko sind beispielsweise klimabedingte Pegelschwankungen von Flüssen, die die Schiffbarkeit beeinträchtigen (z. B. auf der Donau) und dadurch Lieferkettenprobleme verursachen können.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...enfälle, Überflutungen und Murenabgänge wurden beispielsweise für den voestalpine-Konzern als wesentliche akute Klimarisiken identifiziert. Ein chroni- sches Klimarisiko sind beispielsweise klimabedingte Pegelschwankungen von Flüssen, die die Schiff - barkeit beeinträchtigen (z. B. auf der Donau) und dadurch Lieferkettenprobleme verursachen können.


### VOE-063 | PDF-Seite 176 | capex_ma_signale

**Aussage:** Investitionsbudget von 1,5 Mrd. EUR fuer die erste Phase des Projekts greentec steel bis zum Geschaeftsjahr 2027/28

**Zitat:** „Der CapEx-Plan umfasst ein Gesamtvolumen von 1,5 Mrd. EUR und wird aller Voraussicht nach im Geschäftsjahr 2027/28 abgeschlossen werden. Im abgelaufenen Geschäftsjahr wurden 292,7 Mio. EUR (2024/25: 134,4 Mio. EUR) im Zuge des CapEx-Plans als taxonomiekonform unter der Wirtschaftstätigkeit 3.9 Herstellung von Eisen und Stahl klassifiziert.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...ns tändige Produk tionseinheit mit den en tsprechenden technischen Be- wertungskriterien unter dem Umweltziel Klimaschutz ermittelt werden. Der CapEx-Plan umfasst ein Gesamtvolumen von 1,5 Mrd. EUR und wird aller Voraussicht nach im Geschäftsjahr 2027/28 abge- schlossen werden. Im abgelaufenen Geschäftsjahr wurden 292,7 Mio. EUR (2024/25: 134,4 Mio. EUR) im Zuge des CapEx-Plans als taxonomiekonform unter der Wirtschaftstätigkeit 3.9 Herstellung von Eisen und S tahl klassifiziert. Der taxonomiekonforme CapEx in Höhe von 381,8 Mio. EUR setzt sich aus Zugängen zu Sach- anlagen und immateriellen Vermögenswerten in Höhe von 371,1 Mio. EUR, Zugängen zu Sachanlagen und immateriellen Vermög...


### VOE-064 | PDF-Seite 181 | hauptrisiken / Technologie

**Aussage:** Risiken bei der technischen Umstellung auf emissionsarme Technologien im Rahmen von greentec steel

**Zitat:** „Die Transformation hin zu einer emissionsarmen Stahlproduktion im Rahmen von greentec steel erfordert von der voestalpine erhebliche Investitionen in neue Technologien und Anlagen, die unter teils unsicheren gesetzlichen Rahmenbedingungen getätigt werden, z. B.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ... Lokale, nationale und internationale Behörden Lieferant:innen Transitorisches Risiko: Technische Umstellung auf emissionsarme Technologien Die Transformation hin zu einer emissions - armen S tahlproduktion im Rahmen von greentec steel erfordert von der voestalpine erhebliche Investitionen in neue Technologien und Anlagen, die unter teils unsicheren gesetz lichen R ahmenbedingungen getätigt werden, z. B. Unsicher heit en bei der Ausgestal- tung von Schutzmaßnahmen wie dem Carbon Border Adjustment Mechanism (CBAM) und bei der zukünftigen Zuteilung von kostenlosen Zertifikaten. Auch das Fehlen einer einhei...


### VOE-065 | PDF-Seite 181 | hauptrisiken / Regulierung

**Aussage:** Kostenbelastungen und Wettbewerbsnachteile durch CO2e-Bepreisungsmechanismen

**Zitat:** „CO2e-Bepreisungsmechanismen wie das EU-Emissionshandelssystem (ETS) und der CO2-Grenzausgleichsmechanismus (CBAM) führen zu steigenden finanziellen Belastungen, die potenziell Wettbewerbsnachteile gegenüber Nicht-EU-Wettbewerber:innen verursachen und einen strukturellen Wandel, wie Abwanderung von Abnehmerindustrien und einen höheren Preiswettbewerb, in der Industrie auslösen können.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...emporären Betriebs aus fällen. Umwelt Lokale, nationale und internationale Behörden Transitorisches Risiko: Kosten aufgrund CO2e-Bepreisung CO2e-Bepreisungsmechanismen wie das EU-Emissionshandelssystem (ETS) und der CO2-Grenzausgleichsmechanismus (CBAM) führen zu steigenden finanziellen Belastungen, die potenziell Wettbewerbsnachteile gegen- über Nicht-EU-Wettbewerber:innen verursachen und einen strukturellen Wandel, wie Abwande- rung von Abnehmerindustrien und einen höheren Preiswettbewerb, in der Industrie auslösen können. Umwelt Gesetzgeber:innen Mitbewerber:innen Kund:innen Lieferant:innen Investor:innen Transitorische Chance: Steigerung der Verkaufs - v olumina von emissions - armen S tahlprodukten für die voestalpine (in...


### VOE-066 | PDF-Seite 182 | hauptrisiken / Lieferkette

**Aussage:** Lieferengpaesse und hoehere Kosten fuer wichtige Materialien und Rohstoffe

**Zitat:** „Im Zuge der Transformation steigt die Nachfrage nach kritischen Rohstoffen wie Stahlschrott sowie speziellen Metallen und Legierungen, wodurch das Risiko von Versorgungsengpässen zunimmt. Die voestalpine sieht sich mit einem wachsenden Bedarf konfrontiert, der potenziell zu Produktionsverzögerungen oder Qualitätsrisiken führen kann.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ... Betroffene Stake holder:innen Klimaschutz Transitorisches Risiko: Lieferengpässe bzw. höhere Kosten für wichtige Materialien und Rohstoffe Im Zuge der Transformation steigt die Nach - fr age nach kritischen Rohstoffen wie Stahlschrott sowie speziellen Metallen und Legierungen, wodurch das Risiko von Versorgungsengpässen zunimmt. Die voestalpine sieht sich mit einem wachsenden Bedarf konfrontiert, der potenziell zu Produkti ons verzögerungen oder Qualitäts - risik en führen kann. Gleichzeitig erschwert ausgeprägte Preisvolatilität die Planbarkeit und mindert die Investitionssicherheit. Lieferant:innen Anpassung an den Klimawandel Physische Klimarisiken Physische Risiken könne...


### VOE-067 | PDF-Seite 182 | hauptrisiken / Markt

**Aussage:** Versorgungsengpaesse und steigende Beschaffungskosten im Energiebereich

**Zitat:** „Das transitorische Risiko für die voestalpine umfasst mögliche Versorgungsengpässe an großen Produktionsstandorten (insbesondere Linz und Donawitz) sowie steigende Energiebeschaffungskosten (erneuerbare und nicht erneuerbare Quellen) vor dem Hintergrund der europäischen Energiewende.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...innen Lieferant:innen Energie Transitorisches Risiko: Engpässe in der Energie - v ersorgung und höhere Kosten für die Energie - beschaffung Das transitorische Risiko für die voestalpine umfasst mögliche Versorgungsengpässe an großen Produktionsstandorten (insbesondere Linz und Donawitz) sowie steigende Energie - beschaffungsk osten (erneuerbare und nicht erneuerbare Quellen) vor dem Hintergrund der europäischen Energiewende. Das wird vor allem auch durch volatile Energiemärkte und potenzielle Knappheiten getrieben. Lieferant:innen Legende tatsächlich positive Auswirkung tatsächlich negative Auswirkung potenziell positive Auswi...


### VOE-068 | PDF-Seite 183 | strategische_prioritaeten

**Aussage:** Umfassende Reduktion der Treibhausgasemissionen und Transformation zu einer emissionsaermeren Stahlproduktion

**Zitat:** „Die voestalpine verfolgt eine umfassende Reduktion der Treibhausgasemissionen entlang der gesamten Wertschöpfungskette und hat sich im Rahmen der Science Based Targets initiative (SBTi) verpflichtet, ihre Emissionen entsprechend dem wissenschaftlich fundierten 2-Grad-Reduktionspfad zu senken.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> 183 GESCHÄFTSBERICHT 2025/26 STRATEGIE E1-1 – Übergangsplan für den Klimaschutz Die voestalpine verfolgt eine umfassende Reduktion der Treibhausgasemissionen entlang der gesam- ten Wertschöpfungskette und hat sich im Rahmen der Science Based Targets initiative (SBTi) verpflich- tet, ihre Emissionen entsprechend dem wissenschaftlich fundierten 2-Grad-Reduktionspfad zu senken. Bis zum Kalenderjahr 2029 sollen die Scope-1- und Scope-2-Emissionen um 30 % und Scope-3- E missionen um 25 % gesenkt werden. Die gesetzten Vorgaben wurden von der SBTi geprüft und vali- diert und stehen i...


### VOE-069 | PDF-Seite 184 | capex_ma_signale

**Aussage:** Gezielte Investitionen der naechsten Jahre in emissionsarme Technologien und energieeffiziente Anlagen

**Zitat:** „Die finanziellen Mittel zur Umsetzung von Phase 1 dieser Transformation sind in der Mittelfristplanung berücksichtigt. Die voestalpine investiert in den nächsten Jahren gezielt in emissionsarme Technologien und energieeffiziente Anlagen.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...ns und die erforderlichen finanziellen Mittel (1,5 Mrd. EUR Investitionsbudget) zur Umsetzung sind von Vorstand und Aufsichtsrat genehmigt. Die finanziellen Mittel zur Umsetzung von Phase 1 dieser Transformation sind in der Mittelfristplanung berücksichtigt. Die voestalpine investiert in den nächsten Jahren gezielt in emissionsarme Technolo- gien und energieeffiziente Anlagen. Zudem erfolgt eine regelmäßige Quantifizierung der benötigten Investitionen, um die Transformation wirtschaftlich nachhaltig zu gestalten. Alle detaillierten Angaben zu CapEx-Plänen und Leistungsindikatoren ...


### VOE-070 | PDF-Seite 185 | capex_ma_signale

**Aussage:** Aufsichtsrat genehmigte rund 1,5 Mrd. EUR CapEx für Elektrolichtbogenöfen in Linz und Donawitz (Phase 1 greentec steel), wovon bis Ende 2025/26 rund 0,9 Mrd. EUR investiert wurden.

**Zitat:** „Rund 1,5 Mrd. EUR wurden für die Elektrolichtbogenöfen in Linz und Donawitz im Zuge der Phase 1 des Klimaschutzprogramms greentec steel vom Aufsichtsrat bereits genehmigt, was einen zentralen Bestandteil des Klimaübergangsplans des Unternehmens bildet. Davon wurden bereits rund 0,9 Mrd. EUR bis zum Ende des Geschäftsjahres 2025/26“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...ategie zur Dekarbonisierung und der EU ­T axonomie im Geschäftsjahr 2023/24 einen CapEx­ Plan mit einer Laufzeit von fünf Jahren initiiert. Rund 1,5 Mrd. EUR wurden für die Elektrolichtbogenöfen in Linz und Donawitz im Zuge der Phase 1 des Klimaschutzprogramms greentec steel vom Aufsichtsrat be­ reits genehmigt, was einen zentralen Bestandteil des Klimaübergangsplans des Unternehmens bildet. Davon wurden bereits rund 0,9 Mrd. EUR bis zum Ende des Geschäftsjahres 2025/26 (bis 2024/25: rund 0,5 Mrd. EUR) investiert. Darüber hinaus werden weitere Investitionen für den weiteren Ersatz der fossilen Roheisenkapazitäten und CCUS ­T echnologien (Phase 2) in den finanziellen Planung...


### VOE-071 | PDF-Seite 185 | capex_ma_signale

**Aussage:** Im Geschäftsjahr wurden 381,8 Mio. EUR als taxonomiekonformer CapEx ausgewiesen, wovon 292,7 Mio. EUR auf greentec steel entfallen.

**Zitat:** „Im aktuellen Geschäftsjahr wurden insgesamt 381,8 Mio. EUR CapEx als taxonomiekonform ausgewiesen (siehe auch Kapitel Angaben nach der EU-Taxonomie-Verordnung), wobei 303,3 Mio. EUR auf die Wirtschaftstätigkeit 3.9 Herstellung von Eisen und Stahl entfallen, wovon wiederum 292,7 Mio. EUR Investitionen in Zusammenhang mit greentec steel darstellen.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...chritts der Maßnahmen innerhalb der Dekarbonisierungshebel wird der t axonomiekonforme CapEx als zentraler Leistungsindikator herangezogen. Im aktuellen Geschäfts­ jahr wurden insgesamt 381,8 Mio. EUR CapEx als taxonomiekonform ausgewiesen (siehe auch K apitel Angaben nach der EU ­T axonomie ­V erordnung), wobei 303,3 Mio. EUR auf die Wirtschaftstätigkeit 3.9 Herstellung von Eisen und Stahl entfallen, wovon wiederum 292,7 Mio. EUR Investitionen in Zusam­ menhang mit greentec steel darstellen. Im Berichtsjahr wurden keine signifikanten CapEx­ Beträge im Zusammenhang mit Wirtschaftstätigkeiten in den Bereichen Kohle, Öl und Gas investiert. Bereits im Jahr 2024 hat die voestalpine mit der Ver...


### VOE-072 | PDF-Seite 185 | capex_ma_signale

**Aussage:** Fördermittel in Höhe von rund 90 Mio. EUR für Elektrolichtbogenofentechnologie und Forschung erhalten.

**Zitat:** „Darüber hinaus hat die voestalpine Förderzusagen in Höhe von rund 90 Mio. EUR für die Investition in die Elektrolichtbogenofentechnologie und weitere Forschungsaktivitäten erhalten. Diese Mittel stammen aus dem Programm „Transformation der Industrie“ der österreichischen Bundesregierung und unterstützen die Umsetzung zentraler Dekarbonisierungshebel.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...nehmen hat erhebliche Investitionen und Finanzmittel bereitgestellt, um seinen Übergangs­ plan zur Dekarbonisierung erfolgreich umzusetzen. Darüber hinaus hat die voestalpine Förder ­ zusagen in Höhe von rund 90 Mio. EUR für die Investition in die Elektrolichtbogenofentechnologie und w eitere Forschungsaktivitäten erhalten. Diese Mittel stammen aus dem Programm „Transforma tion der Industrie“ der österreichischen Bundesregierung und unterstützen die Umsetzung zentraler De­ karbonisierungshebel. Zur Messung des Fortschritts der Maßnahmen innerhalb der Dekarbonisierungshebel wird der t axonomiekonforme CapEx als zentraler Leistungsindikator herangezogen. Im aktuellen Geschäfts­ jahr wurden insge...


### VOE-073 | PDF-Seite 186 | strategische_prioritaeten

**Aussage:** Stufenweise Dekarbonisierung der Stahlproduktion (greentec steel) und Reduktion von Emissionen bis Net-Zero 2049/50

**Zitat:** „Die Umsetzung des greentec steel-Programms – die stufenweise Transformation der Prozesse zur Rohstahlherstellung – im Rahmen des Klimaübergangsplans ermöglicht eine nachhaltige Weiterentwicklung des Kerngeschäfts, indem emissionsarme Technologien schrittweise eingeführt und bestehende Prozesse optimiert werden.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...eng mit der Nachhaltigkeitsstrate- gie der voestalpine verknüpft und unterstützen die langfristige Wettbewerbsfähigkeit des Unterneh- mens. Die Umsetzung des greentec steel-Programms – die stufenweise Transformation der Prozesse zur Rohstahlherstellung – im Rahmen des Klimaübergangsplans ermöglicht eine nachhaltige Weiter- entwicklung des Kerngeschäfts, indem emissionsarme Technologien schrittweise eingeführt und bes tehende Prozesse optimiert werden. Dies stellt sicher, dass die Stahlproduktion sowohl den regula - t orischen Anforderungen als auch den steigenden Marktanforderungen an klimafreundliche Produkte entspricht. Informationen dazu finden sich i...


### VOE-074 | PDF-Seite 190 | hauptrisiken / Lieferkette

**Aussage:** Lieferengpässe bzw. höhere Kosten für wichtige Materialien und Rohstoffe

**Zitat:** „Zur Reduktion der indirekten Treibhausgasemissionen entlang Scope 3 bis zum Geschäftsjahr 2029/30 konzentriert sich die voestalpine auf gezielte Maßnahmen innerhalb ihrer Wertschöpfungskette. Ein zentraler Dekarbonisierungshebel ist dabei das Supplier Engagement, eine Dekarbonisierung wesentlicher bestehender Rohstoffe.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> 190 GESCHÄFTSBERICHT 2025/26 PHASE 1: DEKARBONISIERUNGSHEBEL SCOPE 3 Zur Reduktion der indirekten Treibhausgasemissionen entlang Scope 3 bis zum Geschäftsjahr 2029/30 konzentriert sich die voestalpine auf gezielte Maßnahmen innerhalb ihrer Wertschöpfungskette. Ein zentraler Dekarbonisierungshebel ist dabei das Supplier Engagement, eine Dekarbonisierung wesent- licher bestehender Rohstoffe. Die Grundlagen bilden die Nutzung valider Daten, z. B. Product Carbon Footprints (PCFs) für wesentliche Rohstoffe und entsprechende Dekarbonisierungsvorhaben und -maßnahmen in der Wertschöpfungskette sowie e...


### VOE-075 | PDF-Seite 191 | hauptrisiken / Regulierung

**Aussage:** Transitorisches Risiko durch Kosten aufgrund von CO2e-Bepreisung

**Zitat:** „Die voestalpine begegnet diesem Risiko durch gezielte Investitionen im Rahmen einer schrittweisen Transformation der Produktionsprozesse. Ergänzend setzt der Konzern auf verstärkte Differenzierung in Produktqualität, Flexibilität und Service.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...wege und Logistikanpassung bei Niedrigwasser. WEITERE AKTIVITÄTEN IM UMGANG MIT DEM TRANSITORISCHEN RISIKO: KOSTEN AUFGRUND CO2e-BEPREISUNG Die voestalpine begegnet diesem Risiko durch gezielte Investitionen im Rahmen einer schrittweisen Transformation der Produktionsprozesse. Ergänzend setzt der Konzern auf verstärkte Differenzierung in Produktqualität, Flexibilität und Service. Darüber hinaus trägt eine zunehmende Internationalisie- rung der voestalpine in renditestarken Weiterverarbeitungsbereichen nach dem „local for local“- Prinzip zur Sicherung der Wettbewerbsfähigkeit bei. MASSN...


### VOE-076 | PDF-Seite 217 | strategische_prioritaeten

**Aussage:** Steigerung des Schrotteinsatzes in der Rohstahlherstellung im Rahmen der Kreislaufwirtschaft

**Zitat:** „Die voestalpine setzt auf eine effiziente Ressourcennutzung, indem Schrott und andere metallhaltige Rückstände wieder in den Produktionsprozess zurückgeführt werden. Bis 2030 soll der Einsatz von Sekundärrohstoffen weiter gesteigert werden, indem der Schrotteinsatz in der Rohstahlherstellung um 50 % erhöht wird.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ... seiner vollen Recycelbarkeit, seiner Langlebigkeit und seiner Reparierbarkeit eine gute Ausgangsposition für die Kreislaufwirtschaft inne. Die voestalpine setzt auf eine effiziente R essourcennutzung, indem Schrott und andere metallhaltige Rückstände wieder in den Produktions- prozess zurückgeführt werden. Bis 2030 soll der Einsatz von Sekundärrohstoffen weiter gesteigert w erden, indem der Schrotteinsatz in der Rohstahlherstellung um 50 % erhöh t wird. Nebenprodukte wie Schlacken, Stäube und Schlämme werden, soweit technisch und rechtlich möglich, innerhalb des Unternehmens verwertet oder an andere Industrien abgegeben. Dadurch wird der Einsatz von Prim...


### VOE-077 | PDF-Seite 228 | hauptrisiken / Technologie

**Aussage:** Sinkende Produktqualität bei vermehrtem Schrotteinsatz

**Zitat:** „Der erhöhte Einsatz von Schrott im Zuge der Umstellung von primär kohlebasierten Hochöfen auf Elektrolichtbogenöfen birgt das Risiko sinkender Produktqualität. Wesentlich ist dieses Risiko aufgrund potenzieller Qualitätseinbußen bei verändertem Rohstoffeinsatz (Schrott, Feinerz) sowie aufgrund hoher Qualitätsanforderungen der Abnehmerbranchen.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...ation and Storage; CCUS). Bildungseinrich- tungen & Forschung Kund:innen Sicherstellen der Produkt- qualit ät bei vermehrtem Schrotteinsatz Der erhöhte Einsatz von Schrott im Zuge der Umstellung von primär kohlebasierten Hochöfen auf Elektrolichtbogenöfen birgt das Risiko sinkender Produktqualität. Wesentlich ist dieses Risiko aufgrund potenzieller Qualitätseinbußen bei verändertem Rohstoffeinsatz (Schrott, Feinerz) sowie aufgrund hoher Qualitätsanforde- rungen der Abnehmerbranchen. Kund:innen Legende tatsächlich positive Auswirkung tatsächlich negative Auswirkung potenziell positive Auswirkung potenziell negative Auswirkung Chance Risiko vorgelagert eigener Betrieb nachgelagert < 1 Jah...


### VOE-078 | PDF-Seite 229 | strategische_prioritaeten

**Aussage:** Implementierung der F&E- und Innovationsstrategie 2030+

**Zitat:** „Im Geschäftsjahr 2025/26 wurde ausgehend von der Konzernstrategie 2030+ die F&E- und Innovationsstrategie 2030+ konzeptioniert, deren Implementierung ab dem Geschäftsjahr 2026/27 geplant ist. Die Strategie zielt darauf ab, den wirtschaftlichen Erfolg des Unternehmens langfristig durch innovative Prozesse und nachhaltige Produkte zu sichern.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...t der Unternehmens - s trategie – trägt wesentlich zur Position der voestalpine als Innovations-, Technologie- und Qualitäts- führerin bei. Im Geschäftsjahr 2025/26 wurde ausgehend von der Konzernstrategie 2030+ die F&E- und Innovationsstrategie 2030+ konzeptioniert, deren Implementierung ab dem Geschäftsjahr 2026/27 geplant ist. Die Strategie zielt darauf ab, den wirtschaftlichen Erfolg des Unternehmens langfristig durch innovative Prozesse und nachhaltige Produkte zu sichern. Richtungsweisend für die dezentral organisierte F&E und Innovation der voestalpine sind die strate- gischen Innovationsrichtlinien, der definierte Innovationsprozess und die Ausrichtung der Forschungs- vorhabe...


### VOE-079 | PDF-Seite 242 | hauptrisiken / Technologie  **PRUEFEN**

**Aussage:** Berufliche Gefahren, Risiken für Arbeitsunfälle, Verletzungen und Erkrankungen

**Zitat:** „Die Mitarbeiter:innen der voestalpine sind aufgrund der Branche, der Art ihrer Arbeit oder der Umgebung, in der sie arbeiten, beruflichen Gefahren und Risiken ausgesetzt, die zu Unfällen, Verletzungen, Krankheiten oder Erkrankungen führen können.“

**Treffertyp:** `exakt_mehrdeutig`  (weitere Fundstellen: 249)

**Umgebung im Bericht:**

> ...n zu erkennen und Schutzmaßnahmen anzuwenden. Mitarbeiter:innen und Fremdarbeits- kräfte Arbeitsunfälle, Verletzungen und Berufskrankheiten Die Mitarbeiter:innen der voestalpine sind aufgrund der Branche, der Art ihrer Arbeit oder der Umgebung, in der sie arbeiten, beruflichen Gefahren und Risiken ausgesetzt, die zu Unfällen, Verletzungen, Krankheiten oder Erkrankungen führen können. Eine regelmäßige Bewertung der Risiken und die Definition von Schutzmaßnahmen reduzieren Schadensschwere und/oder Eintrittswahrscheinlichkeit. Mitarbeiter:innen und Fremdarbeits- kräfte


### VOE-080 | PDF-Seite 245 | strategische_prioritaeten

**Aussage:** Steigerung des Anteils weiblicher Führungskräfte auf 18 % bis 2030

**Zitat:** „Die Konzernstrategie sieht vor, den Anteil weiblicher Führungskräfte bis 2030 von 14 % auf 18 % zu erhöhen. Im Fokus stehen dabei auch die Aktivitäten auf den drei Ebenen Positionierung, Halten sowie Begleiten/Fordern/Fördern.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...ergreifenden Arbeitsgruppen oder in bestehenden Competence Teams, teilweise auch mit externer Unterstützung. IM ZENTRUM: FEMALE EMPOWERMENT Die Konzernstrategie sieht vor, den Anteil weiblicher Führungskräfte bis 2030 von 14 % auf 18 % zu erhöhen. Im Fokus stehen dabei auch die Aktivitäten auf den drei Ebenen Positionie- rung, Halten sowie Begleiten/Fordern/Fördern. Als attraktive Arbeitgeberin ist es das Ziel der voestalpine, das Interesse von Frauen an einer Tätigkeit im Konzern zu wecken, sie langfristig zu begeistern und in ihrer beruflichen und persönlichen Entwick...


### VOE-081 | PDF-Seite 245 | strategische_prioritaeten

**Aussage:** Konzernweite Umsetzung von acht strategischen Handlungsfeldern der HR-Strategie

**Zitat:** „Zur Umsetzung der Strategie arbeitet die voestalpine konzernweit an acht strategischen Handlungsfeldern, die zentrale Hebel zur Erreichung der HR-Ziele darstellen: 1. Werte und Kulturmanagement: Aktives Management der Unternehmenswerte zur Begleitung von Technologiewandel und gesellschaftlichem Wandel“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> 245 GESCHÄFTSBERICHT 2025/26 Strategische Handlungsfelder Zur Umsetzung der Strategie arbeitet die voestalpine konzernweit an acht strategischen Handlungs- feldern, die zentrale Hebel zur Erreichung der HR-Ziele darstellen: 1. W erte und Kulturmanagement: Aktives Management der Unternehmenswerte zur Begleitung von Technologiewandel und gesellschaftlichem Wandel 2. E mployer Branding: Stärkung der Position der voestalpine als glaubwürdige und attraktive Arbeitgeberin durch zielgruppenorientierte Maßnahmen 3. F emale Empowerment: Erhöhung des Frauenanteils in allen ...


### VOE-082 | PDF-Seite 306 | hauptrisiken / Lieferkette

**Aussage:** Nachhaltigkeitsrisiken und Verletzungen von Menschen- und Arbeitsrechten in der Lieferkette

**Zitat:** „Als Nachhaltigkeitsrisiken gelten hier mögliche Verletzungen von Gesetzen und Richtlinien in den Bereichen Menschenrechte und Umweltschutz (siehe nachfolgende Tabelle). Dazu zählt auch das Risiko möglicher Verletzungen von Menschen- und Arbeitsrechten, von dem die Arbeitskräfte in der Lieferkette betroffen sein können.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...f jene Warengruppen, die von der voestalpine regelmäßig beschafft werden und mit denen potenzielle Nachhaltigkeitsrisiken ver- bunden sind. Als Nachhaltigkeitsrisiken gelten hier mögliche Verletzungen von Gesetzen und Richt - linien in den Ber eichen Menschenrechte und Umweltschutz (siehe nachfolgende Tabelle). Dazu zählt auch das Risiko möglicher Verletzungen von Menschen- und Arbeitsrechten, von dem die Arbeits kr äfte in der Lieferkette betroffen sein können. Diese Menschenrechtsrisiken stehen im Mittelpunkt der Analy se und sind in der folgenden Tabelle zusammengefasst. RISIKOBASIERTER ANSATZ FÜR NACHHALTIGES LIEFERANT:INNEN-MANAGEMENT I. Lieferant:innen- Pr...


### VOE-083 | PDF-Seite 306 | strategische_prioritaeten

**Aussage:** Schrittweise Ausdehnung des Due-Diligence-Prozesses auf den gesamten Konzern

**Zitat:** „Zur Weiterentwicklung des Lieferkettenmanagements schafft die voestalpine derzeit die organisatorischen und prozessualen Voraussetzungen, um den bestehenden Due-Diligence-Prozess – der bislang auf Gesellschaften mit Verpflichtung nach dem Lieferkettensorgfaltspflichtengesetz (LkSG) beschränkt ist – schrittweise auf den gesamten Konzern auszudehnen.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...schließlich kleiner und mittelständischer Unternehmen (KMU). Umwelt- und Sozialkriterien sind Teil der Auswahlprozesse für Lieferant:innen. Zur Weiterentwicklung des Lieferkettenmanagements schafft die voestalpine derzeit die organisato- rischen und prozessualen Voraussetzungen, um den bestehenden Due-Diligence-Prozess – der bis- lang auf Gesellschaften mit Verpflichtung nach dem Lieferkettensorgfaltspflichtengesetz (LkSG) b eschränkt ist – schrittweise auf den gesamten Konzern auszudehnen. Dabei stehen insbesondere die Einhaltung der Menschenrechte sowie Maßnahmen zur Reduktion der CO2-Emissionen im Fokus. Das Due Diligence User Manual regelt als konzernweit gültige Richtlinie das sorgfalts...


### VOE-084 | PDF-Seite 387 | capex_ma_signale

**Aussage:** Investitionen in greentec steel durch den Ersatz von Hochöfen durch Elektrolichtbogenöfen ab 2027 und 2032 sowie in CO2-Abscheidetechnologien

**Zitat:** „In dieser sind die Investitionen in Richtung greentec steel – Ersatz von zwei der drei Hochöfen durch Elektrolichtbogenöfen mit geplanten Inbetriebnahmen ab dem Jahr 2027 und 2032 – sowie Investitionen für CO2 -Abscheidetechnologien (CCUS) enthalten.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ... wird eine stabile Bruttomarge in der Mittelfristplanung erwartet. Die 5-Jahres-Mittelfristplanung wurde um eine Grobplanungsphase ergänzt. In dieser sind die Investitionen in Richtung greentec steel – Ersatz von zwei der drei Hochöfen durch Elektrolichtbogenöfen mit geplanten Inbetriebnahmen ab dem Jahr 2027 und 2032 – sowie Investitionen für CO2 -Abscheidetechnologien (CCUS) enthalten. Darüber hinaus sind erwartete Preissteigerungen bei den Emissionszertifikaten und die sukzessive Reduktion von Gratiszertifikaten auf Basis der Maßnahmen zur CO2-Reduktion seitens der Europäischen Union bis zu...


### VOE-085 | PDF-Seite 387 | capex_ma_signale

**Aussage:** Weitgehender Abschluss der Portfoliobereinigung der HPM Division durch Unternehmensverkäufe und Standortkonsolidierungen

**Zitat:** „Die Portfoliobereinigung der HPM Division ist mit den Unternehmensverkäufen (Buderus Edelstahl und BÖHLER Profil), den Kapazitätsanpassungen bei der voestalpine BÖHLER Bleche und den weltweiten Standortkonsolidierungen weitgehend abgeschlossen.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ... als auch die Wachstumsprognosen in den regionalen Absatzmärkten der Kern- märkte, insbesondere Europa, Amerika und Asien, zugrunde gelegt. Die Portfoliobereinigung der HPM Division ist mit den Unternehmensverkäufen (Buderus Edelstahl und BÖHLER Profil), den Kapazitätsan- passungen bei der voestalpine BÖHLER Bleche und den weltweiten Standortkonsolidierungen weit - gehend abgeschlossen. 1 W orld Economic Outlook, IMF – International Monetary Fund 2 EUR OFER – Dachverband der europäischen Stahlindustrie für Stahlverbrauch Europa; über Europa hinausgehend World Steel Association 3 S&P Glob...


### VOE-086 | PDF-Seite 388 | hauptrisiken / Markt

**Aussage:** Unsicherheiten und protektionistische Maßnahmen auf dem nordamerikanischen Markt

**Zitat:** „Der nordamerikanische Markt ist aufgrund der aktuellen politischen Kräfte und der protektionistischen Maßnahmen von Unsicherheiten geprägt. In Asien wird von einer stetigen Erholung in China ausgegangen“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ... stützen sich auf externe Informationsquellen. 1 In Europa wird eine leichte Erholung und mittelfristig ein ge- dämpftes Wachstum erwartet. Der nordamerikanische Markt ist aufgrund der aktuellen politischen Kräfte und der protektionistischen Maßnahmen von Unsicherheiten geprägt. In Asien wird von einer stetigen Erholung in China ausgegangen, wobei der Rest Asiens sich langsam wieder von dem derzeit schwachen Wachstum erholen wird. Indien hat großes Wachstumspotenzial. Bei der Ermittlung der ewigen Rente wurde das letzte Planjahr als Basis herange...


### VOE-087 | PDF-Seite 388 | strategische_prioritaeten

**Aussage:** Weiterer Ausbau von Servicedienstleistungen, Digital Sales und Optimierungsprogrammen in der CGU Value Added Services

**Zitat:** „Der weitere Ausbau der Servicedienstleistungen im Planungszeitraum führt zu einer engeren Kundenbindung und einer Vertiefung der Wertschöpfung. Das konsequente Weitertreiben bereits bewährter Einsparungs- und Optimierungsprogramme sowie Vertriebsaktivitäten in margenstarken Subsegmenten wie auch Initiativen im Bereich Global Supply Chain Management und Digital Sales“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ... Sägen, Sechsseitenbearbeitung) von Material der HPM Production – über- wiegend Werkzeugstahl – aber auch von Fremdmaterial verantwortlich. Der weitere Ausbau der Servicedienstleistungen im Planungszeitraum führt zu einer engeren Kundenbindung und einer Vertiefung der Wertschöpfung. Das konsequente Weitertreiben bereits bewährter Einsparungs- und Optimierungsprogramme sowie Vertriebsaktivitäten in margenstarken Subsegmenten wie auch Ini - tiativ en im Bereich Global Supply Chain Management und Digital Sales (Kundenportale mit vollstän - diger E-Commerce-Funktionalität) stellen weitere Schwerpunkte der laufenden Aktivitäten dar, die im Planungszeitraum zu steigenden Umsätzen und einer positiven Entwicklung der...


### VOE-088 | PDF-Seite 388 | wachstumsmaerkte / Indien

**Aussage:** Indien bietet aus Sicht des Unternehmens großes Wachstumspotenzial.

**Zitat:** „In Asien wird von einer stetigen Erholung in China ausgegangen, wobei der Rest Asiens sich langsam wieder von dem derzeit schwachen Wachstum erholen wird. Indien hat großes Wachstumspotenzial.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...Der nordamerikanische Markt ist aufgrund der aktuellen politischen Kräfte und der protektionistischen Maßnahmen von Unsicherheiten geprägt. In Asien wird von einer stetigen Erholung in China ausgegangen, wobei der Rest Asiens sich langsam wieder von dem derzeit schwachen Wachstum erholen wird. Indien hat großes Wachstumspotenzial. Bei der Ermittlung der ewigen Rente wurde das letzte Planjahr als Basis herangezogen. Bei der Value Added Services wird in der ewigen Rente mit einer Wachstumsrate von 1,57 % (2024/25: 1,55 %) gerechnet. Der W...


### VOE-089 | PDF-Seite 388 | wachstumsmaerkte / China

**Aussage:** In China wird von einer stetigen Erholung ausgegangen.

**Zitat:** „In Asien wird von einer stetigen Erholung in China ausgegangen, wobei der Rest Asiens sich langsam wieder von dem derzeit schwachen Wachstum erholen wird. Indien hat großes Wachstumspotenzial.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...Der nordamerikanische Markt ist aufgrund der aktuellen politischen Kräfte und der protektionistischen Maßnahmen von Unsicherheiten geprägt. In Asien wird von einer stetigen Erholung in China ausgegangen, wobei der Rest Asiens sich langsam wieder von dem derzeit schwachen Wachstum erholen wird. Indien hat großes Wachstumspotenzial. Bei der Ermittlung der ewigen Rente wurde das letzte Planjahr als Basis herangezogen. Bei der Value Added Services wird in der ewigen Rente mit einer Wachstumsrate von 1,57 % (2024/25: 1,55 %) gerechnet. Der W...


### VOE-090 | PDF-Seite 388 | wachstumsmaerkte / Europa uebrig

**Aussage:** In Europa wird eine leichte Erholung und mittelfristig ein gedämpftes Wachstum prognostiziert.

**Zitat:** „Die internen Prognosen und Einschätzungen – die Entwicklung dieser Regionen betreffend – stützen sich auf externe Informationsquellen. 1 In Europa wird eine leichte Erholung und mittelfristig ein gedämpftes Wachstum erwartet.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...ces erfolgt über das Segment- und Regional - managemen t, welches sich auf die großen Absatzmärkte in Europa, Amerika und Asien fokussiert. Die internen Prognosen und Einschätzungen – die Entwicklung dieser Regionen betreffend – stützen sich auf externe Informationsquellen. 1 In Europa wird eine leichte Erholung und mittelfristig ein ge- dämpftes Wachstum erwartet. Der nordamerikanische Markt ist aufgrund der aktuellen politischen Kräfte und der protektionistischen Maßnahmen von Unsicherheiten geprägt. In Asien wird von einer stetigen Erholung in China ausgegangen, wob...


### VOE-091 | PDF-Seite 389 | capex_ma_signale

**Aussage:** Investitionen in eine Elektrolichtbogenofen-Anlage im Rahmen von greentec steel im Geschäftsbereich Railway Systems

**Zitat:** „Ebenso sind die Investitionen in Richtung greentec steel in der 5-Jahres-Mittelfristplanung sowie in der Grobplanungsphase für eine Elektrolichtbogenofen-Anlage und deren Erweiterung in der Vorproduktionsstufe enthalten.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...gehalten werden und sich mögliche Schwankungen in einzelnen Märkten aufgrund der weltweiten Ausrichtung des Geschäftsbereiches ausgleichen. Ebenso sind die Investitionen in Richtung greentec steel in der 5-Jahres-Mittelfristplanung sowie in der Grobplanungsphase für eine Elektrolichtbogenofen-Anlage und deren Erweiterung in der Vorproduktionsstufe enthalten. Darüber hinaus sind erwartete Preisstei- gerungen bei den Emissionszertifikaten und die sukzessive Reduktion von Gratiszertifikaten auf Basis der Maßnahmen zur CO2-Reduktion seitens der Europäischen Union bis ...


### VOE-092 | PDF-Seite 389 | strategische_prioritaeten

**Aussage:** Fortführung der Ausrichtung als Komplettanbieter im Geschäftsbereich Welding

**Zitat:** „Die strategische Ausrichtung des Geschäftsbereichs als Komplettanbieter der „Perfekten Schweißnaht“ („The Perfect Weld Seam“) wird im Planungszeitraum unverändert weiterverfolgt. Bereits eingeleitete sowie laufende Optimierungs- und Effizienzprogramme werden konsequent fortgeführt“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...gen sowie auf den verfügbaren externen Prognosen, aus denen sowohl Kosten als auch daraus abgeleitete Preisentwicklungen abgeleitet wurden. Die strategische Ausrichtung des Geschäftsbereichs als Komplettanbieter der „Perfekten Schweißnaht“ („The Perfect Weld Seam“) wird im Planungszeitraum unverändert weiterverfolgt. Bereits eingeleitete sowie laufende Optimierungs- und Effizienzprogramme werden konsequent fortgeführt und durch kontinuierliche Verbesserungsmaßnahmen ergänzt. Zusammengefasst wird in der Planung – abge - leit et von den Markterwartungen – von einem moderaten Volumenwachstum bei leicht verbesserter Bruttomarge...


### VOE-093 | PDF-Seite 414 | hauptrisiken / Finanzierung

**Aussage:** Risiko der Nichterfüllung von Zahlungsverpflichtungen (Liquiditätsrisiko)

**Zitat:** „Das Liquiditätsrisiko bezeichnet das Risiko, Zahlungsverpflichtungen nicht durch Lieferung von Zahlungsmitteln erfüllen zu können. Ziel des Konzerns in der Steuerung der Liquidität ist es, sicherzustellen, dass stets ausreichend liquide Mittel verfügbar sind“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...z um 10 % darstellt. In der Analyse wird unterstellt, dass alle anderen Einflussfaktoren konstant bleiben. LIQUIDITÄTSRISIKO – FINANZIERUNG Das Liquiditätsrisiko bezeichnet das Risiko, Zahlungsverpflichtungen nicht durch Lieferung von Zahlungsmitteln erfüllen zu können. Ziel des Konzerns in der Steuerung der Liquidität ist es, sicherzustellen, dass stets ausreichend liquide Mittel verfügbar sind, um unter normalen wie auch unter angespannten Bedingungen den Zahlungs- verpflichtungen bei Fälligkeit nachkommen zu können.


### VOE-094 | PDF-Seite 418 | hauptrisiken / Finanzierung

**Aussage:** Ausfall von Forderungen bzw. Bonitätsrisiko von Geschäftspartnern

**Zitat:** „Das Bonitätsrisiko bezeichnet Vermögensverluste, die aus der Nichterfüllung von Vertragsverpflichtungen einzelner Geschäftspartner:innen entstehen können. Das Management des Bonitätsrisikos von Veranlagungs- und Derivatgeschäften wird in internen Richtlinien reglementiert.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...ür sonstige Finanzverbindlichkeiten 0,9 0,1 0,2 0,1 0,0 0,0 Summe Zinslast 76,1 72,1 151,0 136,5 54,4 51,5 Mio . EUR KREDIT-/BONITÄTSRISIKO Das Bonitätsrisiko bezeichnet Vermögensverluste, die aus der Nichterfüllung von Vertragsverpflich- tungen einzelner Geschäftspartner:innen entstehen können. Das Management des Bonitätsrisikos von Veranlagungs- und Derivatgeschäften wird in internen Richtlinien reglementiert. Es sind alle Veranlagungen und Derivatgeschäfte je Kontrahent:in limitiert, wobei die Höhe des Limits vom Rating der Bank abhängig ist. Die Zahlungsmittel und Zahlungsmitteläquivalente bestehen überwiegend g...


### VOE-095 | PDF-Seite 421 | hauptrisiken / Finanzierung

**Aussage:** Währungsrisiko durch Rohstoffeinkäufe in USD und weltweite Fremdwährungsexposures

**Zitat:** „Die größte Währungsposition im Konzern entsteht durch Einkäufe von Rohstoffen in US-Dollar, durch die weltweite Geschäftstätigkeit des voestalpine-Konzerns ergeben sich jedoch auch Währungs-exposures in diversen anderen Währungen.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> 421 GESCHÄFTSBERICHT 2025/26 WÄHRUNGSRISIKO Die größte Währungsposition im Konzern entsteht durch Einkäufe von Rohstoffen in US-Dollar, durch die weltweite Geschäftstätigkeit des voestalpine-Konzerns ergeben sich jedoch auch Währungs - e xposures in diversen anderen Währungen. Durch die Implementierung eines rollierenden Foreign-Currency-Nettings werden ein- und ausgehende Cashflows in den jeweiligen Währungen gegengerechnet. Durch den dadurch erzielten Natural Hedge wird Risiko ...


### VOE-096 | PDF-Seite 422 | hauptrisiken / Finanzierung

**Aussage:** Zinsänderungs- bzw. Cashflow-Risiko bei variabel verzinsten Finanzinstrumenten

**Zitat:** „Die voestalpine AG unterliegt primär einem Cashflow-Risiko (Risiko, dass sich der Zinsaufwand bzw. Zinsertrag zum Nachteil verändert) bei variabel verzinsten Finanzinstrumenten.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...,5140 –21,5 –19,6 2,0 –23,9 –2,4 CAD 28,9 1,6022 18,0 16,4 –1,6 20,0 2,0 Sonstige 0,8 0,7 –0,1 0,9 0,1 Summe 31,3 –38,2 Mio. EUR ZINSRISIKO Die voestalpine AG unterliegt primär einem Cashflow-Risiko (Risiko, dass sich der Zinsaufwand bzw. Zinsertrag zum Nachteil verändert) bei variabel verzinsten Finanzinstrumenten. Der dargestellte Bestand umfasst alle zinsreagiblen Finanzinstrumente (Kredite, Money Market, begebene und gekauf- te Wertpapiere sowie Zinsderivate). Das primäre Ziel des Zinsmanagements ist die Optimierung d...


### VOE-097 | PDF-Seite 435 | capex_ma_signale

**Aussage:** Auszahlungen für Unternehmenserwerbe im Berichtsjahr

**Zitat:** „Im Cashflow aus der Investitionstätigkeit sind aus Unternehmenserwerben Zugänge an Zahlungsmitteln und Zahlungsmitteläquivalenten in Höhe von 0,6 Mio. EUR (2024/25: 0,0 Mio. EUR) enthalten und ein Kaufpreis in Höhe von 30,7 Mio. EUR“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...ks. Die Auswirkungen von Konsolidierungskreisänderungen wurden eliminiert und sind im Cash- flow aus der Investitionstätigkeit ausgewiesen. Im Cashflow aus der Investitionstätigkeit sind aus Unternehmenserwerben Zugänge an Zahlungsmit- teln und Zahlungsmitteläquivalenten in Höhe von 0,6 Mio. EUR (2024/25: 0,0 Mio. EUR) enthalten und ein Kaufpreis in Höhe von 30,7 Mio. EUR (2024/25: 19,0 Mio. EUR) ist abgegangen (siehe Punkt C.2. Konsolidierungskreisänderungen, Abschnitt Unternehmenserwerbe und sonstige Zugänge zum Konsolidierungskreis). Aufgrund des Abganges von Tochtergesell...


### VOE-098 | PDF-Seite 435 | capex_ma_signale

**Aussage:** Abgang von Tochtergesellschaften und Veräußerungsgruppen mit entsprechenden Cashflows

**Zitat:** „Aufgrund des Abganges von Tochtergesellschaften im laufenden Geschäftsjahr sind 1,5 Mio. EUR (2024/25: 0,0 Mio. EUR) Zahlungsmittel und Zahlungsmitteläquivalente abgeflossen und es ist ein Verkaufserlös in der Höhe von 4,7 Mio. EUR zugeflossen.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ... abgegangen (siehe Punkt C.2. Konsolidierungskreisänderungen, Abschnitt Unternehmenserwerbe und sonstige Zugänge zum Konsolidierungskreis). Aufgrund des Abganges von Tochtergesellschaften im laufenden Geschäftsjahr sind 1,5 Mio. EUR (2024/25: 0,0 Mio. EUR) Zahlungsmittel und Zahlungsmitteläquivalente abgeflossen und es ist ein Verkaufserlös in der Höhe von 4,7 Mio. EUR zugeflossen. Darüber hinaus sind aus dem letztjährigen Abgang einer Veräußerungsgruppe 9,7 Mio. EUR Kaufpreisrückvergütung/-anpassung im Berichts- jahr zugeflossen (2024/25: 47 Mio. EUR abgeflossen). Aus dem Abgang von nic...


---

# Wienerberger AG  (wienerberger_2025.pdf, 36 Elemente)


### WIE-099 | PDF-Seite 7 | capex_ma_signale

**Aussage:** Investitionen in moderne Rohrproduktionsstätten zur Stärkung der technologischen Führerschaft

**Zitat:** „Investitionen in unseren modernen industriellen Footprint – darunter unsere hochinnovative Rohrproduktionsstätte in Schweden – unterstreichen unser Bekenntnis zu technologischer Führerschaft und nachhaltigen Infrastrukturlösungen.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...er Neubautätigkeit blieben die Margen in Europa robust und belegen die Widerstandsfähigkeit unseres infrastruktur- fokussierten Portfolios. Investitionen in unseren modernen industriellen Footprint – darunter unsere hochinnovative Rohrproduktionsstätte in Schweden – unterstreichen unser Bekenntnis zu technologischer Führerschaft und nachhaltigen Infrastrukturlösungen. Finanzielle Disziplin und operative Exzellenz Ein zentrales Element unseres Erfolgs im Jahr 2025 war unser konsequenter Fokus auf operative Exzellenz und Effizienz. Unser Programm „Fit for Growth“ leistete ein...


### WIE-100 | PDF-Seite 8 | capex_ma_signale

**Aussage:** Evaluierung der Italcer-Gruppe als potenzielles Akquisitionsziel

**Zitat:** „Im Dezember 2025 fanden zudem strategische Beratungen mit dem Management im Hinblick auf die Evaluierung der Italcer- Gruppe als mögliches Akquisitionsziel statt.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...sserungs-, Dachrinnen und Kabelkanalsysteme, und GSEi, einem in Frankreich ansässi- gen Anbieter von dachintegrierten Photovoltaiklösungen. Im Dezember 2025 fanden zudem strategische Beratungen mit dem Management im Hinblick auf die Evaluierung der Italcer- Gruppe als mögliches Akquisitionsziel statt. Der Prüfungs- und Risikoausschuss beschäftigte sich vorran- ging mit der Vorbereitung und Prüfung des Konzern- und Ein- zelabschlusses, der Frage der Unabhängigkeit des Abschluss- prüfers sowie mit Themen des ...


### WIE-101 | PDF-Seite 30 | strategische_prioritaeten

**Aussage:** Positionierung als führender Komplettanbieter von Lösungen für die Gebäudehülle sowie für Energie- und Wassermanagement in der Infrastruktur

**Zitat:** „Unser Ziel ist die konsequente Steigerung der Wertschöpfung sowie unsere Positionierung als führender Komplettanbieter von Lösungen für die Gebäudehülle sowie für Energie- und Wassermanagement in der Infrastruktur .“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...ung, Operational Excellence und Nach- haltigkeit spielen nicht nur heute, sondern auch in der Zukunft von wienerberger eine zentrale Rolle. Unser Ziel ist die konse- quente Steigerung der Wertschöpfung sowie unsere Positio- nierung als führender Komplettanbieter von Lösungen für die Gebäudehülle sowie für Energie- und Wassermanagement in der Infrastruktur . Als solcher möchten wir auch in Zukunft die Bauindustrie aktiv mitgestalten und das Leben der Menschen weiter verbessern. Forschung und Entwicklung Forschung und Entwicklung (F&E) ist von großer strategisc...


### WIE-102 | PDF-Seite 30 | strategische_prioritaeten

**Aussage:** Fokus auf Forschung und Entwicklung für Energieeffizienz, smarte Funktionalitäten und Nachhaltigkeitsziele

**Zitat:** „Unser Ziel ist die Entwicklung von Lösungen, die einen umweltfreundlichen, schnellen und einfachen Einbau auf der Baustelle ermöglichen, zum Klimaschutz und zur Energieeffizienz von Gebäuden beitragen und spürbaren Mehrwert für unsere Kunden schaffen.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...ptimierung von Produkteigen- schaften, der Steigerung der Energieeffizienz und der Bereit- stellung smarter und digitaler Funktionalitäten. Unser Ziel ist die Entwicklung von Lösungen, die einen umweltfreundlichen, schnellen und einfachen Einbau auf der Baustelle ermöglichen, zum Klimaschutz und zur Energieeffizienz von Gebäuden bei- tragen und spürbaren Mehrwert für unsere Kunden schaffen. Im keramischen Bereich sind die F&E-Aktivitäten auf die Entwicklung innovativer Produkte ausgerichtet, darunter ver- besserte gedämmte Wandsysteme und ausgereifte Dachlösun- gen mit integrierter Solartechnol...


### WIE-103 | PDF-Seite 42 | capex_ma_signale

**Aussage:** Ausgaben für Unternehmensakquisitionen beliefen sich 2025 auf EUR 24 Mio

**Zitat:** „Im Geschäftsjahr 2025 beliefen sich die Ausgaben für Unternehmensakquisitionen auf EUR 24 Mio (2024: EUR 637 Mio). Alle T ransaktionen standen in vollem Einklang mit den strategischen und finanziellen Kriterien des Konzerns und konzentrierten sich auf wertsteigerndes Wachstum ohne Beeinträchtigung der Bilanzstärke.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ... Übernahme von VETA France, einem Hersteller von Fassadenpaneelen mit integrier- ten Dämmsystemen, stärkte das Fassadengeschäft der Gruppe. Im Geschäftsjahr 2025 beliefen sich die Ausgaben für Unter- nehmensakquisitionen auf EUR 24 Mio (2024: EUR 637 Mio). Alle T ransaktionen standen in vollem Einklang mit den strategi- schen und finanziellen Kriterien des Konzerns und konzentrier- ten sich auf wertsteigerndes Wachstum ohne Beeinträchtigung der Bilanzstärke. Darüber hinaus erwarb der Konzern die verbleibenden Anteile an GSEi in Höhe von EUR 24 Mio. Corporate Governance Bericht | Konzernlagebericht | Konzernabschluss


### WIE-104 | PDF-Seite 42 | capex_ma_signale

**Aussage:** Übernahme von MFP Ltd. zur Stärkung der Rohrplattform

**Zitat:** „In Irland und Großbritannien wurde durch die Übernahme von MFP Ltd., einem Spezialisten für Entwässerungs-, Dachrinnen- und Kabelkanalsysteme, die Plattform für Rohrlösungen und die regionale Präsenz weiter gestärkt.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...en Akquisitionen fort, um seine strategische Positionierung insbesondere in den Bereichen Renovierung und Infrastrukturlösungen zu stärken. In Irland und Großbritannien wurde durch die Übernahme von MFP Ltd., einem Spezialisten für Entwässerungs-, Dachrinnen- und Kabelkanalsysteme, die Plattform für Rohrlösungen und die regionale Präsenz weiter gestärkt. Die Übernahme von VETA France, einem Hersteller von Fassadenpaneelen mit integrier- ten Dämmsystemen, stärkte das Fassadengeschäft der Gruppe. Im Geschäftsjahr 2025 beliefen sich die Ausgaben für Unter- nehmen...


### WIE-105 | PDF-Seite 42 | capex_ma_signale

**Aussage:** Erwerb der verbleibenden Anteile an GSE Integration

**Zitat:** „Darüber hinaus wurden EUR 24 Mio für den Erwerb von nicht beherrschenden Anteilen (2024: EUR 0 Mio) aufgewendet, die sich auf die verbleibende Beteiligung an GSE Integration (GSEi) beziehen.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...ktienrückkäufe von EUR 29 Mio (2024: EUR 34 Mio) sowie Auszahlungen für Leasingverbindlichkeiten in Höhe von EUR 77 Mio (2024: EUR 72 Mio). Darüber hinaus wurden EUR 24 Mio für den Erwerb von nicht beherrschenden Anteilen (2024: EUR 0 Mio) aufgewendet, die sich auf die verbleibende Beteiligung an GSE Integration (GSEi) beziehen. Zum Jahresende 2025 verfügte wienerberger über eine solide Liquidität in Höhe von EUR 963 Mio (2024: EUR 1.012 Mio), bestehend aus liquiden Mitteln sowie zugesagten und vollstän- dig ungezogenen Kreditlinien. ...


### WIE-106 | PDF-Seite 47 | capex_ma_signale

**Aussage:** Übernahme der Italcer Group im Jahr 2026 vereinbart

**Zitat:** „Am 24. Februar 2026 hat wienerberger eine verbindliche Vereinbarung zum Erwerb von Italcer unterzeichnet, einem führenden Hersteller hochwertiger keramischer Lösungen mit Produktionsstandorten in Italien und Spanien. Der Abschluss der T ransaktion wird – vorbehaltlich der behördlichen Genehmigungen – im zweiten Quartal 2026 erwartet.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...ngfristigen Zinsen verbleiben auf hohem Niveau. Ein wichtiger strategischer Schritt für wienerberger ist die Akquisition der Italcer Group. Am 24. Februar 2026 hat wiener- berger eine verbindliche Vereinbarung zum Erwerb von Italcer unterzeichnet, einem führenden Hersteller hochwertiger keramischer Lösungen mit Produktionsstandorten in Italien und Spanien. Der Abschluss der T ransaktion wird – vorbehalt- lich der behördlichen Genehmigungen – im zweiten Quartal 2026 erwartet. Vor diesem Hintergrund prognostiziert wienerberger für das Geschäftsjahr 2026 – unter Einbeziehung eines erwarteten Ergebnisbeitrags von Italcer – ein operatives EBITDA von rund EUR 810 Mio. (2025: EUR 754...


### WIE-107 | PDF-Seite 47 | hauptrisiken / Lieferkette

**Aussage:** Störungen der Lieferketten und Logistikströme sowie Versorgungsengpässe infolge geopolitischer Konflikte

**Zitat:** „Dieser Konflikt hat Auswirkungen auf wichtige Verkehrs- und Handelsströme. Seither ist neben Störungen entlang von Lieferketten und Logistikströmen eine erhöhte Volatilität an den globalen Rohstoff- und Energiemärkten zu beobachten.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...n Rückgang des Preisanstiegs auf 1,9 % (2025: 2,1 %). Am 28. Februar 2026 begann eine militärische Auseinander- setzung im mittleren Osten. Dieser Konflikt hat Auswirkungen auf wichtige Verkehrs- und Handelsströme. Seither ist neben Störungen entlang von Lieferketten und Logistikströmen eine erhöhte Volatilität an den globalen Rohstoff- und Energie- märkten zu beobachten. Die Auswirkungen beschränken sich daher nicht nur auf höhere Energiepreise, sondern umfassen breitere Störungen bei der Rohstoffversorgung und Logistik. Auswirkungen auf die Finanzmärkte sind nicht auszuschl...


### WIE-108 | PDF-Seite 47 | hauptrisiken / Markt

**Aussage:** Preisanstiege bei Energie, Rohstoffen und Logistik durch geopolitische Konflikte

**Zitat:** „Für wienerberger kann dies zu deutlichen Preissteigerungen insbesondere in den Bereichen Energie, Rohstoffe und Logistik führen und in Versorgungsengpässen resultieren. wienerberger überwacht die Situation kontinuierlich und ergreift Maßnahmen, um die Versorgungssicherheit sicherzustellen.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ..., sondern umfassen breitere Störungen bei der Rohstoffversorgung und Logistik. Auswirkungen auf die Finanzmärkte sind nicht auszuschließen. Für wienerberger kann dies zu deutlichen Preissteigerungen insbesondere in den Bereichen Energie, Rohstoffe und Logistik führen und in Versorgungsengpässen resultieren. wienerberger überwacht die Situation kontinuierlich und ergreift Maß- nahmen, um die Versorgungssicherheit sicherzustellen. Eine Quantifizierung der Auswirkungen ist aufgrund der Dynamik des Konflikts zum jetzigen Zeitpunkt nicht möglich und daher nicht in unserem Ausblick für das Jahr 2026 berücksichtigt. wienerberger Für 2026 e...


### WIE-109 | PDF-Seite 48 | hauptrisiken / Regulierung

**Aussage:** Übergangsrisiken und physische Risiken infolge des Klimawandels und der Wende zu einer kohlenstoffarmen Wirtschaft

**Zitat:** „Seit 2020 unterstützen wir daher die Empfehlungen der T ask Force on Climate-related Financial Disclosures (TCFD) in Bezug auf die Identifizierung, Analyse und Bewertung von physischen Risiken und Übergangsrisiken im Zusammenhang mit der Auswirkung der Wende zu einer kohlenstoffarmen Wirtschaft“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...denen Risiken. Die Identifizierung und Analyse klimabezogener Risiken ist T eil des umfassenden Risikomanagementansatzes von wienerberger . Seit 2020 unterstützen wir daher die Empfehlungen der T ask Force on Climate-related Financial Disclosures (TCFD) in Bezug auf die Identifizierung, Analyse und Bewertung von physischen Risiken und Übergangsrisiken im Zusammenhang mit der Auswirkung der Wende zu einer kohlenstoffarmen Wirtschaft (z.B. Reputationsrisiken, regulatorische Risiken, Marktrisiken und T echnologierisiken). Außerdem informieren wir über die Einschätzung von Klimarisiken gemäß den Anforderungen der CSRD-Richtlinie (Corporate S...


### WIE-110 | PDF-Seite 52 | hauptrisiken / Markt

**Aussage:** Abhaengigkeit von den Konjunkturzyklen der Bauindustrie und Nachfrageschwankungen

**Zitat:** „Unvorteilhafte Entwicklungen einiger oder all dieser Einflussgrößen können einen negativen Einfluss auf die Nachfrage nach Produkten und Systemlösungen von wienerberger , die abgesetzten Mengen und das Preisniveau haben.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ... Zyklen der Bauaktivität sind deutlich langfristiger als in anderen Bereichen und verlaufen in unterschiedlichen Märkten zeitlich versetzt. Unvorteilhafte Entwicklungen einiger oder all dieser Einfluss- größen können einen negativen Einfluss auf die Nachfrage nach Produkten und Systemlösungen von wienerberger , die abgesetzten Mengen und das Preisniveau haben. Zyklische Schwankungen der Nachfrage bergen das Risiko von Überkapa- zitäten, die einen erhöhten Preisdruck, eine Verringerung der Margen sowie ungedeckte Kosten in der Produktion zur Folge haben können. Ris...


### WIE-111 | PDF-Seite 52 | wachstumsmaerkte / Europa uebrig

**Aussage:** Zentral- und osteuropaeische Maerkte gelten wegen Nachholbedarfs langfristig als Wachstummaerkte

**Zitat:** „Die zentral- und osteuropäischen Märkte betrachtet wienerberger auch aufgrund des Nachholbedarfs im Wohnungsneubau und in der Infrastruktur langfristig als Wachstumsmärkte. Diese Märkte zeigen erfahrungsgemäß eine höhere Volatilität“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...eschäft. Die Produktionskapa- zitäten werden daher laufend analysiert und durch entspre- chende Maßnahmen den Marktgegebenheiten angepasst. Die zentral- und osteuropäischen Märkte betrachtet wienerber- ger auch aufgrund des Nachholbedarfs im Wohnungsneubau und in der Infrastruktur langfristig als Wachstumsmärkte. Diese Märkte zeigen erfahrungsgemäß eine höhere Volatilität und können Risiken aus einer schwächeren Nachfrage und einem höheren Preisdruck mit sich bringen. Risiken im Zusammenhang mit konkurrierenden Baumaterialien Darüber hinaus stehen die Produkte von wienerberge...


### WIE-112 | PDF-Seite 53 | hauptrisiken / Lieferkette  **PRUEFEN**

**Aussage:** Preis- und Verfuegbarkeitsrisiken bei Rohstoffen und Zusatzstoffen

**Zitat:** „Neben dem Preisrisiko besteht auch ein Risiko aus der Versorgungssicherheit mit ausreichenden Rohstoffen. Eine Unterbrechung der Versorgung zieht unweigerlich einen Ausfall der Produktion nach sich.“

**Treffertyp:** `exakt_mehrdeutig`  (weitere Fundstellen: 182)

**Umgebung im Bericht:**

> ...lieren bzw. an den Markt anzupassen. Rasches Handeln im Preismanage- ment ist entscheidend, um nachhaltig profitable Ergebnisse zu sichern. Neben dem Preisrisiko besteht auch ein Risiko aus der Versorgungssicherheit mit ausreichenden Rohstoffen. Eine Unterbrechung der Versorgung zieht unweigerlich einen Aus- fall der Produktion nach sich. Mit wenigen Ausnahmen gibt es für die Rohstoffversorgung alternative Lieferantenoptionen, um dem Versorgungsrisiko zu begegnen. Risiken im Zusammenhang mit saisonalen Marktschwankungen Die Baustoff- als auch...


### WIE-113 | PDF-Seite 54 | capex_ma_signale

**Aussage:** Rentabilitaetsabhaengigkeit bei Akquisitions- und Wachstumsinvestitionen

**Zitat:** „Zur Steigerung des wienerberger Unternehmenswerts werden neben der laufenden Optimierung (Operational Excellence) Produktinnovationen sowie interne und externe Wachstumsprojekte durchgeführt. Die zukünftige Rentabilität dieser Projekte ist in hohem Maße von“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...cht T eil von CBAM und erhalten weiterhin die zuerkannten Carbon Leakage Gratiszuteilungen. Abhängigkeit von zukünftigen Wachstumsprojekten Zur Steigerung des wienerberger Unternehmenswerts werden neben der laufenden Optimierung (Operational Excellence) Produktinnovationen sowie interne und externe Wachstums- projekte durchgeführt. Die zukünftige Rentabilität dieser Projekte ist in hohem Maße von der Investitionshöhe bzw. den Akquisitionspreisen sowie der Marktentwicklung abhängig. Alle Investitionsmaßnahmen müssen daher den Rentabilitätszielen für unsere Wachstumsprojekte gerecht werden. Weiters erg...


### WIE-114 | PDF-Seite 54 | hauptrisiken / Regulierung

**Aussage:** Risiken bei M&A-Transaktionen durch kartellrechtliche Genehmigungsverfahren

**Zitat:** „Abhängig von der Marktstellung in einzelnen Ländern sowie der Größe von beabsichtigten Akquisitionen unterliegen Transaktionen wettbewerbsrechtlichen Genehmigungsverfahren. Dadurch könnten sich bei Akquisitionen bzw. Zusammenschlüssen Verzögerungen bzw.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...e Projekte werden deshalb vor dem Start einer umfassenden qualitativen und quantitativen Analyse unterzogen. Risiken bei M&A-T ransaktionen Abhängig von der Marktstellung in einzelnen Ländern sowie der Größe von beabsichtigten Akquisitionen unterliegen T rans- aktionen wettbewerbsrechtlichen Genehmigungsverfahren. Dadurch könnten sich bei Akquisitionen bzw. Zusammen- schlüssen Verzögerungen bzw. in einzelnen Fällen auch Unter- sagungen von Übernahmen ergeben. wienerberger prüft kar- tellrechtliche Risiken bereits intensiv im Vorfeld mit nationalen und internationalen juristischen und betriebswirt...


### WIE-115 | PDF-Seite 55 | hauptrisiken / Lieferkette

**Aussage:** Risiken aus geopolitischen Spannungen und Lieferkettenstoerungen

**Zitat:** „Mögliche Risiken ergeben sich insbesondere aus Störungen internationaler Lieferketten, steigenden Energie- und Rohstoffpreisen, Handelsbeschränkungen oder erhöhten politischen Unsicherheiten in einzelnen Märkten.“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...oliti- sche Spannungen oder Sanktionen – können erhebliche Aus- wirkungen auf die globalen Wirtschafts- und Lieferkettenstruk- turen haben. Mögliche Risiken ergeben sich insbesondere aus Störungen internationaler Lieferketten, steigenden Energie- und Rohstoffpreisen, Handelsbeschränkungen oder erhöh- ten politischen Unsicherheiten in einzelnen Märkten. Diese Faktoren können zu Kostensteigerungen, Verzögerungen in der Beschaffung sowie zu einer erhöhten Volatilität auf Absatz- und Beschaffungsmärkten führen. Globale Gesundheitskrisen oder Pandemien können z...


### WIE-116 | PDF-Seite 55 | hauptrisiken / Regulierung

**Aussage:** Verschaerfte Vorschriften und politische Massnahmen zur Bekaempfung des Klimawandels

**Zitat:** „Zu den zentralen Risiken zählt, dass Regierungen Vorschriften und politische Maßnahmen zur Bekämpfung des Klimawandels, wie z. B. Emissionsreduktionsziele, verabschieden könnten.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...uswirkungen, Risiken und Chancen gemäß der Corporate Sustainability Reporting Directive (CSRD). Risiken im Zusammenhang mit dem Klimawandel Zu den zentralen Risiken zählt, dass Regierungen Vorschriften und politische Maßnahmen zur Bekämpfung des Klimawandels, wie z. B. Emissionsreduktionsziele, verabschieden könnten. Die Einführung von zusätzlichen CO2-Preismechanismen oder Steu- ern kann die Produktionskosten erhöhen, die Gesamtrentabili- tät gefährden und Investitionszyklen beschleunigen, während verzögerte und unzureich...


### WIE-117 | PDF-Seite 55 | hauptrisiken / Technologie

**Aussage:** Risiken im Zusammenhang mit Cybersicherheit und IT-Ausfaellen

**Zitat:** „Risiken eines Ausfalls unserer zentral geführten konzernweiten Datenverarbeitung aufgrund von Elementarereignissen oder Cyberangriffen werden durch parallele Installation der Systeme in räumlich getrennten Rechenzentren und Cloud-Lösungen vermindert.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...lgemeine Risikomanagementstrategie und das interne Kontrollsystem von wienerberger eingebettet. Risiken im Zusammenhang mit Cybersicherheit Risiken eines Ausfalls unserer zentral geführten konzernweiten Datenverarbeitung aufgrund von Elementarereignissen oder Cyberangriffen werden durch parallele Installation der Systeme in räumlich getrennten Rechenzentren und Cloud-Lösungen vermindert. Das Cyber-Sicherheitsteam schult die Mitarbeiter und trainiert regelmäßig Notfälle. Damit wird eine kontinuier- liche Verbesserung der internen Betriebsfortführungskonzepte ermöglicht und ein möglicher Schaden...


### WIE-118 | PDF-Seite 56 | strategische_prioritaeten

**Aussage:** Erreichung der Netto-Null-Emissionen bis 2050 und Umsetzung des Nachhaltigkeitsprogramms 2023–2026

**Zitat:** „Um dieses Ziel zu verwirklichen, setzen wir uns für den Klimaschutz ein und tragen dazu bei, die Vorgaben des europäischen Green Deal umzusetzen, mit dem klaren Ziel der Netto-Null-Emissionen bis 2050.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ... stets als unsere Verantwortung angesehen, sicherzustellen, dass zukünftige Generationen die höchstmögliche Lebensqualität genießen können. Um dieses Ziel zu verwirklichen, setzen wir uns für den Klimaschutz ein und tragen dazu bei, die Vorgaben des europäischen Green Deal umzusetzen, mit dem klaren Ziel der Netto-Null-Emissionen bis 2050. Zur Umsetzung haben wir das Nachhaltigkeitsprogramm 2023–2026 eingefüh rt, das klare Ziele für die wesentlichen Aspekte unseres Geschäfts definiert. Die Ergebnisse der ersten beiden Jahre bestätigen die strate...


### WIE-119 | PDF-Seite 60 | capex_ma_signale

**Aussage:** Ganzheitlicher Ansatz des Managements im Umgang mit Risiken und Chancen umfasst Fusionen und Übernahmen (M&A) sowie den Ausbau des Werksnetzes.

**Zitat:** „Bei Minderung von Risiken und Nutzung von Chancen wählt das Management von wienerberger einen ganzheitlichen Ansatz, der die Bereiche Produktentwicklung, Fusionen und Übernahmen (Mergers and Acquisitions, M&A), Ausbau des Werksnetzes und Auswahl der Energieträger sowie eine breite Palette an Initiativen“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...cheidungen. Geleitet werden sie dabei von der strategischen Vision von wienerberger , die im Nach- haltigkeitsprogramm 2026 dargelegt wird. Bei Minderung von Risiken und Nutzung von Chancen wählt das Management von wienerberger einen ganzheitlichen Ansatz, der die Bereiche Produktentwicklung, Fusionen und Übernahmen (Mergers and Acquisitions, M&A), Ausbau des Werksnetzes und Auswahl der Energieträger sowie eine breite Palette an Initiativen zur Reduktion von Scope-3-Emissionen umfasst. Dazu zählt auch die Berücksichtigung von Spannungsfeldern im Zusammen- hang mit diesen Auswirkungen, Risiken und Chancen. GOV-3 Einbeziehung der nachhaltig- keitsb...


### WIE-120 | PDF-Seite 71 | hauptrisiken / Markt

**Aussage:** Physische Klimarisiken und klimabedingte Gefahren für Vermögenswerte und Geschäftsaktivitäten über kurz-, mittel- und langfristige Zeithorizonte

**Zitat:** „wienerberger hat eine Analyse der physischen Klimarisiken durchgeführt, um festzustellen, ob klimabedingte Gefahren Risiken für Vermögenswerte und Geschäftsaktivitäten über einen kurz- (bis 2030), mittel (bis 2040) und langfristigen Zeithorizont (bis 2050) darstellen könnten.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...gewährleisten diese eine umfassende Bewertung plausibler Unsicherheiten im Einklang mit den Zielen des Pariser Abkommens. Physische Risiken wienerberger hat eine Analyse der physischen Klimarisiken durchgeführt, um festzustellen, ob klimabedingte Gefahren Risiken für Vermögenswerte und Geschäftsaktivitäten über einen kurz- (bis 2030), mittel (bis 2040) und langfristigen Zeit- horizont (bis 2050) darstellen könnten. Diese Zeithorizonte ermöglichen es, sowohl unmittelbare als auch langfristige Risiken zu erfassen. Die erwartete betriebliche Nutzungsdauer unserer wienerberger-Standorte erstreckt sich in der Szenario- anal...


### WIE-121 | PDF-Seite 82 | capex_ma_signale

**Aussage:** Rückgang des CapEx-Anteils nach der Terreal-Übernahme im Vorjahr und Ausbleiben vergleichbarer Zukäufe im Jahr 2025

**Zitat:** „Der taxonomiekonforme Anteil der CapEx im Berichtszeitraum erreichte 50,8 % des gesamten CapEx (2024: 81,1 %). Der Betrag für 2024 ist aufgrund der Übernahme von T erreal, dessen Dachproduktion eine taxonomiekonforme Geschäftstätigkeit war , erhöht. Im Jahr 2025 erfolgte keine Akquisition. in diesem Ausmaß.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...ur Wirtschaftstätigkeiten im Umweltziel Klimaschutz identifiziert wurden, können Doppelzählungen zu mehreren Umweltzielen vermieden werden. Der taxonomiekonforme Anteil der CapEx im Berichtszeitraum erreichte 50,8 % des gesamten CapEx (2024: 81,1 %). Der Betrag für 2024 ist aufgrund der Übernahme von T erreal, dessen Dachproduktion eine taxonomiekonforme Geschäftstätigkeit war , erhöht. Im Jahr 2025 erfolgte keine Akquisition. in diesem Ausmaß. KPI-Bericht CapEx Geschäftsjahr 2025 Wirtschaftstätigkeiten N r. T axonomiefähiger KPI (Anteil des taxonomiefä- higen Umsatzes/CapEx/ OpEx) T axonomiekonformer KPI (Wert des taxonomiekonformen Umsatzes/CapEx/O...


### WIE-122 | PDF-Seite 83 | strategische_prioritaeten

**Aussage:** Konzentration auf nachhaltige und klimafreundliche Produkte mit dem Ziel des Umsatzes aus Netto-Null-Gebäuden im Rahmen des Nachhaltigkeitsprogramms 2026

**Zitat:** „Die Anpassungsmaßnahmen stehen im Zusammenhang mit der Strategie und dem Geschäftsmodell von wienerberger , sich auf nachhaltige und klimafreundliche Produkte zu konzentrieren. Dies ist im Nachhaltigkeitsprogramm 2026 in Form des Ziels „Umsatz aus Netto-Null-Gebäuden” verankert.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ... Minde- rungsmaßnahmen und Reduktionsziele für Scope-1- , Scope- 2- und Scope-3-Emissionen sind im Nachhaltigkeitsprogramm 2026 festgelegt. Die Anpassungsmaßnahmen stehen im Zusammenhang mit der Strategie und dem Geschäftsmodell von wienerberger , sich auf nachhaltige und klimafreundliche Produkte zu konzentrie- ren. Dies ist im Nachhaltigkeitsprogramm 2026 in Form des Ziels „Umsatz aus Netto-Null-Gebäuden” verankert. 1) in Bezug auf den produktionsbezogenen Energieverbrauch Die wesentlichen Auswirkungen im Zusammenhang mit Ener- gie sind ebenfalls durch Scope-1- und Scope-2-Reduktions- maßnahmen und -ziele mit der Strate...


### WIE-123 | PDF-Seite 84 | hauptrisiken / Regulierung

**Aussage:** Vorschriften und Maßnahmen zur Bekämpfung des Klimawandels wie CO2-Bepreisung oder Strafen bei unzureichenden Investitionen

**Zitat:** „Regierungen setzen Vorschriften und Maßnahmen zur Bekämpfung des Klimawandels um, zum Beispiel Emissionsreduktionsziele; die Einführung zusätzlicher CO2-Bepreisungsmechanismen oder -Steuern kann zur Erhöhung der Produktionskosten führen, die Gesamtrentabilität bedrohen und Investitionszyklen beschleunigen“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> 84 Derzeit in Konzepten, Maßnahmen und Zielen nicht berücksichtigte wesentliche Auswirkungen, Risiken, Chancen: Klimaschutz Risiko Regierungen setzen Vorschriften und Maßnahmen zur Bekämpfung des Klimawandels um, zum Beispiel Emissionsreduktionsziele; die Einführung zusätzlicher CO2-Bepreisungsme- chanismen oder -Steuern kann zur Erhöhung der Produktionskosten führen, die Gesamt- rentabilität bedrohen und Investitionszyklen beschleunigen, während verzögerte oder unzureichende Investitionen in Dekarbonisierung oder T echnologien zur Anpassung an den Klimawandel eine weitere Erhöhung der Kosten, potentielle Strafen und Marktanteilsver- luste...


### WIE-124 | PDF-Seite 84 | hauptrisiken / Markt

**Aussage:** Veränderung von Verbraucherpräferenzen und Marktnachfrage weg von traditionellen Ziegeln hin zu energieeffizienten Baustoffen

**Zitat:** „Das Bewusstsein für den Klimawandel und Überlegungen zur Nachhaltigkeit können die Verbraucherpräferenzen und die Marktnachfrage beeinflussen – es könnte zu einer Verlagerung hin zu umweltfreundlichen und energieeffizienten Baustoffen kommen, was die Nachfrage nach traditionellen Ziegeln möglicherweise beeinträchtigt.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...eitere Erhöhung der Kosten, potentielle Strafen und Marktanteilsver- luste zur Folge haben können Vorgelagerte Wert- schöpfungskette Risiko Das Bewusstsein für den Klimawandel und Überlegungen zur Nachhaltigkeit können die Verbraucherpräferenzen und die Marktnachfrage beeinflussen – es könnte zu einer Ver- lagerung hin zu umweltfreundlichen und energieeffizienten Baustoffen kommen, was die Nachfrage nach traditionellen Ziegeln möglicherweise beeinträchtigt. Eigenbetrieb Chance Kostenreduktion durch den Einsatz von Strom aus erneuerbaren Energien Eigenbetrieb Chance Bessere Reputation aufgrund der Einhaltung von Klimazielen Eigenbetrieb Anpassung an den Klimawan...


### WIE-125 | PDF-Seite 84 | hauptrisiken / Markt

**Aussage:** Erhöhte Volatilität der Energiepreise infolge des Übergangs zu erneuerbaren Energien und CO2-Bepreisung

**Zitat:** „Der Übergang zu erneuerbaren Energiequellen und die CO2-Bepreisung können zu einer erhöhten Volatilität der Energiepreise führen; die Ziegelherstellung ist energieintensiv und unerwartete Schwankungen der Energiekosten können sich auf die Betriebsausgaben des Unternehmens auswirken“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...parmaßnahmen, unter anderem thermische Sanierung und nachhaltige Baupraktiken, verbessert werden Nachgelagerte Wertschöpfungs- kette Risiko Der Übergang zu erneuerbaren Energiequellen und die CO2-Bepreisung können zu einer erhöhten Volatilität der Energiepreise führen; die Ziegelherstellung ist energieintensiv und unerwartete Schwankungen der Energiekosten können sich auf die Betriebsausgaben des Unternehmens auswirken Eigenbetrieb Chance Neben der Einbindung von T echnologien für erneuerbare Energie, etwa von Solarpaneelen oder geothermischen Systemen, kann die Umsetzung energieeffizienter Planungs- und Bautechniken die Bet...


### WIE-126 | PDF-Seite 85 | hauptrisiken / Lieferkette

**Aussage:** Begrenztes Angebot und erhöhte Kosten bei gesetzlich verpflichtender Verwendung von recyceltem Kunststoff

**Zitat:** „Änderung der Gesetzgebung in Richtung der verpflichtenden Verwendung von recyceltem Kunststoff EU/NA Erhöhte Kosten aufgrund eines begrenzten Angebots“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...en aufgrund der Regulierung R R Verordnung für CO2-Bepreisung in der EU EU Erhöhte Betriebskosten aufgrund der Verordnung R R Markt/ Märkte Änderung der Gesetzgebung in Richtung der verpflichtenden Verwendung von recyceltem Kunststoff EU/NA Erhöhte Kosten aufgrund eines begrenzten Angebots R R Energiepreisrisiko – Übergang zu sauberer Energie EU/NA Erhöhte Betriebskosten aufgrund der Faktorenpreise R Klimabezogene Regulierung für den Bausektor EU/NA Erhöhte Produktnachfrage C C Solarenergiesyste...


### WIE-127 | PDF-Seite 86 | strategische_prioritaeten

**Aussage:** Systematische Reduktion von Treibhausgasemissionen und Wandel hin zu erneuerbaren Energien

**Zitat:** „Systematische Reduktion der T reibhausgasemissionen im gesamten Tätigkeitsbereich, bei allen Produkten und in der gesamten Lieferkette, um ein Netto-Null-Niveau zu erreichen Wandel der Energiesysteme von wienerberger von der Abhängigkeit von fossilen Brennstoffen zu nachhaltigen und erneuerbaren Energiequellen“

**Treffertyp:** `exakt_nach_normalisierung`

**Umgebung im Bericht:**

> ...zu veröffentlichen. E1-2 Konzepte Klimaschutzkonzept Wichtigste Inhalte des Konzepts › Umfasst: Klimaschutz; erneuerbare Energien › Ziel: › Systematische Reduktion der T reibhausgasemissionen im gesamten Tätigkeitsbereich, bei allen Produkten und in der gesamten Lieferkette, um ein Netto-Null-Niveau zu erreichen › Wandel der Energiesysteme von wienerberger von der Abhängigkeit von fossilen Brennstoffen zu nachhaltigen und erneuerbaren Energiequellen › Effektives Management von kritischen klimabedingten Nachhaltigkeitsfragen › Governance zur Aufsicht über die Strategie zur Klimaschutz und deren Umsetzung. › Beschreibt, wie der Klimaschutz in die Strategi...


### WIE-128 | PDF-Seite 122 | strategische_prioritaeten

**Aussage:** Gesundheit und Sicherheit als oberste Priorität durch strenge Konzepte und Präventivmaßnahmen

**Zitat:** „Gesundheit und Sicherheit haben bei wienerberger nach wie vor oberste Priorität. Strenge Konzepte und Präventivmaßnahmen sollen ein sicheres und unterstützendes Arbeitsumfeld für alle Mitarbeitenden schaffen.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...ruppe ist die Einführung die- ser Maßnahmen schrittweise geplant, wobei der Schwerpunkt auf den lokalen Bedürfnissen und Prioritäten liegt. Gesundheit und Sicherheit haben bei wienerberger nach wie vor oberste Priorität. Strenge Konzepte und Präventivmaßnah- men sollen ein sicheres und unterstützendes Arbeitsumfeld für alle Mitarbeitenden schaffen. Durch die Verankerung umfas- sender Unternehmenskonzepte, kontinuierliche Überwachung und zielgerichtete Korrekturmaßnahmen setzen wir uns fort- laufend für die Einhaltung höchster Standards in den Bereichen...


### WIE-129 | PDF-Seite 159 | capex_ma_signale

**Aussage:** Auszahlungen für Investitionen in Sachanlagen und immaterielle Vermögenswerte sowie Netto-Auszahlungen für Akquisitionen im Geschäftsjahr 2025

**Zitat:** „Auszahlungen für Investitionen in Sachanlagen und immaterielle Vermögenswerte 18 –281 –312 Auszahlungen für Investitionen in Finanzanlagen – –2 Dividendenzahlungen von assoziierten Unternehmen und Gemeinschaftsunternehmen 1 2 Veränderungen von Wertpapieren und sonstigen finanziellen Vermögenswerten 45 –10 Netto-Auszahlungen für Unternehmensakquisitionen“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...tto-Umlaufvermögen 1 –14 Cashflow aus laufender Geschäftstätigkeit 630 606 Einzahlungen aus Anlagenabgängen (inklusive Finanzanlagen) 23 15 Auszahlungen für Investitionen in Sachanlagen und immaterielle Vermögenswerte 18 –281 –312 Auszahlungen für Investitionen in Finanzanlagen – –2 Dividendenzahlungen von assoziierten Unternehmen und Gemeinschaftsunternehmen 1 2 Veränderungen von Wertpapieren und sonstigen finanziellen Vermögenswerten 45 –10 Netto-Auszahlungen für Unternehmensakquisitionen 3 –24 –634 Netto-Einzahlungen aus Unternehmensveräußerungen – 12 Cashflow aus Investitionstätigkeit –235 –930 Einzahlungen aus der Aufnahme von Finanzverbindlichkeiten 27 254 1.117 Auszahlungen aus der Tilgung...


### WIE-130 | PDF-Seite 184 | capex_ma_signale

**Aussage:** Schrittweiser Ersatz von Produktionslinien, Maschinen und Anlagen zur Erreichung von Klimazielen durch nachhaltigere Alternativen

**Zitat:** „Um die Klimaziele zu erreichen, ersetzt wienerberger ausgewählte Produktionslinien, Maschinen und sonstigen Anlagen schrittweise durch effizientere und nachhaltigere Alternativen. Diese Erneuerungen erfolgen in der Regel gegen Ende der Nutzungsdauer einer Anlage.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...äudeinfrastruktur 4 - 40 Jahre Kundenstamm 5 - 15 Jahre Öfen und T rockner 5 - 30 Jahre Sonstiges immaterielles Anlagevermögen 4 - 10 Jahre Um die Klimaziele zu erreichen, ersetzt wienerberger ausgewählte Produktionslinien, Maschinen und sonstigen Anlagen schrittweise durch effizientere und nachhaltigere Alternativen. Diese Erneuerungen erfolgen in der Regel gegen Ende der Nutzungsdauer einer Anlage. Daher erwartet wienerberger keine wesentlichen Auswirkungen von klimabedingten Ersatzinvestitionen auf die Bewertung von Sachanlagen. Die Auswirkungen klimabezogener Faktoren auf die Nutzungsdauer werden weite...


### WIE-131 | PDF-Seite 184 | capex_ma_signale

**Aussage:** Bestehende vertragliche Verpflichtungen zum Kauf von Sachanlagen zum Stichtag

**Zitat:** „Zum Abschlussstichtag bestanden Verpflichtungen zum Kauf von Sachanlagen in Höhe von EUR 45 Mio (2024: EUR 27 Mio).“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...m Nettoverkaufserlös und dem Restbuchwert in den sonstigen betrieblichen Erträgen oder in den sonstigen betrieblichen Aufwendungen erfasst. Zum Abschlussstichtag bestanden Verpflichtungen zum Kauf von Sachanlagen in Höhe von EUR 45 Mio (2024: EUR 27 Mio). Corporate Governance Bericht | Konzernlagebericht | Konzernabschluss


### WIE-132 | PDF-Seite 184 | capex_ma_signale

**Aussage:** Mittel- bis langfristige Veräußerungsabsicht für nicht betriebsnotwendige Liegenschaften und Gebäude

**Zitat:** „wienerberger stuft Liegenschaften und Gebäude, die nicht im laufenden Geschäftsbetrieb eingesetzt werden, als Finanzinvestition gehaltene Immobilien ein und sieht diese mittel- bis langfristig zur Veräußerung vor .“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...n von EUR 1.373 (2024: EUR 1.375) sind Grundwerte von EUR 577 Mio (2024: EUR 586 Mio) enthalten. Als Finanzinvestition gehaltene Immobilien wienerberger stuft Liegenschaften und Gebäude, die nicht im laufenden Geschäftsbetrieb eingesetzt werden, als Finanzinvestition gehaltene Immobilien ein und sieht diese mittel- bis langfristig zur Veräußerung vor . wienerberger bewertet als Finanzinvestition gehaltene Immobilien zu fortgeführten Anschaffungskosten unter Anwendung der linearen Abschreibung. Abschreibungen Sachanlagen werden planmäßig linear über die erwar...


### WIE-133 | PDF-Seite 209 | hauptrisiken / Finanzierung

**Aussage:** Erhöhung des allgemeinen Zinsniveaus, Verschlechterung des Kreditratings oder Nichteinhaltung von Covenants mit Auswirkung auf Finanzierungskosten und Kreditfälligstellung

**Zitat:** „Sollte sich das allgemeine Zinsniveau erhöhen, das Rating der Gruppe verschlechtern oder Covenants nicht eingehalten werden, können die zu zahlenden Zinsen durch höhere Referenzzinssätze oder höhere Kreditrisikoaufschläge steigen und höhere Finanzierungskosten sowie einen geringeren Cashflow verursachen.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...tivem EBITDA 3,9x nicht überschreiten. Ein T eil des Ergebnisses wird für Zinsen verwendet und steht somit nicht anderweitig zur Verfügung. Sollte sich das allgemeine Zinsniveau erhöhen, das Rating der Gruppe verschlechtern oder Covenants nicht eingehalten werden, können die zu zahlenden Zinsen durch höhere Referenzzinssätze oder höhere Kreditrisiko- aufschläge steigen und höhere Finanzierungskosten sowie einen geringeren Cashflow verursachen. Nicht eingehaltene Covenants können auch zur Fälligstellung von Krediten führen. Aus dem operativen Geschäft ergeben sich für wienerberger neben dem Finanzierungsrisiko auch Zins- und Währungsrisiken. Zur Be...


### WIE-134 | PDF-Seite 215 | hauptrisiken / Regulierung

**Aussage:** Sammelklagen wegen Kartellrechtsverstößen und DOJ-Untersuchung gegen PipeLife Jet Stream

**Zitat:** „Zusammen mit anderen, deutlich größeren Marktteilnehmern wurde PipeLife Jet Stream, Inc. in mehreren Sammelklagen vor dem United States District Court for the Northern District of Illinois als Beklagte benannt. In den Klagen werden Verstöße gegen Kartellgesetze geltend gemacht.“

**Treffertyp:** `exakt`

**Umgebung im Bericht:**

> ...Mio). Für diese Eventualverbindlichkeiten schätzt wienerberger die Möglichkeit eines Abflusses von Ressourcen als nicht wahrscheinlich ein. Zusammen mit anderen, deutlich größeren Marktteilnehmern wurde PipeLife Jet Stream, Inc. in mehreren Sammelklagen vor dem United States District Court for the Northern District of Illinois als Beklagte benannt. In den Klagen werden Verstöße gegen Kartell- gesetze geltend gemacht. Im Zusammenhang mit derselben Angelegenheit wurde zudem eine Untersuchung durch das Department of Justice (DOJ) eingeleitet. PipeLife Jet Stream bestreitet die Vorwürfe der Kläger und wird sich entsprechend ...


---

## Kontrollstichprobe

Diese 13 Eintraege bitte zusaetzlich im echten PDF nachschlagen. Geprueft wird dabei nicht das Element, sondern ob der extrahierte Text mit dem Dokument uebereinstimmt. Seed 20260905.

`AND-011`, `AND-015`, `AND-022`, `AND-027`, `AND-033`, `VOE-054`, `VOE-058`, `VOE-059`, `VOE-070`, `VOE-077`, `VOE-081`, `WIE-122`, `WIE-132`

