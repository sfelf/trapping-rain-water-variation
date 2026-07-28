# Coding Interview Question
Below are the instructions for a recent Coding Interview question that is a variation on the Trapping Rain Water problem. There are three parts to the challenge. Solutions for parts one and three can be found in `terrain.py` and the solution for part two is in `fill.py`. The code in `main.py` can be used to run the solutions and `tests.py` runs multiple tests for the solution to part two.

## PART ONE:
Write a function called `printTerrain` which will take an array of numbers as input. Each value in the input array represents the height of an imaginary terrain which we will print to the console. For example:

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
Write a function `fill` which will take three arguments as input: a number `amount` which represents an amount of water we will be filling our imaginary terrain with, a number `pourPosition` which represents the horizontal location in our terrain where we will be pouring water, and an array of numbers `terrain` which is the same format at Part 1.
  
The `fill` function should return a NEW array of numbers which represent the heights of the terrain once it has been "filled" with `amount` of water poured at `pourPosition`.

### `fill` contract

- `amount` must be a non-negative integer. A value of `0` is valid and returns an unchanged copy of the terrain.
- `pourPosition` must be an integer identifying an existing position in `terrain`.
- Boolean values are not accepted as integers for either `amount` or `pourPosition`.
- The input terrain is never modified. The function always returns a new list for valid input.
- For each unit, `fill` searches outward from the pour position for a location where water can be contained. When equivalent candidates are found, the left position takes precedence.
- Water that cannot be contained by higher terrain on both sides spills and is not included in the returned terrain.

The function raises:
- `TypeError` when `amount` or `pourPosition` is not an integer, including boolean values.
- `ValueError` when `amount` is negative or `pourPosition` does not identify an element of `terrain`. Because an empty terrain has no valid position, it also results in `ValueError`.

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
Modify the `printTerrain` function to accept two arrays of numbers as input instead of one. The first will represent the "unfilled" terrain and the second will represent the "filled" terrain. Using the difference between these two arrays, print the terrain to the console, but use "w" to represent water. For example:
  
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
