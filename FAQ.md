# Frequently Asked Questions

## General Usage

### Q: Does this happen automatically when I clone the repo?
**A: No.** You must define an AI agent (using Claude Desktop, Cursor, or a Python script) and tell it to "Read KAIZEN.md and activate it." The text files are the *instructions* for the agent, not executable code themselves.

### Q: Which AI models support this?
**A: Tested on:**
- Claude 3.5 Sonnet (Best performance)
- Gemini 1.5 Pro
- GPT-4o
- DeepSeek V3 (Good for reasoning skills)

### Q: Can I use this with ChatGPT (Web UI)?
**A:** Yes, but context is limited. Copy the contents of `UNIVERSAL_PROMPT.txt` into your "Custom Instructions" or paste it at the start of your chat.

### Q: How do I add my own skills?
**A:** Create a new markdown file in `skills/my-skill/SKILL.md`. Use the template in `CONTRIBUTING.md`.

---

## Technical

### Q: Why are the files in markdown?
**A:** Markdown is the native language of LLMs. It consumes fewer tokens than JSON/XML for this type of instructional data and is easier for humans to edit.

### Q: What is the "Step Zero" I keep seeing?
**A:** It's the core protocol: "Understand Purpose Before Action." It prevents the agent from rushing into coding before knowing *why* it's coding.

### Q: My agent is ignoring the skills. Why?
**A:**
1. Did you explicitly tell it to "Activate Kaizen"?
2. Is the `skills/` folder in its working directory?
3. Try pasting `UNIVERSAL_PROMPT.txt` into the chat context.
