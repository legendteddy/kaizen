---
name: open-source-llms
description: Skill for open-source-llms tasks and workflows.
---

# Skill: Open-Source LLMs (v1.0)

> Open-weight models for self-hosting (Llama, Mistral, Qwen, gpt-oss)

## Purpose
Understand and deploy open-source LLMs for local or self-hosted inference.

## Activation Trigger
- Self-hosting requirements
- Privacy-sensitive deployments
- Custom fine-tuning needs

---

## 2026 Open-Source Landscape

### Tier 1: Frontier Open Models

| Model | Params | Context | Specialty |
|:---|:---|:---|:---|
| Llama 4 Scout | 109B (17B active) | 10M | General, multimodal |
| Llama 4 Maverick | 400B (17B active) | 20K | Agentic tasks |
| Mistral Large 3 | 675B (41B active) | 256K | Multimodal, reasoning |
| Qwen 3 | 0.6B-235B | 256K-1M | Hybrid thinking |
| Kimi K2.5 | 1T | - | Open-source frontier |
| gpt-oss | Various | - | OpenAI open-weight |

### Tier 2: Efficient Models

| Model | Params | Context | Use Case |
|:---|:---|:---|:---|
| Devstral 2 | 123B | - | Coding (72.2% SWE-bench) |
| Devstral Small | 24B | - | Fast coding |
| Ministral 3 | 3B/8B/14B | 256K | Single-GPU |
| Mistral Small 3.1 | 24B | 128K | Multimodal lightweight |
| Mistral 7B | 7B | 32K | Fast deployment |

---

## Deployment Options

### 1. Ollama (Local)
```bash
# Run locally
ollama run llama4:scout
ollama run mistral:large
```
Best for: Personal use, development

### 2. vLLM (Production)
```bash
# High-performance serving
python -m vllm.entrypoints.openai.api_server \
  --model mistralai/Mistral-Large-3
```
Best for: Production deployments

### 3. Self-Hosted Cloud
- AWS, GCP, Azure with private VPCs
- Enterprise compliance
- Data sovereignty

---

## Open-Source Advantages

| Factor | Closed | Open |
|:---|:---|:---|
| Data Privacy | Data leaves premises | Stays local |
| Customization | Limited | Full control |
| Cost | Per-token pricing | Compute only |
| Vendor Lock-in | High | None |
| Fine-tuning | Often unavailable | Full access |

---

## For Sovereign Framework

Open models enable:
1. **Local processing**: Data never leaves machine
2. **Custom skills**: Fine-tune for specific domains
3. **Cost control**: No API fees
4. **Swarm operations**: Parallel local workers

