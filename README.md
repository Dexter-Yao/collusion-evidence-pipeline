# Collusion evidence pipeline · Apart Track 2.3

26 October 2026. This is one exploratory study connecting **source validity → process evidence → frozen calibration → held-out comparison**. The real-source pipeline has run end to end. Its reference labels are AI-assisted source audits awaiting independent human review; results are preliminary, not validated detector performance.

The research question is whether a monitor infers coordination or execution that the available record does not establish. The contribution combines a channel/execution audit, three complete historical auction process audits, and a small real-source frozen-rule pilot.

## Results and evidence

- [Integrated real-source experiment, results and limits](results/real_calibration/report.md): 16 distinct parent-run focal cases, eight calibration/eight test, 144 new Luna calls. The audit rule detects 2/2 provisional positives and flags 1/6 provisional negatives; ordinary direct judgment detects 2/2 and flags 2/6. B-only matches the audit rule, so no benefit of the AND operator itself is established.
- [Channel and execution validity audit](docs/channel_validity_audit.md): original candidate-path limitations and a communicated withdrawal request that the market fails to execute.
- [Complete historical process audit](docs/auction-pilot-results.md): three full runs, 450 seller-rounds and 540 repeated judge calls. These are descriptive process observations, not 450 independent experiments.
- [One dataflow and interface to Oz’s pipeline](docs/auction-pipeline-integration.md).
- [Original market and process-judge protocol](docs/auction-process-evaluation.md); the additional focal-case study has its own immutable [protocol and split](results/real_calibration/frozen_protocol.json).

## What changed in the statistical code

The original synthetic defaults and all 20 synthetic rate-table rows are unchanged. Optional fit arguments select actual score names, a pre-scoring run split, the positive target and a direct-judge baseline. An opt-in empirical cutoff handles ordinal ties. Missing assignment metadata remains unknown and is never the target. The fitted real rule was committed as `db7c217` before test evaluation.

```bash
uv run --with pandas --with numpy python fit_rule.py   --input results/real_calibration/scores_complete.csv   --out /tmp/replayed_rule.json --talk-col intent_score --behaviour-col action_score   --ordinary-col ordinary_score --positive-case-type coordinated_action   --threshold-policy empirical --split-file results/real_calibration/frozen_protocol.json
uv run --with pandas --with numpy python evaluate_rule.py   --input results/real_calibration/scores_complete.csv   --rule /tmp/replayed_rule.json --outdir /tmp/replayed_test
```

The original frozen artifact is retained. No model calls are needed to replay these scores. The `historical_audit` module retains source parsing, repeated Codex CLI scoring, summaries and the earlier descriptive bridge. A fresh inference run requires explicit authorization and subscription access; it is unnecessary for reviewing the saved results.

## Verification and interpretation

31 inference-free integrity tests pass. Replacing held-out scores does not change fitted thresholds, swapping input bytes is rejected, and the original synthetic defaults reproduce. All 48 source files for the focal study match their pinned Git objects. Six new judge calls timed out and one returned the wrong seller ID; all sixteen cases still have at least two known scores per method. Failed/unknown answers are not zero.

The positive target is supported coordinated **selected action**, not realised causal harm. The unilateral-proposal controls apply only at their focal opening round, not the whole subsequent run. The sample is small, purposive and condition/time-confounded; the audit uses more judge calls than the direct baseline. No causal oversight effect, validated early warning or general detection superiority is claimed. See the report for intervals, references and LLM-assistance disclosure.

## Synthetic verification

`results/fake_debug/` contains fabricated-score pipeline checks. `make_fake_scores.py`, default `fit_rule.py`, `frozen_rule_blind.py` and `evaluate_rule.py` reproduce those checks. Their numbers must not be represented as real detector observations. Largest-gap/percentile sensitivity results remain synthetic only.

## Team and paper

**Oz** (`roz-logic`): original statistical pipeline and integrity checks. **Shuhao Yao** (`Dexter-Yao`): source/process audit and real-data integration with AI assistance. **Lucette** (`cookkatelyn01-ui`): paper structure, editing and formatting.

[Complete concise paper review copy](paper/main.tex) · [Verified references](paper/refs.bib) · [Paper and Run Atlas review bundle](artifacts/submission-review.zip). The paper is a review copy for Lucette, not a submission to Overleaf or the sprint. See [attribution](THIRD_PARTY_NOTICES.md).
