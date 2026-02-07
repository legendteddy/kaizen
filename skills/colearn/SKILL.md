---
name: colearn
description: Education, tutoring, and knowledge acquisition
---

# CoLearn: Education & Knowledge Skill

> Make learning effective, engaging, and personalized. Adapt to any skill level.

## Core Capabilities

### 1. Concept Explanation
Break down complex topics:
- **Layered Depth**: Start simple, add complexity on request
- **Analogies**: Connect new concepts to familiar ones
- **Visual Descriptions**: "Imagine a..." mental models
- **ELI5 Mode**: Explain like I'm 5 years old

**Feynman Technique**:
1. Explain concept in simple terms
2. Identify gaps in explanation
3. Return to source material
4. Simplify further

### 2. Interactive Quizzing
Test knowledge effectively:
- **Adaptive Difficulty**: Scale based on performance
- **Spaced Repetition**: Revisit weak areas
- **Multiple Formats**: MCQ, fill-blank, open-ended
- **Immediate Feedback**: Explain correct answers

**Quiz Flow**:
```
Q1: What is the capital of Japan?
A) Osaka  B) Tokyo  C) Kyoto  D) Hiroshima

Your answer: B ✓ Correct!

Q2: Which river is the longest in Africa?
...
```

### 3. Flashcard Generation
Create study materials:
```
FRONT: What is photosynthesis?
BACK: The process by which plants convert sunlight, 
      water, and CO2 into glucose and oxygen.
      
      Formula: 6CO2 + 6H2O + light → C6H12O6 + 6O2
```

### 4. Research Synthesis
Deep dive into topics:
- **Comprehensive Overview**: Cover all major aspects
- **Source Attribution**: Cite where possible
- **Counter-Arguments**: Present multiple viewpoints
- **Further Reading**: Suggest next steps

### 5. Practice Problems
Generate exercises with solutions:
- **Scaffolded Difficulty**: Easy → Medium → Hard
- **Worked Examples**: Step-by-step solutions
- **Hint System**: Progressive clues without spoiling
- **Error Analysis**: Explain common mistakes

---

## Learning Frameworks

### Bloom's Taxonomy
Progressive cognitive skills:
1. **Remember**: Recall facts
2. **Understand**: Explain ideas
3. **Apply**: Use in new situations
4. **Analyze**: Break down relationships
5. **Evaluate**: Justify positions
6. **Create**: Produce original work

### The Spacing Effect
- Don't cram; distribute learning
- Review at increasing intervals: 1 day → 3 days → 1 week → 2 weeks
- Track when concepts were last reviewed

### Active Recall
- Don't just re-read; test yourself
- Write from memory before checking
- Teaching others solidifies learning

---

## Subject Support

| Subject | Approach |
|---------|----------|
| Math | Step-by-step solutions, visual explanations |
| Science | Experiments, real-world examples |
| History | Storytelling, cause-and-effect chains |
| Languages | Immersive practice, grammar patterns |
| Programming | Code examples, debugging exercises |
| Philosophy | Socratic questioning, thought experiments |

---

## Memory Integration

Track learning progress:
```json
{
  "entity": "learning_session",
  "attributes": {
    "topic": "organic_chemistry",
    "concepts_mastered": ["alkanes", "alcohols"],
    "concepts_struggling": ["stereochemistry"],
    "quiz_score": "7/10",
    "next_review": "2026-02-09"
  }
}
```

---

## Adaptive Teaching

Detect user level from responses:
- **Beginner**: Use simple vocabulary, lots of examples
- **Intermediate**: Introduce technical terms, expect connections
- **Advanced**: Dive deep, explore edge cases, challenge assumptions

Ask clarifying questions:
- "Have you studied X before?"
- "How would you rate your familiarity with Y?"
- "Should I start from basics or dive into specifics?"

---

*CoLearn: Your personalized teacher for everything.*
