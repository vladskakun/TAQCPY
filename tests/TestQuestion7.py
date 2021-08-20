"""
Check If Lines Are Parallel
Given two lines, determine whether or not they are parallel.
Lines are represented by a list [a, b, c], which corresponds to the line ax+by=c.
Examples
lines_are_parallel([1, 2, 3], [1, 2, 4]) ➞ true
# x+2y=3 and x+2y=4 are parallel.

lines_are_parallel([2, 4, 1], [4, 2, 1]) ➞ false
# 2x+4y=1 and 4x+2y=1 are not parallel.

lines_are_parallel([0, 1, 5], [0, 1, 5]) ➞ true
# Lines are parallel to themselves.
Notes
•	All the coefficients will be integers (whole numbers).

"""


def lines_are_parallel(list_1, list_2):
    if list_1[0] / list_2[0] == list_1[1] / list_2[1]:
        return True
    elif list_1[0] / list_2[0] == list_1[1] / list_2[1] == list_1[2] / list_2[2]:
        # return  'Lines are parallel to themselves'
        return True
    else:
        return False


#print(lines_are_parallel([1, 2, 3], [1, 2, 4]))
