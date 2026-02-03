---
name: software-architecture
description: Enterprise-grade patterns including SOLID principles, Clean Architecture, design patterns, and code smell detection.
---

# Software Architecture — Enterprise Patterns

This skill enforces **professional architecture standards**. Every system you build should be maintainable, scalable, and beautiful.

## Activation Trigger
- Designing a new module or service.
- Refactoring legacy code (Code Smells).
- Deciding on design patterns (Factory/Strategy).

---

## 1. SOLID Principles

### S — Single Responsibility
```javascript
// ❌ One class doing everything
class UserManager {
  createUser(data) { ... }
  sendWelcomeEmail(user) { ... }
  validatePassword(password) { ... }
  logActivity(action) { ... }
  generateReport() { ... }
}

// ✅ Single responsibility per class
class UserService { createUser(data) { ... } }
class EmailService { sendWelcomeEmail(user) { ... } }
class PasswordValidator { validate(password) { ... } }
class ActivityLogger { log(action) { ... } }
class ReportGenerator { generate() { ... } }
```

### O — Open/Closed
```javascript
// ❌ Must modify code to add new behavior
function calculateArea(shape) {
  if (shape.type === 'circle') return Math.PI * shape.radius ** 2;
  if (shape.type === 'square') return shape.side ** 2;
  // Must add new if-else for every shape...
}

// ✅ Open for extension, closed for modification
interface Shape {
  area(): number;
}

class Circle implements Shape {
  constructor(private radius: number) {}
  area() { return Math.PI * this.radius ** 2; }
}

class Square implements Shape {
  constructor(private side: number) {}
  area() { return this.side ** 2; }
}
```

### L — Liskov Substitution
```javascript
// ❌ Subclass breaks parent behavior
class Bird {
  fly() { return 'flying'; }
}

class Penguin extends Bird {
  fly() { throw new Error('Cannot fly'); }  // Breaks LSP!
}

// ✅ Proper abstraction
interface Animal { move(): string; }
class FlyingBird implements Animal { move() { return 'flying'; } }
class SwimmingBird implements Animal { move() { return 'swimming'; } }
```

### I — Interface Segregation
```javascript
// ❌ Fat interface
interface Worker {
  work(): void;
  eat(): void;
  sleep(): void;
}

// Robot can work but can't eat or sleep!

// ✅ Segregated interfaces
interface Workable { work(): void; }
interface Eatable { eat(): void; }
interface Sleepable { sleep(): void; }

class Human implements Workable, Eatable, Sleepable { ... }
class Robot implements Workable { ... }
```

### D — Dependency Inversion
```javascript
// ❌ High-level depends on low-level
class OrderService {
  private db = new MySQLDatabase();  // Direct dependency
  
  save(order) { this.db.insert(order); }
}

// ✅ Both depend on abstractions
interface Database { insert(data: any): void; }

class OrderService {
  constructor(private db: Database) {}  // Injected
  save(order) { this.db.insert(order); }
}
```

---

## 2. Clean Architecture Layers

```
┌─────────────────────────────────────────┐
│           Frameworks & Drivers          │  ← Express, React, PostgreSQL
│  ┌─────────────────────────────────┐    │
│  │     Interface Adapters          │    │  ← Controllers, Presenters
│  │  ┌─────────────────────────┐    │    │
│  │  │   Application Layer     │    │    │  ← Use Cases
│  │  │  ┌─────────────────┐    │    │    │
│  │  │  │   Domain Layer  │    │    │    │  ← Entities, Business Rules
│  │  │  └─────────────────┘    │    │    │
│  │  └─────────────────────────┘    │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘

Dependencies point INWARD only.
Inner layers know nothing about outer layers.
```

### Layer Responsibilities

| Layer | Contains | Example |
|-------|----------|---------|
| **Domain** | Entities, Value Objects, Business Rules | `User`, `Order`, `validatePrice()` |
| **Application** | Use Cases, DTOs | `CreateOrderUseCase`, `OrderDTO` |
| **Interface** | Controllers, Presenters, Gateways | `OrderController`, `PDFPresenter` |
| **Infrastructure** | Frameworks, Databases, APIs | `ExpressApp`, `PostgresRepo` |

---

## 3. Design Patterns

### Creational Patterns

