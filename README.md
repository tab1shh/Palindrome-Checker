# Palindrome-Checker

The palindrome checker function determines if a given string is a palindrome, ignoring non-alphanumeric characters and case differences.

## Table of Contents
- [Structure](#structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Palindrome Checker](#running-the-palindrome-checker)
- [Running Tests](#running-tests)

## Structure

- `palindrome_checker.py`: Contains the `is_palindrome` function.
- `test_palindrome_checker.py`: Contains unit tests for the `is_palindrome` function.

## Getting Started

### Prerequisites
Ensure you have Python installed on your system. 

### Installation
1. Clone the repository or download the files.
2. Navigate to the project directory.

### Running the Palindrome Checker

You can use the `is_palindrome` function directly in your Python scripts. Here is an example:

```python
from palindrome_checker import is_palindrome

test_string = "A man, a plan, a canal, Panama"
print(f"'{test_string}' is a palindrome: {is_palindrome(test_string)}")
```

## Running Tests
Run the test suite using 'unittest' or 'pytest'.
Using 'unittest'
```python
python -m unittest discover tests
```
Using pytest
```python
pytest
```