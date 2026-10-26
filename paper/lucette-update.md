# Necessary paper updates for Lucette

Thanks for pulling the draft together. The real auction data now run through Oz’s calibration, committed freeze and held-out evaluation. Please treat the accompanying `main.tex` as a reference copy and preserve your newer Overleaf/template edits.

## Findings to incorporate

The main contribution is one evidence chain: source/channel validity, full-run process audit, then frozen-rule evaluation. A communicated withdrawal request can be selected by an agent but fail in environment execution. Our process judges inspect seller-round evidence rather than only whole-run aggregates.

The additional real-source pilot has 16 distinct parent runs, split eight/eight before scoring. On eight held-out focal cases:

| Method | Provisional positives detected | Provisional negatives flagged |
| --- | ---: | ---: |
| Audit + Oz rule | 2/2 | 1/6 |
| Ordinary judge, same-null calibration | 2/2 | 2/6 |
| Participation B alone | 2/2 | 1/6 |

References were drafted with AI assistance before scoring and await independent human validation. The sample is purposive and small. This is preliminary workflow evidence, not a validated accuracy benchmark or proof that the AND operator improves detection. The Tara example separates a unilateral proposal from supported joint action; the remaining Omar flag reflects inconsistent treatment of the outgoing proposal as an action.

## Necessary corrections

- Real historical data are Agrawal’s `llm-agent-collusion`; Colosseum is related work and ColludeBench supplies the initial audited paths.
- Replace the old three-directory case table with the source-validity audit. Remove uncomputed coalition-advantage/dependence claims.
- Use the actual frozen-rule methods/results. Original synthetic checks stay explicitly synthetic.
- Keep the time/data constraints: we have not isolated the gain from process information over whole-run aggregates, established causal harm, or validated early warning.
- The complete draft includes related work, limitations/ethics, contributions and LLM usage. Team authors: **Oz, Shuhao Yao, Lucette**.

The editable TeX and bibliography are included; raw test counts and provenance are in `real-evaluation/`. No additional experiment is proposed for the remaining sprint time.
