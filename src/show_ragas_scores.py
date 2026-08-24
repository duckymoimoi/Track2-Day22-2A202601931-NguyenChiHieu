"""In kết quả RAGAS đã lưu mà không phải chạy lại quá trình đánh giá."""

import json
from pathlib import Path


def main() -> None:
    report_path = Path(__file__).parent.parent / "data" / "ragas_report.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    v1 = report["prompt_v1_scores"]
    v2 = report["prompt_v2_scores"]

    print("=" * 67)
    print("  Đánh giá RAGAS - So sánh Prompt V1 và Prompt V2")
    print("=" * 67)
    print(f"  {'Chỉ số':30s}  {'V1':>9}  {'V2':>9}  Kết quả")
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
            winner = "Hòa"
        else:
            winner = "V1" if score_v1 > score_v2 else "V2"
        print(f"  {metric:30s}  {score_v1:>9.4f}  {score_v2:>9.4f}  {winner}")
    print("=" * 67)
    print(f"  Mục tiêu faithfulness >= 0.8: {'ĐẠT' if report['target_met'] else 'CHƯA ĐẠT'}")
    print(f"  Báo cáo: {report_path}")


if __name__ == "__main__":
    main()
