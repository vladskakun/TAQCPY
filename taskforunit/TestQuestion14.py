"""
14. Sum Fractions
Create a function that takes a list containing nested lists as an argument. Each sublist has 2 elements. The first element is the numerator and the second element is the denominator. Return the sum of the fractions rounded to the nearest whole number.
Examples
sum_fractions([[18, 13], [4, 5]]) ➞ 2

sum_fractions([[36, 4], [22, 60]]) ➞ 9

sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]) ➞ 11
Notes
Your result should be a number not string.

"""

def sum_fractions(a):
    i = 0
    j = 0
    rez = 0
    while(i < len(a)):
        sum=a[i][j] / a[i][j+1]
        rez += sum
        i = i + 1
    rez = round(rez)
    return rez


#print(sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]))