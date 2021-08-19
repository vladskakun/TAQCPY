"""
24. Buggy Uppercase Counting
In the Code tab is a function which is meant to return how many uppercase letters there are in a list of various words. Fix the list comprehension so that the code functions normally!
Examples
count_uppercase(['SOLO', 'hello', 'Tea', 'wHat']) ➞ 6

count_uppercase(['little', 'lower', 'down']) ➞ 0

count_uppercase(['EDAbit', 'Educate', 'Coding']) ➞ 5

"""


def count_uppercase(data_list):
    i = 0
    rez = 0
    while(i < len(data_list)):
        j = 0
        while(j < len(data_list[i])):
            if data_list[i][j].isupper():                
                rez += 1
            j += 1
        i += 1
    return rez


print(count_uppercase(['EDAbit', 'Educate', 'Coding']))

