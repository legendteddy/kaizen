---
name: software-architecture
description: Enterprise-grade patterns including SOLID principles, Clean Architecture, and design patterns.
---

# Software Architecture (Enterprise Patterns)

> "Architecture is about the important stuff. Whatever that is."

## Activation Trigger
- Designing a new module or service.
- Refactoring legacy code (Code Smells).
- Deciding on design patterns (Factory/Strategy).

## Protocols

### 1. First Principle: Separation of Concerns
Things that change for different reasons should be separated.

### 2. SOLID Enforcement
- **S**: Single Responsibility (One class, one job).
- **O**: Open/Closed (Extend, don't modify).
- **L**: Liskov Substitution (Subtypes must be substitutable).
- **I**: Interface Segregation (Small interfaces > Big ones).
- **D**: Dependency Inversion (Depend on abstractions).

### 3. Clean Architecture
Dependencies point INWARD.
`Infrastructure -> Interface Adapters -> Use Cases -> Entities`

## Code Patterns

### The Factory Pattern
```javascript
class NotificationFactory {
  create(type) {
    if (type === 'email') return new EmailNotifier();
    if (type === 'sms') return new SMSNotifier();
    throw new Error('Unknown type');
  }
}
```

### The Strategy Pattern
```javascript
// Interchangeable algorithms
class Order {
  constructor(pricingStrategy) {
    this.pricing = pricingStrategy;
  }
  
  total() {
    return this.pricing.calculate(this.items);
  }
}
```

## Safety Guardrails
- **No God Classes**: Any class over 200 lines is suspect.
- **No Circular Dependencies**: Module A requires B requires A = Fatal.
- **YAGNI**: Do not build generic systems for a single use case.
- **Abstraction Cost**: Do not abstract until you have 3 examples of duplication.
- **Explicit Interfaces**: Typed languages must use Interfaces/Types for boundaries.
