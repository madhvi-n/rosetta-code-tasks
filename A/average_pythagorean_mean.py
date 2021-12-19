"""
Problem Statement:
Compute all three of the Pythagorean means of the set of integers 1 through 10 (inclusive).
The most common of the three means, the arithmetic mean, is the sum of the list divided by its length.
The geometric mean is the nth root of the product of the list.
The harmonic mean is {\displaystyle n} divided by the sum of the reciprocal of each item in the list.

"""
from typing import List
from functools import reduce


def arithmetic_mean(num: List[int]) -> float:
    mean = sum(num)/len(num)
    return round(mean, 2)


def geometric_mean(num : List[int]) -> float:
    result = reduce(lambda x, y: x * y, num)
    mean = result ** (1/len(num))
    return round(mean, 2)


def harmonic_mean(num: List[int]) -> float:
    mean = len(num)/ sum(1/n for n in num)
    return round(mean, 2)


def main():
    numbers = [x for x in range(1, 11)]
    ar = arithmetic_mean(numbers)
    gm = geometric_mean(numbers)
    hm = harmonic_mean(numbers)

    print(f"Arithmetic mean: {ar}")
    print(f"Geometric mean: {gm}")
    print(f"Harmonic mean: {hm}")


if __name__ == '__main__':
    main()
