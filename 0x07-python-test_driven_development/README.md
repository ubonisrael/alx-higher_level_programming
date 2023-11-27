# 0x07. Python - Test-driven development


## Concepts

For this project, we expect you to look at this concept:
- Never forget a test


## Background Context

Important notice on intranet checks for Python projects

Starting from today:

- Based on the requirements of each task, you should always write the documentation (module(s) + function(s)) and tests first, before you actually code anything
- The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case. But not in the implementation of them!
- Don’t trust the user, always think about all possible edge cases


## Resources

Read or watch:

- doctest — Test interactive Python examples (until “26.2.3.7. Warnings” included)
- doctest – Testing through documentation
- Unit Tests in Python
- Unittest module
- Interactive and Non-interactive tests


## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- Why Python programming is awesome
- What’s an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases


### Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.


## Tasks

- 0. Integers addition
  - Write a function that adds 2 integers.
    -Prototype: def add_integer(a, b=98):
    - a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
    - a and b must be first casted to integers if they are float
    - Returns an integer: the addition of a and b
    - You are not allowed to import any module

- 1. Divide a matrix
  - Write a function that divides all elements of a matrix.
    -Prototype: def matrix_divided(matrix, div):
    - matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
    - Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
    - div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
    - div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
    - All elements of the matrix should be divided by div, rounded to 2 decimal places
    - Returns a new matrix
    - You are not allowed to import any module

- 2. Say my name
  - Write a function that prints My name is <first name> <last name>
    - Prototype: def say_my_name(first_name, last_name=""):
    - first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string
    - You are not allowed to import any module
