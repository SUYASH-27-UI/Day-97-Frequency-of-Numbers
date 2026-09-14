# Day-97-Frequency-of-Numbers
# Python Day 97 - Frequency of Numbers

This program finds how many times each number appears in a list.

## Example

Input:

```text
[10, 20, 10, 30, 20, 10, 40, 30]
```

Output:

```text
10 appears 3 times
20 appears 2 times
30 appears 2 times
40 appears 1 times
```

## Concepts Used

* Lists
* `for` loop
* `if` condition
* `count()` method
* `not in` operator
* `append()` method

## How It Works

1. Create a list of numbers.
2. Create an empty `checked` list.
3. Use a `for` loop to check every number.
4. Check whether the number is already in `checked`.
5. If it is not present, use `count()` to find its frequency.
6. Add the number to `checked` so it is not counted again.

## Python Code

```python
numbers = [10, 20, 10, 30, 20, 10, 40, 30]

checked = []

for number in numbers:
    if number not in checked:
        print(number, "appears", numbers.count(number), "times")
        checked.append(number)
```

## Output

```text
10 appears 3 times
20 appears 2 times
30 appears 2 times
40 appears 1 times
```

## Goal

The goal of this project is to practice Python lists, loops, conditions, and the `count()` method.
