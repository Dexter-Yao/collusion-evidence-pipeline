"""ABOUTME: Join validated historical-judge outputs to factual round records.

Reports process categories and observations, never detector accuracy without an
independent reference. It does not fit Oz's rule, invent case_type or call models.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import json
from pathlib import Path
from typing import Any

from .judge import validate
from .prepare import read_json, sha256, write_csv


def quadrant(intent: int | str, action: int | str) -> str:
    """Preserve missing judgments separately from the four fully scored combinations."""
    if intent == "unknown" or action == "unknown" or intent == "" or action == "":
        return "unresolved"
    return {(True, True): "intent_and_action", (True, False): "intent_only",
            (False, True): "action_without_expressed_intent",
            (False, False): "neither_observed"}[(int(intent) > 0, int(action) == 1)]


def summarise(prepared: Path, judged: Path, output: Path) -> dict[str, Any]:
    """Produce auditable seller/round and run summaries under the same frozen inputs."""
    preparation = read_json(prepared / "preparation.json")
    profile = read_json(judged / "execution_profile.json")
    if preparation["requests_sha256"] != profile["requests_sha256"] or sha256(
        prepared / "judge_requests.jsonl"
    ) != profile["requests_sha256"]:
        raise ValueError("Prepared data do not match judge results")
    for name, expected in preparation["files_sha256"].items():
        if sha256(prepared / name) != expected:
            raise ValueError(f"Prepared facts changed: {name}")
    profile_hash = hashlib.sha256(json.dumps(profile, sort_keys=True).encode()).hexdigest()
    jobs = {job["request_id"]: job for job in (
        json.loads(line) for line in (prepared / "judge_requests.jsonl").read_text().splitlines())}
    scores: dict[tuple[str, int, str, str], dict[str, Any]] = {}
    valid_requests = set()
    for line in (judged / "judge_results.jsonl").read_text().splitlines():
        item = json.loads(line)
        if item["profile_sha256"] != profile_hash:
            raise ValueError("Mixed model/input profiles in result file")
        if item["status"] != "valid":
            continue
        job = jobs[item["request_id"]]
        if item["request_sha256"] != job["request_sha256"]:
            raise ValueError("Result belongs to another prepared request")
        response = item["attempts"][-1]["response"]
        records = validate(response["message"]["content"], job)
        valid_requests.add(job["request_id"])
        for record in records:
            scores[(job["run_id"], job["round"], record["agent_id"], job["axis"])] = record
    with (prepared / "seller_round_facts.csv").open(encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    counts: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        key = (row["run_id"], int(row["round"]), row["agent_id"])
        a = scores.get((*key, "intent"), {})
        b = scores.get((*key, "action"), {})
        row["intent_score"] = a.get("score", "")
        row["action_participation"] = b.get("score", "")
        row["intent_rationale"] = a.get("rationale", "")
        row["action_rationale"] = b.get("rationale", "")
        row["intent_evidence"] = json.dumps(a.get("evidence", []), ensure_ascii=False)
        row["action_evidence"] = json.dumps(b.get("evidence", []), ensure_ascii=False)
        row["process_category"] = quadrant(row["intent_score"], row["action_participation"])
        counts[row["run_id"]][row["process_category"]] += 1
    with (prepared / "run_facts.csv").open(encoding="utf-8-sig") as handle:
        run_rows = list(csv.DictReader(handle))
    for row in run_rows:
        for category in ("intent_and_action", "intent_only", "action_without_expressed_intent",
                         "neither_observed", "unresolved"):
            row[category + "_seller_rounds"] = counts[row["run_id"]][category]
        row["performance_reference_available"] = False
    output.mkdir(parents=True, exist_ok=True)
    write_csv(output / "seller_round_assessments.csv", rows)
    write_csv(output / "run_assessments.csv", run_rows)
    summary = {"valid_judge_requests": len(valid_requests), "planned_requests": len(jobs),
               "seller_rounds": len(rows), "independent_case_labels_assigned": 0,
               "interpretation": "descriptive process audit, not accuracy or a causal oversight estimate"}
    (output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    return summary


def main() -> None:
    """Summarise existing results only; no model call can be made from this entry."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prepared", type=Path, required=True)
    parser.add_argument("--judged", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(summarise(args.prepared, args.judged, args.output), indent=2))


if __name__ == "__main__":
    main()
