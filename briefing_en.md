# Where is Austrian industry looking for growth in 2026, and which risks does it name?

An LLM-assisted analysis of seven annual reports of ATX-listed industrial companies.
Lorenz Frauscher, September 2026.

---

## Universe and method

The analysis covers every ATX constituent in the industries **Basic Industries** and
**Industrial Goods & Services**, excluding the sectors Oil & Gas, whose growth follows commodity
prices, and Transportation, a service without own manufacturing. The basis is the Vienna Stock
Exchange sector classification in its current version with 10 industries and 41 sectors. The rule
was fixed in writing before the first extraction, and the sequence is verifiable through the
repository history.

**Seven companies, 2,217 pages.** Export-driven manufacturers: voestalpine, Lenzing, Andritz,
PALFINGER. Construction and building materials: Strabag, Porr, Wienerberger.

A Python pipeline extracts four field types per company and returns **369 statements**, each with
a verbatim quote. **The central design decision: the language model does not output page
numbers.** It returns quotes only, and the pipeline then locates each quote in the report text
itself to derive the page. A page reference therefore cannot be hallucinated, and a quote that
does not exist is caught for every single statement rather than in a sample.

In addition, 134 statements from three randomly drawn companies were checked by hand against the
source. The draw used a documented random seed and took place before any result data existed.

---

## Finding 1: Automated citation checking has a measurable limit

| | |
|---|---|
| quotes verified automatically | 369 |
| found verbatim in the report | **364 (99 %)** |
| **fabricated quotes** | **0** |
| statements checked by hand | 134, of which 111 correct (83 %) |
| **errors only the manual check found** | **23** |

The model does not fabricate quotes. In **15.7 per cent** of checked cases it cites the **wrong
real sentence**: the statement is substantively correct and appears in the report, but not in the
sentence given as evidence. Example Andritz, page 143: the quote reports the classification as
held for sale at end-2024, the statement reports the 2025 disposal. That information sits in the
following sentence.

**Automated citation verification proves that a sentence exists in the document. It does not
prove that the sentence supports the statement derived from it.**

| Field type | checked | correct | evidence does not support |
|---|---|---|---|
| Strategic priorities | 28 | 89 % | 2 |
| Capex and M&A | 42 | 83 % | 7 |
| Principal risks | 56 | 80 % | 11 |
| Growth markets | 8 | 75 % | 1 |

A side finding on caution with one's own measurements: the first run reported a 4.1 per cent
hallucination rate. The manual check showed that all 15 cases were measurement errors of the
pipeline's own quote search, caused by spaces the PDF extraction inserts inside words. After
correction: zero. **A measured error rate first measures your own pipeline.**

---

## Finding 2: Two separate growth geographies

The manufacturers name growth markets outside Europe. PALFINGER names India three times, plus
North America and the Middle East. voestalpine names China and India, Andritz names North
America, Latin America and the Middle East.

The construction companies name the home market and broad categories. Porr names Austria, DACH
and Europe, Strabag names DACH and Europe. Neither Porr nor Strabag nor Wienerberger names India
or China a single time.

**Limitation.** Across all seven companies there are only 27 quote-verified regional mentions,
and Lenzing names none. The extraction schema requires mapping to a fixed region list, so
segment-based growth statements fall through. The finding describes where growth is **named
geographically**, not where it is pursued.

<!--chart:1-->

---

## Finding 3: Only the manufacturers name technology risks

| Category | Manufacturers (n=4) | Construction (n=3) | total |
|---|---|---|---|
| Financing | 20 | 8 | 28 |
| Market | 17 | 10 | 27 |
| Regulation | 11 | 5 | 16 |
| Supply chain | 7 | 5 | 12 |
| **Technology** | **9** | **0** | **9** |

Technology is the only row with a qualitative jump: nine mentions among the manufacturers, **not
one** among construction and building materials. What they name there is product portfolio
competitiveness, intellectual property constraints and cyber risk. With four against three
companies this is not statistically robust, but the contrast is unambiguous because one group
does not touch the category at all.

<!--chart:2-->

---

## Limitations

**Sample size.** Seven companies, split four to three. The group tables describe, they do not
prove.

**One third comes from mandatory reporting.** 114 of 369 elements originate in the ESRS and
taxonomy sections. They are labelled, not removed. For Wienerberger the share is 53 per cent, for
Andritz zero, because that company publishes its sustainability section separately. The manual
check shows 78 against 85 per cent accuracy for ESRS sections.

**Inconsistent reporting year.** voestalpine closes on 31 March 2026, the other six on
31 December 2025.

**Version dependency.** PDF text extraction returns slightly different results depending on the
library version. The versions used are pinned in `requirements.txt`.

**Disclosure.** PALFINGER was the author's employer from February to June 2025. PALFINGER was not
drawn into the verification sample.

---

## What follows

An architecture that forces the model to quote and computes the evidence location itself makes
fabrication machine-detectable, and drove it to zero here. It does not replace human review, it
shifts that review's task from "does this sentence exist" to "does this sentence support this
statement". That is the question which decides 15.7 per cent of cases.

Anyone running such a pipeline in production without manual review gets results that survive
every automated check and are nonetheless wrongly evidenced in roughly one case out of six.

*Code, raw data, verification protocol and decision log: github.com/lorenzrauscher1-create/atx-industrials.
The annual reports themselves are not part of the repository.*
