# Understanding Java Interfaces

## Table of Contents

- [Understanding Java Interfaces](#understanding-java-interfaces)
  - [Table of Contents](#table-of-contents)
  - [Core Concepts](#core-concepts)
  - [Basic Interface Structure](#basic-interface-structure)
    - [Key Points](#key-points)
  - [Implementation Rules](#implementation-rules)
  - [Advanced Features](#advanced-features)
    - [Default Methods (Java 8+)](#default-methods-java-8)
    - [Interface Inheritance](#interface-inheritance)
    - [Interface as Type](#interface-as-type)
  - [Practical Applications](#practical-applications)
  - [Best Practices](#best-practices)

---

## Core Concepts

- An interface defines a contract of methods that implementing classes must follow
- Unlike multiple inheritance (not allowed in Java), interfaces provide a way to inherit from multiple sources
- Interfaces are similar to abstract classes but can't contain instance variables
- A class can implement multiple interfaces while extending only one class

---

## Basic Interface Structure

```java
public interface Strokeable {
   public void stroke(GraphicsContext g);
}

// Implementation
public class Line implements Strokeable {
    public void stroke(GraphicsContext g) {
        // Implementation here
    }
}
```

### Key Points

- Methods in interfaces are implicitly public and abstract
- Variables in interfaces are implicitly public, static, and final
- A class must use the `implements` keyword to implement an interface

---

## Implementation Rules

1. Class Implementation

   - Must implement all abstract methods from the interface
   - Can implement multiple interfaces
   - Can extend a class while implementing interfaces

2. Method Requirements
   - Must maintain the exact method signature
   - Must be public
   - Must provide concrete implementation

---

## Advanced Features

### Default Methods (Java 8+)

```java
public interface Readable {
    char readChar();  // abstract method

    default public String readLine() {  // default method
        // Implementation provided
    }
}
```

### Interface Inheritance

- Interfaces can extend other interfaces
- Can extend multiple interfaces unlike classes

```java
public interface Drawable extends Strokeable, Fillable {
    // Additional methods here
}
```

### Interface as Type

```java
Strokeable figure;  // Interface type variable
figure = new Line();  // Can hold implementing class instance
```

---

## Practical Applications

1. Type Definition

   - Declaring variables
   - Method parameters
   - Return types
   - Array types

2. Common Uses
   - Defining contracts
   - Creating pluggable architectures
   - Achieving loose coupling
   - Supporting polymorphism

---

## Best Practices

1. Keep interfaces focused and cohesive
2. Use interfaces for defining contracts
3. Prefer interfaces over abstract classes when possible
4. Use default methods judiciously
5. Document interface behavior clearly
