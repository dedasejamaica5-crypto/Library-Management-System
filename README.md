# Library Management System

A comprehensive command-line library management system built with Python. This system allows librarians to manage books, members, and book borrowing/returning transactions efficiently.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [System Architecture](#system-architecture)
- [API Reference](#api-reference)
- [Error Handling](#error-handling)
- [Data Flow](#data-flow)
- [Example Usage](#example-usage)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

The Library Management System provides the following core functionalities:

### 1. **Add Book** (Menu Option 1)
- Add new books to the library inventory
- Each book has a unique ID, title, and author
- Books are initially marked as available
- Prevents duplicate entries in the system

### 2. **Register Member** (Menu Option 2)
- Register new library members
- Each member has a unique ID, name, and email address
- Store member contact information for loan records
- Manage member database efficiently

### 3. **Borrow Book** (Menu Option 3)
- Members can borrow available books
- Validates both book and member existence
- Checks book availability before borrowing
- Creates a loan record with automatic loan ID generation
- Marks book as unavailable after borrowing

**Error Handling:**
- `BookNotFoundError` - Book ID doesn't exist
- `MemberNotFoundError` - Member ID doesn't exist
- `BookUnavailableError` - Book is already borrowed

### 4. **Return Book** (Menu Option 4)
- Members return borrowed books
- Requires a valid loan ID
- Marks the book as available again
- Closes the loan record and records return date
- Displays confirmation message

### 5. **View Books** (Menu Option 5)
- Display all books in the library
- Shows book ID, title, author, and availability status
- Color-coded status (Available/Borrowed)
- Useful for inventory management

### 6. **View Members** (Menu Option 6)
- Display all registered library members
- Shows member ID, name, and email
- Useful for member management and contact purposes

### 7. **View Loans** (Menu Option 7)
- Display all active and closed loans
- Shows loan ID, member name, book title, and loan status
- Tracks borrowing history
- Useful for auditing and reports

### 8. **Exit** (Menu Option 8)
- Gracefully exit the application
- Displays goodbye message

---

## 📁 Project Structure


### File Descriptions

#### `main.py`
- Entry point for the application
- Implements the CLI menu interface
- Handles user input and displays output
- Calls appropriate service methods based on user choice
- Implements exception handling for user-friendly error messages

#### `library_service.py`
- Contains the `LibraryService` class
- Manages all business logic
- Maintains data structures for books, members, and loans
- Validates operations before executing them
- Generates automatic loan IDs

#### `exceptions.py`
- Defines 4 custom exception classes:
  - `BookNotFoundError`
  - `MemberNotFoundError`
  - `BookUnavailableError`
  - `LoanNotFoundError`

#### `book.py`
- Defines the `Book` class
- Properties: `book_id`, `title`, `author`, `available`
- Methods: `borrow()`, `return_book()`
- String representations for display

#### `member.py`
- Defines the `Member` class
- Properties: `member_id`, `name`, `email`
- String representations for display

#### `loan.py`
- Defines the `Loan` class
- Properties: `loan_id`, `book`, `member`, `loan_date`, `return_date`, `is_active`
- Methods: `close_loan()`
- Tracks loan timestamps

---

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Git

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/dedasejamaica5-crypto/Library-Management-System.git
cd Library-Management-System
