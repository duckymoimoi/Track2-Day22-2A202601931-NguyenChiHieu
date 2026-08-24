# Tổng hợp bằng chứng

Sinh viên: Nguyễn Chí Hiếu (`2A202601931`)

## Cấu hình chạy

- Nhà cung cấp LLM: Groq qua API tương thích OpenAI
- Mô hình LLM: `openai/gpt-oss-120b`
- Chiến lược API key: xoay vòng 7 key Groq và tự chuyển key khi gặp giới hạn
- Embeddings: Ollama local với `nomic-embed-text` (768 chiều)
- LangSmith project: `pr-drab-increase-11`
- Tên prompt trên Prompt Hub:
  - `nguyen-chi-hieu-2a202601931-rag-v1`
  - `nguyen-chi-hieu-2a202601931-rag-v2`

## Xác minh traces

Kết quả kiểm tra qua LangSmith API sau khi chạy đầy đủ:

- `rag-query`: 51 root runs
- `ab-rag-query`: 101 root runs
- Tổng số root runs trong project: 359

Hai nhiệm vụ bắt buộc đã tạo tổng cộng 152 root traces, vượt yêu cầu tối
thiểu 100 traces.

## So sánh kết quả RAGAS

| Chỉ số | Prompt V1 | Prompt V2 | Kết quả cao hơn |
|---|---:|---:|---|
| Faithfulness | 0.9375 | 0.8209 | V1 |
| Answer relevancy | 0.8716 | 0.8734 | V2 |
| Context recall | 0.9800 | 0.9800 | Hòa |
| Context precision | 0.9083 | 0.9117 | V2 |

V1 có faithfulness cao hơn rõ rệt vì chỉ dẫn trả lời ngắn gọn giúp hạn chế
việc diễn giải thêm ngoài context được truy xuất. V2 nhỉnh hơn một chút ở
answer relevancy và context precision vì phong cách chuyên gia có cấu trúc
giúp tổ chức các dữ kiện rõ ràng hơn. Cả hai phiên bản đều vượt ngưỡng
faithfulness 0.8; V1 đồng thời vượt ngưỡng điểm thưởng 0.9.

## Các tệp bằng chứng bắt buộc

- `01_langsmith_traces.png`: chụp thủ công trên LangSmith sau khi lọc root
  runs theo tên `rag-query` và `ab-rag-query`.
- `02_prompt_hub.png`: chụp thủ công trên Prompt Hub, bảo đảm cả hai tên
  prompt cùng xuất hiện trong ảnh.
- `02_ab_routing_log.txt`: đã sinh từ lần chạy A/B đầy đủ 50 câu hỏi.
- `03_ragas_scores.png`: chụp thủ công cửa sổ terminal đang hiển thị bảng
  điểm RAGAS đã lưu.
- `03_ragas_report.json`: đã được Task 3 tự động tạo.
- `04_pii_demo_log.txt`: đã sinh từ sáu trường hợp kiểm thử PII.
- `04_json_demo_log.txt`: đã sinh từ năm trường hợp kiểm thử JSON.

Ba tệp PNG phải là ảnh chụp giao diện hoặc terminal thật, không được tạo giả
lập bằng chương trình.