#### Factory
```javascript
// When: Object creation is complex or varies by type
class NotificationFactory {
  create(type: 'email' | 'sms' | 'push'): Notification {
    switch (type) {
      case 'email': return new EmailNotification();
      case 'sms': return new SMSNotification();
      case 'push': return new PushNotification();
    }
  }
}
```

#### Builder
```javascript
// When: Object has many optional parameters
const user = new UserBuilder()
  .withName('John')
  .withEmail('john@example.com')
  .withRole('admin')
  .build();
```

#### Singleton
```javascript
// When: Only one instance should exist
class Database {
  private static instance: Database;
  
  private constructor() {}
  
  static getInstance(): Database {
    if (!Database.instance) {
      Database.instance = new Database();
    }
    return Database.instance;
  }
}
```

### Structural Patterns

#### Adapter
```javascript
// When: Incompatible interfaces need to work together
class OldPaymentGateway {
  processPayment(amount: number) { ... }
}

class PaymentAdapter implements NewPaymentInterface {
  constructor(private legacy: OldPaymentGateway) {}
  
  pay(request: PaymentRequest) {
    return this.legacy.processPayment(request.amount);
  }
}
```

#### Facade
```javascript
// When: Complex subsystem needs a simple interface
class OrderFacade {
  constructor(
    private inventory: InventoryService,
    private payment: PaymentService,
    private shipping: ShippingService
  ) {}
  
  placeOrder(order: Order) {
    this.inventory.reserve(order.items);
    this.payment.charge(order.total);
    this.shipping.schedule(order);
  }
}
```

### Behavioral Patterns

#### Strategy
```javascript
// When: Algorithm should be interchangeable
interface PricingStrategy {
  calculate(basePrice: number): number;
}

class RegularPricing implements PricingStrategy {
  calculate(price: number) { return price; }
}

class VIPPricing implements PricingStrategy {
  calculate(price: number) { return price * 0.8; }
}

class Order {
  constructor(private pricing: PricingStrategy) {}
  
  getTotal(basePrice: number) {
    return this.pricing.calculate(basePrice);
  }
}
```

#### Observer
```javascript
// When: Many objects need to react to changes
class EventEmitter {
  private listeners: Map<string, Function[]> = new Map();
  
  on(event: string, callback: Function) {
    const list = this.listeners.get(event) || [];
    list.push(callback);
    this.listeners.set(event, list);
  }
  
  emit(event: string, data: any) {
    this.listeners.get(event)?.forEach(cb => cb(data));
  }
}
```

---

## 4. Code Smell Detection

### Long Method (>20 lines)
**Smell**: Function does too many things  
**Fix**: Extract smaller functions

### Large Class (>200 lines)
**Smell**: Class has too many responsibilities  
**Fix**: Split into focused classes

### Feature Envy
**Smell**: Method uses another class's data more than its own  
**Fix**: Move method to the class it envies

### Data Clumps
**Smell**: Same group of variables appears together repeatedly  
**Fix**: Extract into a class

### Primitive Obsession
**Smell**: Using primitives instead of small objects  
**Fix**: Create value objects (e.g., `Money`, `Email`, `PhoneNumber`)

### Shotgun Surgery
**Smell**: One change requires edits in many places  
**Fix**: Consolidate related code

### Divergent Change
**Smell**: One class changed for many different reasons  
**Fix**: Split by responsibility

---

## 5. File Organization

### Feature-Based Structure
```
src/
├── features/
│   ├── auth/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── services/
│   │   └── index.ts
│   ├── orders/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── services/
│   │   └── index.ts
├── shared/
│   ├── components/
│   ├── hooks/
│   └── utils/
└── app/
    ├── routes.ts
    └── main.ts
```

### Layer-Based Structure (for backend)
```
src/
├── domain/
│   ├── entities/
│   └── value-objects/
├── application/
│   ├── use-cases/
│   └── dtos/
├── infrastructure/
│   ├── database/
│   ├── http/
│   └── external-services/
└── main.ts
```

---

## 6. Refactoring Checklist

Before starting:
- [ ] Tests exist and pass
- [ ] Version control is clean
- [ ] Understand current behavior

During:
- [ ] One small change at a time
- [ ] Run tests after each change
- [ ] Commit frequently

After:
- [ ] All tests still pass
- [ ] Code is more readable
- [ ] No functionality changed

---

*"Any fool can write code that a computer can understand. Good programmers write code that humans can understand." — Martin Fowler*
