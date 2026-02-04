# Contributing to Kaizen

We treat this repository as a "Cognitive Codebase". Each file adds a capability to the AI.

## How to Add a Skill

1. **Copy the Template**
   ```bash
   cp templates/NEW_SKILL.md skills/your-skill-name/SKILL.md
   ```

2. **Define the Header**
   The YAML frontmatter is critical for the indexer.
   ```yaml
   ---
   name: your-skill-name
   description: 10-15 words. Specific and searchable.
   ---
   ```

3. **Write the Logic**
   - Use **imperative mood** ("Do this", not "You should do this").
   - Include **Guardrails** ("Never delete without asking").
   - Providing **Examples** is the best way to steer behavior.

## How to Improve a Skill

1. **Profile**: Where did the agent fail?
2. **Patch**: Edit the markdown to explicitly handle that edge case.
3. **Verify**: Test the new prompt.

## Style Guide
- **Concise**: Agents have token limits. Be brief.
- **Structural**: Use headers (#, ##) to organize thought.
- **Explicit**: Don't just imply rules; state them.