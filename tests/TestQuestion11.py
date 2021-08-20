"""
. Is the Number a Repdigit
A repdigit is a positive number composed out of the same digit.
Create a function that takes an integer and returns whether it's a repdigit or not.
Examples
is_repdigit(66) ➞ True

is_repdigit(0) ➞ True

is_repdigit(-11) ➞ False
Notes
•	The number 0 should return True (even though it's not a positive number).

"""

def is_repdigit(a):
    res = True
    if a >= 0:
        ost = a
        lst_num = []
        for i in range(0, len(str(a))):
            lst_num.append(ost % 10)
            ost = a // 10
            if i > 0:
                if lst_num[i] == lst_num[i - 1]:
                    res = True
                elif lst_num[i] != lst_num[i - 1] :
                    res = False
                    break
            else:
                res = True
    else:
        res = False
    return res

#print(is_repdigit(666))