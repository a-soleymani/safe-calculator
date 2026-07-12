# Safe Calculator

A simple command-line calculator built with Python to practice functions, exception handling, input validation, and unit testing.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Handles invalid user input (`ValueError`)
- Prevents division by zero (`ZeroDivisionError`)
- Menu-driven interface
- Supports decimal numbers (`float`)
- Unit tests written using Python's `unittest`

## Project Structure

```
safe-calculator/
├── calculator.py
├── test_calculator.py
└── README.md
```

## Requirements

- Python 3.10 or later

## Running the Application

```bash
python calculator.py
```

## Running the Tests

```bash
python -m unittest test_calculator.py
```

## Example

```
Please enter your first number: 10
Please enter your second number: 5

1. plus
2. minus
3. divide
4. multiplication

Please enter your choice: 3

2.0
```

## Concepts Practiced

- Functions
- Loops (`while`)
- Conditional statements (`if`, `elif`, `else`)
- Exception handling (`try` / `except`)
- Input validation
- Unit testing with `unittest`

## Future Improvements

- Add modulus (`%`)
- Add exponentiation (`**`)
- Save calculation history to a file
- Support more mathematical operations
- Improve the command-line interface

## License

This project is for educational purposes.
