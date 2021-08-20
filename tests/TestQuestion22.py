"""
22. Number of Lists in a List
Return the total number of lists inside a given list.
Examples
num_of_sublists([[1, 2, 3]]) ➞ 1

num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) ➞ 3

num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]) ➞ 4

num_of_sublists([1, 2, 3]) ➞ 0

"""


def num_of_sublists(data_list):
    rez = 0
    i=0
    while(i < len(data_list)):
        if type(data_list[i]) == list:
            rez += 1
        i += 1
    return rez


#print(num_of_sublists([1, 2, 3]))