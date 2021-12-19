"""
Display the complete lyrics for the song: 99 Bottles of Beer on the Wall.

The lyrics follow this form:

99 bottles of beer on the wall
99 bottles of beer
Take one down, pass it around
98 bottles of beer on the wall

98 bottles of beer on the wall
98 bottles of beer
Take one down, pass it around

"""
def solution():
    """Using while loop"""
    max = 99

    while max > 1:
        print(f"{max} bottles of beer on the wall")
        print(f"{max} bottles of beer")
        print(f"Take one down, pass it around")
        max -= 1
        print(f"{max} bottles of beer \n")


def main():
    solution()


if __name__ == '__main__':
    main()
