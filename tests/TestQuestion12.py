"""
12. Concatenate Variable Number of Input Lists
Create a function that concatenates n input lists, where n is variable.
Examples
concat([1, 2, 3], [4, 5], [6, 7]) ➞ [1, 2, 3, 4, 5, 6, 7]

concat([1], [2], [3], [4], [5], [6], [7]) ➞ [1, 2, 3, 4, 5, 6, 7]

concat([1, 2], [3, 4]) ➞ [1, 2, 3, 4]

concat([4, 4, 4, 4, 4]) ➞ [4, 4, 4, 4, 4]
Notes
Lists should be concatenated in order of the arguments.

"""


def concat(*lists):
    summ = []
    for list1 in lists:
        summ = summ + list1
    return summ
a=[1,3,5]
b=[2,4,6]
c=[0,-1]

#print(concat(a,b,c))