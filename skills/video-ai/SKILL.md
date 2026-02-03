---
name: video-ai
description: Skill for generating, editing, and processing video content (Sora, Runway, FFMPEG).
---

# Skill: Video AI & Processing (v1.0)

## Purpose
Navigate the landscape of Video AI tools and perform programmatic video editing.

## Activation Trigger
- "Make a video..."
- "Edit this clip..."
- "FFMPEG" mentioned.

---

## Protocol: FFMPEG Mastery

**Rule:** Always stream copy when possible to avoid re-encoding quality loss.

### Common Operations

**1. Cut/Trim:**
```bash
ffmpeg -i input.mp4 -ss 00:00:10 -t 00:00:05 -c copy output.mp4
```

**2. Extract Audio:**
```bash
ffmpeg -i input.mp4 -vn -acodec libmp3lame output.mp3
```

**3. Resize/Scale:**
```bash
ffmpeg -i input.mp4 -vf scale=1280:720 -c:a copy output.mp4
```

---

## Protocol: AI Video Generation

| Tool | Strength | Prompt Strategy |
|:---|:---|:---|
| **Sora** | Physics simulation | Describe lighting, camera angle, and movement physics. |
| **Runway Gen-3** | Stylization | Use "Motion Brush" concepts in prompt. |
| **Luma Dream Machine** | Keyframe animation | Define Start and End frames. |

**Prompt Template:**
"A cinematic wide shot of [SUBJECT], [ACTION], 4k resolution, shallow depth of field, golden hour lighting."