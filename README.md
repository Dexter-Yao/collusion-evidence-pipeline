## Collusion evidence pipeline (Apart AI Collusion Sprint, question 2.3)

**Status: unfinished work.** This repo contains an evaluation pipeline verified on synthetic data, plus an audit of what starter environments can and cannot establish about agent coordination. It contains **no results on real agent logs.**

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
python fit_rule.py --input fake_scores.csv --out results/fake_debug/frozen_rule.json
python evaluate_rule.py --input fake_scores.csv --rule results/fake_debug/frozen_rule.json --outdir results/fake_debug
pytest tests/ -v
```

**All numbers in `results/fake_debug/` come from synthetic data built with obvious separation. They verify the pipeline. They are not evidence about any real detector.**

**Reused vs new:** see `docs/NOTICE_REUSED_VS_NEW.md`. **Limitations and dual-use:** see `docs/LIMITATIONS_AND_DUAL_USE.md`. **Report:** [link when submitted]. **Team and roles:** `docs/CONTRIBUTIONS.md`.
