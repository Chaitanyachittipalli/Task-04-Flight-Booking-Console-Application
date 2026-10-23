# Task 04: Flight Booking OOP Console Application

A console-based flight booking system implemented in Python demonstrating core Object-Oriented Programming (OOP) concepts.

## Features
- **Abstraction:** Abstract base class `Booking` defining the fare calculation contract.
- **Encapsulation:** Private attributes for sensitive booking details with controlled getter access.
- **Inheritance:** Derived classes `RegularBooking` and `StudentBooking` extending base booking functionality.
- **Polymorphism:** Dynamic discount calculation (0% for Regular, 10% for Students).
- **Input Validation:** Prevents empty inputs and handles numeric fare validation.

## How to Run
```bash
python main.py
