# Understanding Inheritance in Java

## Table of Contents

- [Understanding Inheritance in Java](#understanding-inheritance-in-java)
  - [Table of Contents](#table-of-contents)
  - [Core Concepts](#core-concepts)
  - [Basic Syntax](#basic-syntax)
  - [Important Rules](#important-rules)
  - [Abstract Classes](#abstract-classes)
  - [Advanced Concepts](#advanced-concepts)
    - [Complex Inheritance Hierarchies](#complex-inheritance-hierarchies)
    - [Protected Access Modifier](#protected-access-modifier)
    - [Final Methods and Classes](#final-methods-and-classes)
    - [Pattern Matching](#pattern-matching)
    - [Object Class](#object-class)
  - [Best Practices for Beginners](#best-practices-for-beginners)
  - [Note](#note)

---

## Core Concepts

- Inheritance: A class can inherit properties and methods from another class
- Subclass: The class that inherits (child)
- Superclass: The class being inherited from (parent)
- Polymorphism: Objects of different classes can respond differently to the same method call

---

## Basic Syntax

```java
public class Subclass extends Superclass {
    // New or modified methods/properties
}
```

---

## Important Rules

- A subclass inherits all non-private members from its superclass
- A subclass can add new members or override existing ones
- A variable of a superclass type can hold references to subclass objects
- You can't assign a superclass reference to a subclass variable without casting

---

## Abstract Classes

- Cannot be instantiated directly
- Serve as templates for other classes
- May contain abstract methods (methods without implementation)
- Concrete subclasses must implement all abstract methods

Example:

```java
abstract class Shape {
    abstract void draw(); // Abstract method
}

class Rectangle extends Shape {
    void draw() {
        // Specific implementation for rectangle
    }
}
```

---

## Advanced Concepts

### Complex Inheritance Hierarchies

```java
// Example of multi-level inheritance
class Vehicle { }
class Car extends Vehicle { }
class ElectricCar extends Car { }
```

- Classes can form chains of inheritance
- Each subclass inherits from all classes above it in the chain
- Best practice: Keep hierarchies shallow to maintain simplicity

### Protected Access Modifier

```java
class Parent {
    protected int value; // Accessible by subclasses
}
```

- More permissive than private but more restrictive than public
- Accessible by:
  - The class itself
  - Its subclasses
  - Classes in the same package

### Final Methods and Classes

```java
final class CannotBeExtended {
    // This class can't have subclasses
}
```

- Use final class when you want to prevent inheritance
- Use final methods when you want to prevent method overriding
- Common use: Security and ensuring consistent behavior

### Pattern Matching

```java
// Modern approach with pattern matching (Java 17+)
if (obj instanceof Car car) {
    car.drive(); // No explicit casting needed
}
```

### Object Class

- Root of all Java class hierarchy
- Provides basic methods:
  - toString()
  - equals()
  - hashCode()
  - getClass()

---

## Best Practices for Beginners

1. Start with understanding basic inheritance syntax
2. Practice extending existing classes
3. Learn basic polymorphism concepts
4. Understand when to use abstract classes
5. Learn advanced concepts as needed for specific projects

---

## Note

Remember: While these concepts are important to know about, you don't need to master them all at once. Learn them as you encounter situations that require them.
