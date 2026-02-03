---
name: voice-ai
description: Skill for Text-to-Speech (TTS), Speech-to-Text (STT), and Voice Cloning.
---

# Skill: Voice AI Models (v1.0)

## Purpose
Implement voice interfaces using ElevenLabs, OpenAI Whisper, or local models.

## Activation Trigger
- "Transcribe this audio"
- "Generate speech"
- "Voice clone"

---

## Protocol: Transcription (STT)

### OpenAI Whisper (Python)
```python
import openai

audio_file = open("audio.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript["text"])
```

### Local Whisper (Faster-Whisper)
**Use when:** Privacy is required or offline.
```python
from faster_whisper import WhisperModel

model = WhisperModel("large-v3", device="cuda", compute_type="float16")
segments, info = model.transcribe("audio.mp3", beam_size=5)
```

---

## Protocol: Synthesis (TTS)

### ElevenLabs (High Quality)
- **Latency:** ~1s
- **Cost:** High
- **Use:** Final production audio.

### OpenAI TTS (Speed)
- **Latency:** ~300ms
- **Cost:** Low
- **Use:** Real-time chat.

### Edge TTS (Local)
**Use:** Zero cost, offline.
```python
import edge_tts
import asyncio

async def main():
    communicate = edge_tts.Communicate("Hello World", "en-US-AriaNeural")
    await communicate.save("hello.mp3")
```