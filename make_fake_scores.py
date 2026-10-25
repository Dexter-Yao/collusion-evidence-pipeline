# Fake data for debugging the collusion pipeline logic only.
# Never to be quoted as a real result anywhere in the report.
# Python version: 3.14.4
# Required packages: pandas, numpy

import numpy as np
import pandas as pd

rng = np.random.default_rng(1)

# (talk mean, behaviour mean) per case type, deliberately separated
# so a correct pipeline should recover the expected pattern cleanly
spec = {
    "harmful":            (2.0, 2.0),  # talk AND behaviour, should flag
    "common_incentives":  (0.0, 1.0),  # behaviour only, should not flag
    "talk_only":          (2.0, 0.0),  # talk only, should not flag
    "honest":             (0.0, 0.0),  # neither, should not flag
}

rows = []
for case_type, (mt, mb) in spec.items():
    for i in range(10):
        rows.append({
            "run_id": f"{case_type}_{i}",
            "case_type": case_type,
            "cross_run_mi": rng.normal(mt, 1.0),
            "welfare_shift": rng.normal(mb, 1.0),
            "manifest_colluders": "['a']" if case_type in ("harmful", "talk_only") else "[]",
        })

pd.DataFrame(rows).to_csv("fake_scores.csv", index=False)
print("Wrote fake_scores.csv, 40 rows, 10 per case type")