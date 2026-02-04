---
name: video-ai
description: Protocols for generative video and programmatic editing (FFmpeg).
---

# Protocol: Video AI & Processing

## Activation Trigger
- Generating video prompts (Camera/Lighting).
- Editing video programmatically (FFmpeg).
- Upscaling or verifying video assets.

## 1. Generative Video Strategy
To get consistent, high-quality video, you must control the camera and physics.

### Prompting Structure
1.  **Camera Movement:** (Static, Pan Right, Zoom In, Drone Shot, Tracking Shot)
2.  **Subject Action:** (Walking forward, Looking at camera, Transforming)
3.  **Atmosphere:** (Golden hour, Cyberpunk neon, Foggy, Studio lighting)
4.  **Technical:** (4k, 60fps, shallow depth of field, anamorphic lens)

### Consistency Hacks
- **Image-to-Video:** Always prefer starting with a generated image (Midjourney) rather than Raw Text-to-Video for better composition control.
- **Reference Start/End:** If the tool supports it (Luma, Runway), define the end frame to control the trajectory.
- **Motion Bucket:** Lower motion = less artifacts. Higher motion = more chaos. Start low (3-4/10).

## 2. The Editing Pipeline (FFmpeg)

Avoid re-encoding whenever possible.

### Lossless Cut
`-c copy` is your best friend. It slices without decoding.
```bash
ffmpeg -i input.mp4 -ss 00:00:30 -to 00:00:40 -c copy output.mp4
```

### Quality Encoding (CRF)
When you MUST re-encode, control quality with CRF (18-28).
lower = better quality, higher size.
```bash
ffmpeg -i input.mp4 -vcodec libx264 -crf 23 -preset fast output.mp4
```

### Format Standardization
Convert weird formats to standard web-ready MP4.
```bash
ffmpeg -i input.mkv -c:v libx264 -profile:v high -level 4.0 -pix_fmt yuv420p -c:a aac output.mp4
```

## 3. Workflow: The 'Sandwich' Method
1.  **Generate Image:** Create the perfect keyframe.
2.  **Animate:** Use Image-to-Video (4s).
3.  **Extend:** If good, extend by 4s (using the last frame as input).
4.  **Upscale:** Use Topaz or AI upscaler as the FINAL step.

## Self-Improvement
- **Did the video look melty?** -> Reduce motion parameters.
- **Did FFMPEG invalid input?** -> Check if input file path has spaces (quote them).

## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Professional Standards?


## Related Skills
- [Agent Identity](../agent-identity/SKILL.md)
- [Prompt Architect](../prompt-architect/SKILL.md)
- [Context Manager](../context-manager/SKILL.md)
- [Ambiguity Handling](../ambiguity-handling/SKILL.md)
