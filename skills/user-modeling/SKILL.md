---
name: user-modeling
description: Understand and adapt to user preferences, patterns, and expertise.
---

# User Modeling

> Every user is different. Adapt to them, not the other way around.

## Activation Trigger
- New user interaction
- User expresses preference
- User corrects approach
- Communication style mismatch

---

## User Model Components

```
┌─────────────────────────────────────────────────────────────────┐
│                    USER MODEL                                   │
│                                                                 │
│  EXPERTISE:    [Beginner / Intermediate / Expert]              │
│  STYLE:        [Detailed / Concise]                            │
│  PACE:         [Fast / Deliberate]                             │
│  PREFERENCES:  [Specific patterns observed]                    │
│  CONSTRAINTS:  [Time, resources, limitations]                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Expertise Detection

| Signal | Likely Expertise |
|:---|:---|
| Uses jargon correctly | Expert |
| Asks "how" questions | Intermediate |
| Asks "what" questions | Beginner |
| Provides detailed specs | Expert |
| Gives vague requirements | Needs guidance |

## Style Adaptation

```
FOR EXPERTS:
- Skip basics
- Use technical terms
- Provide options
- Trust their judgment

FOR BEGINNERS:
- Explain concepts
- Use analogies
- Give recommendations
- Confirm understanding
```

## Preference Learning

Observe and remember:
```
□ Code style preferences (tabs/spaces, naming)
□ Communication preferences (verbose/terse)
□ Tool preferences (frameworks, editors)
□ Decision style (quick/deliberate)
□ Review style (detailed/high-level)
```

## Adaptation in Action

```
IF: User prefers concise
THEN: Bullet points, minimal prose

IF: User prefers detailed
THEN: Full explanations, examples

IF: User is time-constrained
THEN: Quick answers, defer details

IF: User wants to learn
THEN: Explain the why, teach patterns
```

## Building the Model

```
1. Start with neutral assumptions
2. Observe user patterns
3. Note explicit preferences
4. Adjust approach accordingly
5. Verify adaptation is working
```

## Self-Improvement Hook

After interaction:
```
□ Did I match user's expectations?
□ What preferences did I learn?
□ Should I adjust my model?
```
