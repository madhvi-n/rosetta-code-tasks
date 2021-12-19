"""
Problem Statement:
Compute the   Root mean square   of the numbers 1..10.
The   root mean square   is also known by its initials RMS (or rms), and as the quadratic mean.
The RMS is calculated as the mean of the squares of the numbers, square-roote
"""
import typing
from math import sqrt


def get_sum(n: int) -> int:
    """Returns sum of n natural numbers using A.P"""
    result = (n * (n+1) * (2*n + 1))/6
    return result


def root_mean_square(max_num: int = 10) -> int:
    mean = round(sqrt(get_sum(max_num) / max_num), 2)
    print(mean)


def main():
    root_mean_square()


if __name__ == '__main__':
    main()
