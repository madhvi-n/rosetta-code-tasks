"""
Problem Statement:
Show how to concatenate two arrays in your language.
If this is as simple as array1 + array2, so be it.

"""
def solution():
    array1 = [x for x in range(1, 10, 2)]
    array2 = [x for x in range(3, 10, 3)]
    array3 = [x for x in range(5, 10, 5)]

    print(f"First array: {array1}")
    print(f"Second array: {array2}")

    array2 = array1 + array2
    print(f"First array + Second array: {array2}")

    array3.extend(array2)
    print(f"Third array: {array3}")


def main():
    solution()

if __name__ == '__main__':
    main()
