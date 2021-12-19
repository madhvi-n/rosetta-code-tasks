"""
For a given range, replace every multiple of 3 with "Fizz",
every multiple of 5 with "Buzz", and every multiple of 7 with "Baxx".

In the case where a number is a multiple of at least two factors, print each of the words
associated with those factors in the order of least to greatest factor.
"""

def fizzbuzz(n):
    mappings = { 3: "Fizz", 5: "Buzz", 7: "Baxx" }
    for i in range(1, n+1):
        print(''.join( word * (i % key == 0) for  key, word in mappings.items()) or i)


def main():
    fizzbuzz(100)


if __name__ == '__main__':
    main()
