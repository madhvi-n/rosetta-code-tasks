"""
Problem Statement:
Determine the amount of elements in an array.
As an example use an array holding the strings 'apple' and 'orange'.
"""


def solution():
    fruits = ['apples', 'mango', 'grapes', 'berries', 'banana', 'kiwi']
    numbers = [x for x in range(1, 11)]

    print(f"Length of fruits: {len(fruits)}")
    print(f"Length of numbers: {len(numbers)}")


def main():
    solution()


if __name__ == '__main__':
    main()
