# Evidence summary

Student: Nguyen Chi Hieu (`2A202601931`)

## Runtime configuration

- LLM provider: Groq OpenAI-compatible API
- LLM model: `openai/gpt-oss-120b`
- API key strategy: round-robin rotation across 7 Groq keys with failover
- Embeddings: local Ollama `nomic-embed-text` (768 dimensions)
- LangSmith project: `pr-drab-increase-11`
- Prompt Hub names:
  - `nguyen-chi-hieu-2a202601931-rag-v1`
  - `nguyen-chi-hieu-2a202601931-rag-v2`

## Trace verification

The LangSmith API verification after the full run returned:

- `rag-query`: 51 root runs
- `ab-rag-query`: 101 root runs
- Total root runs in the project: 359

The two required tasks therefore contribute 152 root traces, exceeding the
minimum requirement of 100 combined traces.

## RAGAS comparison

| Metric | Prompt V1 | Prompt V2 | Higher result |
|---|---:|---:|---|
| Faithfulness | 0.9375 | 0.8209 | V1 |
| Answer relevancy | 0.8716 | 0.8734 | V2 |
| Context recall | 0.9800 | 0.9800 | Tie |
| Context precision | 0.9083 | 0.9117 | V2 |

V1 is substantially more faithful because its concise instruction limits
unnecessary elaboration beyond the retrieved context. V2 is slightly better
on answer relevancy and context precision because its structured expert style
organizes the retrieved facts more explicitly. Both variants exceed the
required faithfulness threshold of 0.8; V1 also exceeds the 0.9 bonus target.

## Required evidence files

- `01_langsmith_traces.png`: capture manually from LangSmith after filtering
  root runs to `rag-query` and `ab-rag-query`.
- `02_prompt_hub.png`: capture manually from Prompt Hub with both prompt names
  visible.
- `02_ab_routing_log.txt`: generated from the full 50-query A/B run.
- `03_ragas_scores.png`: capture manually by displaying the saved JSON scores
  in a terminal.
- `03_ragas_report.json`: generated automatically by Task 3.
- `04_pii_demo_log.txt`: generated from all six PII cases.
- `04_json_demo_log.txt`: generated from all five JSON cases.

The three PNG files must be screenshots of the real UI/terminal and are not
generated synthetically.
