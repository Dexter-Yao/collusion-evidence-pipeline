## Collusion evidence pipeline (Apart AI Collusion Sprint, track 2.3)

**Status: unfinished work.** This repo contains an evaluation pipeline verified on synthetic data, plus an audit of what starter environments can and cannot establish about agent coordination. It now also contains an **exploratory process audit of three real historical auction runs**, with repeated Luna judgments pending human calibration. No real detector-accuracy result is claimed.

**Question:** when both the language and the actions of AI agents look collusive, does a detector infer an agreement that the evidence doesn’t establish?

**What’s here**

- `fit_rule.py`: splits runs by case type, calibrates thresholds on known-negative training runs at a 10% per-axis false-alarm target, and writes `frozen_rule.json`.
- `evaluate_rule.py`: reads the frozen rule, checks the input file hash, scores held-out runs, and reports rates with Wilson 95% intervals against two single-axis baselines.
- `frozen_rule_blind.py`: a sensitivity analysis using label-free thresholds (gap and percentile).
- `tests/`: a leak test showing thresholds don’t depend on test rows.
- `docs/channel_validity_audit.md`: the audit.

**Reproduce (synthetic data only)**

```bash
pip install -r requirements.txt
python make_fake_scores.py
python fit_rule.py
python frozen_rule_blind.py
python evaluate_rule.py --outdir results/fake_debug
pytest tests/ -v
```

**All numbers in `results/fake_debug/` come from synthetic data built with obvious separation. They verify the pipeline. They are not evidence about any real detector.**

## Author Contributions

To be confirmed with each person before submission. 

## Historical auction process audit

The additive `historical_audit/` module prepares three complete pinned auction runs: 90 rounds and 450 seller decisions, including communication-disabled, communication-enabled, and overseen conditions. The completed pilot uses 180 frozen request packets, each repeated in three fresh `gpt-6-luna` Codex CLI sessions: **540 calls and 2,700 planned axis ratings**. All 2,700 ratings satisfy the current basic checks for seller coverage, legal scores and non-empty rationale. Exact quotation is not an inclusion gate. Stable judgment is not ground-truth correctness. No real detector-performance claim is made.

- [Market and evaluation diagrams, canonical judge prompts, scope](docs/auction-process-evaluation.md)
- [Source-level channel and execution audit](docs/channel_validity_audit.md)
- [Real-log pilot results and stability](docs/auction-pilot-results.md)
- [Small aggregate exports and provenance](results/historical_pilot/)
- [Completed descriptive bridge to Oz’s unchanged classifier](results/luna_bridge/summary.json)
- `python -m historical_audit.fetch_sources --help`: acquire and verify pinned public records.
- `python -m historical_audit.prepare --help`: prepare factual tables and the frozen request batch offline.
- `python -m historical_audit.codex_batch --help`: repeat the frozen packets using authenticated Codex CLI; inference requires explicit `--execute`.
- `python -m historical_audit.judge --prepared /path/to/prepared`: optional alternative-provider preview, not used for the Luna pilot.
- `python -m historical_audit.summarise --help`: join basic-checked outputs to round facts, without fitting a rule or inventing reference labels.
- `python -m unittest discover -s historical_audit/tests -v`: inference-free integrity tests.

The existing fit/evaluate scripts and synthetic results are unchanged. Raw source logs and prepared requests belong in an external local cache, not Git. Intention/participation scores are not automatically equivalent to the original talk/behaviour placeholders, and the complete-run pilot is not a held-out accuracy study.

## Reproduce the saved-rating bridge (no inference)

With the dependencies in `requirements.txt` installed:

```bash
uv run python -m historical_audit.oz_bridge --analysis /path/to/saved/analysis --output /path/to/bridge-results
```

This reuses the existing classification functions at the approved ordinal boundaries; it does not fit thresholds or fill reference labels. All 450 units are retained, including 48 unresolved after three-repeat binary consensus. It does not establish improved detection accuracy. Judge B already reads communication context, so B-only is not an actions-only baseline.
