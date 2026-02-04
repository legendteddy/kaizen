---
name: voice-ai
description: Protocols for TTS, STT, Voice Cloning, and audio pipeline optimization.
---

# Voice AI

## Activation Trigger
- Implementing Text-to-Speech (TTS) or STT.
- Optimizing audio pipelines for latency.
- Cloning voices.

## 1. Speech-to-Text (STT) Strategy

### Preprocessing (Critical)
Garbage in, garbage out. Before sending to Whisper:
1.  **Denoise:** Remove background hum (FFmpeg lowpass/highpass).
2.  **Normalize:** Standardize volume to -14 LUFS.
3.  **Split:** Chunk long audio into 5-minute segments (Whisper has limits).

### Model Selection
| Model | Use Case | Hardware |
|:---|:---|:---|
| **Whisper API** | General, Multilingual | Cloud |
| **Faster-Whisper** | Production Backend | GPU (CUDA) |
| **Whisper.cpp** | Local/Mobile | CPU (Apple Silicon) |

## 2. Text-to-Speech (TTS) Strategy

### Optimization (Latency vs Quality)
- **Real-time Chat:** Use `OpenAI TTS-1` or `Deepgram`. Must use **Streaming Mode** (chunks).
- **Audiobooks/Content:** Use `ElevenLabs` or `OpenAI TTS-1-HD`. Render fully before playing.
- **Offline:** Use `Piper TTS` or `Edge TTS`.

### Voice Cloning Protocol
For perfect clones:
1.  **Source:** 1-5 minutes of high-quality audio.
2.  **Clean:** No background music, reverb, or other voices.
3.  **Delivery:** The clone mimics the *style* of the sample. If the sample is whispering, the clone will whisper. Upload different samples for different emotions.

## 3. Real-Time Pipeline (VAD)
For voice assistants, you need **Voice Activity Detection (VAD)**.
- Don't send silence to the API (costs money + latency).
- Use `Silero VAD` to detect when a user starts/stops speaking.

## Code Snippet: Minimal Latency Streaming (Concept)
```python
# Concept: Play chunks as they arrive
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Hello world",
    response_format="opus", # Lower bandwidth
)
for chunk in response.iter_bytes(chunk_size=1024):
    stream.write(chunk) # PortAudio stream
```

## Self-Improvement
- **Bad transcription?** -> Check if audio was clipped or too quiet.
- **Robot voice?** -> Check if you sent text with weird formatting (URLs, JSON).

## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Sovereign Standards?


## Related Skills
- [Sovereign Identity](../sovereign-identity/SKILL.md)
- [Prompt Architect](../prompt-architect/SKILL.md)
- [Context Manager](../context-manager/SKILL.md)
- [Ambiguity Handling](../ambiguity-handling/SKILL.md)
