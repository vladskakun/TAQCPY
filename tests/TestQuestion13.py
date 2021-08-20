"""
13. Emptying the values
Given a list of values, return a list with each value replaced with the empty value of the same type. More explicitly:
•	replace integers (e.g. 1, 3), whose type is "int", with 0
•	replace floats (e.g. 3.14, 2.17), whose type is "float", with 0.0
•	replace strings (e.g. 'abcde', 'x'), whose type is "str", with ''
•	replace booleans (True, False), whose type is "bool", with False
•	replace lists (e.g. [1, 'a', 5], [[4]]), whose type is "list", with []
•	replace tuples (e.g. (1,9,0), (2,)), whose type is "tuple", with ()
•	replace sets (e.g. {0,'a'}, {'b'}), whose type is "set", with set() (caution: python interprets {} as the empty dictionary, not the empty set)
•	None, whose type is "NoneType", is preserved as None
Examples
[1, 2, 3] ➞ [0, 0, 0]

[7, 3.14, 'cat'] ➞ [0, 0.0, '']

[[1, 2, 3], (1,2,3), {1,2,3}] ➞ [[], (), set()]

[[7, 3.14, 'cat']] ➞ [[]]

[None] ➞ [None]
Notes
•	None has the special "NoneType" all for itself.

"""


def Emptying(a):
    i = 0
    while(i < len(a)):
        if(isinstance(a[i], bool)):
            a[i] = False
        elif(isinstance(a[i], int)):
            a[i] = 0
        elif(isinstance(a[i], float)):
            a[i] = 0.0
        elif(isinstance(a[i], str)):
            a[i] = ''
        elif(isinstance(a[i], list)):
            a[i] = []
        elif(isinstance(a[i], tuple)):
            a[i] = ()
        elif(isinstance(a[i], set)):
            a[i] = set()
        elif(a[i] is None):
            a[i] = None
        i = i + 1

    return a


# print(Emptying([True, False]))
