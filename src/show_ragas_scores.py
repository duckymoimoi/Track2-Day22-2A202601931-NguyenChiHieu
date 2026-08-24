"""Print the saved RAGAS comparison without rerunning the expensive evaluation."""

import json
from pathlib import Path


def main() -> None:
    report_path = Path(__file__).parent.parent / "data" / "ragas_report.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    v1 = report["prompt_v1_scores"]
    v2 = report["prompt_v2_scores"]

    print("=" * 67)
    print("  RAGAS Evaluation - Prompt V1 vs Prompt V2")
    print("=" * 67)
    print(f"  {'Metric':30s}  {'V1':>9}  {'V2':>9}  Winner")
    print("-" * 67)
    for metric in (
        "faithfulness",
        "answer_relevancy",
        "context_recall",
        "context_precision",
    ):
        score_v1 = v1[metric]
        score_v2 = v2[metric]
        if abs(score_v1 - score_v2) < 0.0001:
            winner = "Tie"
        else:
            winner = "V1" if score_v1 > score_v2 else "V2"
        print(f"  {metric:30s}  {score_v1:>9.4f}  {score_v2:>9.4f}  {winner}")
    print("=" * 67)
    print(f"  Faithfulness target >= 0.8: {'PASS' if report['target_met'] else 'FAIL'}")
    print(f"  Report: {report_path}")


if __name__ == "__main__":
    main()
