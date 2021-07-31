"""
Problem Statement:
There are 100 doors in a row that are all initially closed.
You make 100 passes by the doors.
The first time through, visit every door and  toggle the door (if the door is closed, open it. If it is open, close it).
The second time, only visit every 2nd door   (door #2, #4, #6, ...), and toggle it.
The third time, visit every 3rd door   (door #3, #6, #9, ...), etc, until you only visit the 100th door.

Task:
What state are the doors in after the last pass? Which are open, which are closed?
"""

if __name__ == '__main__':

    doors = [False] * 101
    open_doors = []
    closed_doors = []

    for i in range(1, 101):
        for j in range(i, 101, i):
            doors[j] = not doors[j]


    for i in range(1, 101):
        if doors[i]:
            open_doors.append(i)
        else:
            closed_doors.append(i)

    print(open_doors)
    print(closed_doors)
