# Coding Interview Question
Below are the instructions for a recent Coding Interview question that is a variation on the Trapping Rain Water problem. There are three parts to the challenge. Solutions for parts one and three can be found in `terrain.py` and the solution for part two is in `fill.py`. The code in `main.py` can be used to run the solutions. The pytest suite in `tests/` covers both the `fill` and `print_terrain` functions.

## PART ONE:
Write a function called `print_terrain` which will take a sequence of numbers as input. Each value in the input sequence represents the height of an imaginary terrain which we will print to the console. For example:

     Input:
     [5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3]
  
     Should Print:
     +           
     ++        + 
     ++  +     ++
     +++ +++   ++
     ++++++++ +++
     ++++++++++++

## PART TWO:
Write a function `fill` which will take three arguments as input: a number `amount` which represents an amount of water we will be filling our imaginary terrain with, a number `pour_position` which represents the horizontal location in our terrain where we will be pouring water, and a list of numbers `terrain` which is the same format at Part 1.
  
The `fill` function should return a NEW list of numbers which represent the heights of the terrain once it has been "filled" with `amount` of water poured at `pour_position`.

For example:
  
    Input:
    (4, 6, [5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3])
  
    Output:
    [5, 4, 2, 1, 3, 2, 2, 2, 2, 2, 4, 3]
  
     Visualization of what a "filled" terrain looks like:
     +           
     ++        + 
     ++  +     ++
     +++ +++www++
     ++++++++w+++
     ++++++++++++

## PART THREE:
Modify the `print_terrain` function to accept two sequences of numbers as input instead of one. The first will represent the "unfilled" terrain and the second will represent the "filled" terrain. Using the difference between these two sequences, print the terrain to the console, but use "w" to represent water.

For example:

     Input:
     [5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3]
     [5, 4, 2, 1, 3, 2, 2, 2, 2, 2, 4, 3]
  
     Should Print:
     +           
     ++        + 
     ++  +     ++
     +++ +++www++
     ++++++++w+++
     ++++++++++++

## Function Contracts

### `fill` contract

- `amount` must be a non-negative integer. A value of `0` is valid and returns an unchanged copy of the terrain.
- `pour_position` must be an integer identifying an existing position in `terrain`.
- Boolean values are not accepted as integers for either `amount` or `pour_position`.
- Every terrain height must be a non-negative integer. Boolean values are rejected as heights.
- The input terrain is never modified. The function always returns a new list for valid input.
- For each unit, `fill` searches outward from the pour position for a location where water can be contained. When equivalent candidates are found, the left position takes precedence.
- Water that cannot be contained by higher terrain on both sides spills and is not included in the returned terrain.

The function raises:
- `TypeError` when `amount`, `pour_position`, or a terrain height is not an integer, including boolean values.
- `ValueError` when `amount` or a terrain height is negative, or when `pour_position` does not identify an element of `terrain`. Because an empty terrain has no valid position, it also results in `ValueError`.

### `print_terrain` contract

- `terrain` must be a nonempty sequence of non-negative integers.
- When supplied, `water` must be a nonempty sequence of non-negative integers with the same length as `terrain`.
- Boolean values are rejected as heights.
- Every `water` value must be greater than or equal to its corresponding `terrain` value.

The function raises:
- `TypeError` when `terrain` or `water` contain invalid height types.
- `ValueError` when `terrain` or `water` contain invalid values or relationships.

## Running the example

This repository is structured as a standalone Python script project rather than
an installable Python package.

Run the example from the repository root:

```bash
python main.py
```

## Running the tests

Create an isolated development environment and install the test dependency:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

Run the automatically discovered test suite from the repository root:

```bash
.venv/bin/python -m pytest
```

Alternatively, let pipx provide an isolated pytest environment without adding
pytest to the project environment or base Python:

```bash
pipx run pytest .
```
