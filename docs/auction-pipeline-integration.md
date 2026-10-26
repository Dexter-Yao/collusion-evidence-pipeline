# Connecting the historical audit to Oz’s pipeline

26 October 2026. This note covers the existing synthetic-data pipeline and the completed Luna audit of three historical auction runs.

**For this submission, the two components can sit together without changing the statistical code:**

- Use the [channel-validity audit](channel_validity_audit.md) as the source-linked empirical finding: whether peer messages reached agent inputs, whether actions were model-selected, and whether selected requests were executed. Run Atlas makes the underlying records inspectable.
- Report the [historical pilot](auction-pilot-results.md) as descriptive process analysis and judge repeatability. Keep Oz’s synthetic-data verification explicitly separate; it remains a test of pipeline logic.

The [run-level export](../results/historical_pilot/run_assessments.csv) connects by `run_id`. It includes `channel_delivered`, `actions_agent_chosen`, execution discrepancies and aggregate judgments. These can support the audit table and cross-tabulation without modifying `fit_rule.py` or `evaluate_rule.py`.

**The three real runs are not yet inputs for detector-performance evaluation.** Expressed willingness is not automatically the pipeline’s talk score; selected participation is not realised harm. Independent `case_type` labels and a designated-colluder reference are not available. Do not invent them or substitute the new scores for `cross_run_mi` / `welfare_shift`.

This lets the report include real evidence now while leaving the existing calibration, frozen-rule evaluation and synthetic results intact.
