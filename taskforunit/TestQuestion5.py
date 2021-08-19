"""
List of Multiples
Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num up to length.
Examples
list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]

list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]
Notes
Notice that num is also included in the returned list.

"""

def list_of_multiples(number,length):
    list = []
    sum = 0
    i = 0
    while(i < length):
        sum = sum + number
        list.append(sum)
        i = i + 1
    return list


#print(list_of_multiples(7,5))