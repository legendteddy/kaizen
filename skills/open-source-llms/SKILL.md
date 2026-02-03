---
name: open-source-llms
description: Guide to local Llama/Mistral/Qwen models, hardware requirements, and serving engines.
---

# Open-Source LLMs (2026 Landscape)

> "Own your intelligence."

## 1. Top Models (The Starting Lineup)

| Model Family | Best For | Typical Params |
|:---|:---|:---|
| **Llama 4** (Meta) | General Tasks, Ecosystem Support | 8B, 70B, 405B |
| **Mistral / Mixtral** | Efficiency, Long Context | 7B, 8x7B (MoE), 8x22B |
| **Qwen 2.5** | Coding, Math, Multilingual | 7B, 14B, 32B, 72B |
| **DeepSeek R1** | Reasoning (Chain of Thought) | 671B (MoE) |
| **Phi-4** | Small Devices (Mobile/Laptop) | 3.8B, 14B |

## 2. Hardware Requirements (VRAM Guide)

Can you run it? Check your GPU VRAM.
*Estimates based on 4-bit quantization (GGUF/EXL2).*

| VRAM | Max Model Size | Recommended Models |
|:---|:---|:---|
| **6 GB** | ~8B Params | Llama-3-8B-Q4, Phi-4, Qwen-7B |
| **8 GB** | ~11B Params | Mistral-7B-Instruct, Gemma-2-9B |
| **12 GB** | ~20B Params | Command R, Yi-34B (heavy quant) |
| **16 GB** | ~25B Params | Mixtral 8x7B (Q3), Qwen-32B |
| **24 GB** (3090/4090) | ~40B Params | Llama-3-70B (IQ2_XS), Yi-34B, Command R+ (heavy) |
| **48 GB** (2x3090) | ~80B Params | Llama-3-70B (Q4), Qwen-72B |
| **Mac M1/M2/M3 (Unified)** | Shared System RAM | Run anything that fits in RAM minus 4GB OS overhead. |

## 3. Serving Engines

### 1. Ollama (The Easy Way)
Best for: Developers, CLI usage.
```bash
ollama run llama3
ollama run deepseek-coder:33b
```
- **Pros:** Zero config, huge library.
- **Cons:** Slower than vLLM.

### 2. SGLang / vLLM (The Fast Way)
Best for: Production APIs, Batching.
- **vLLM:** Standard for high throughput.
- **SGLang:** Specialized for structured output (JSON).

### 3. LM Studio / KoboldCPP (The GUI Way)
Best for: Visual users, tweaking GGUF layers on the fly.

## Protocol: Choosing a Local Model
1. **Task:** Coding? -> Qwen/DeepSeek. General? -> Llama/Mistral.
2. **RAM Check:** Do you have the VRAM? (Use `nvidia-smi` or Task Manager).
3. **Quantization:**
   - **Q4_K_M:** The sweet spot (minimal loss, small size).
   - **Q8_0:** Overkill usually.
   - **Q2_K:** Brain damage expected. Avoid unless desperate.

## Self-Improvement
- **Tokens/sec too low?** -> Check if layers are offloaded to GPU (`-ngl` in llama.cpp).
- **Out of Memory (OOM)?** -> Use a higher instruction context size `-c` or lower quantization.
