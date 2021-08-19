"""
19. Oddish vs. Evenish
Create a function that determines whether a number is Oddish or Evenish. A number is Oddish if the sum of all of its digits is odd, and a number is Evenish if the sum of all of its digits is even. If a number is Oddish, return "Oddish". Otherwise, return "Evenish".
For example, oddish_or_evenish(121) should return "Evenish", since 1 + 2 + 1 = 4. oddish_or_evenish(41) should return "Oddish", since 4 + 1 = 5.
Examples
oddish_or_evenish(43) ➞ "Oddish"

oddish_or_evenish(373) ➞ "Oddish"

oddish_or_evenish(4433) ➞ "Evenish"

"""


def oddish_or_evenish(num_num):
    numbers_of_num = []
    for i in range(0, len(str(num_num))):
        numbers_of_num.append(num_num % 10)
        num_num=num_num // 10
    summ = 0
    for number in numbers_of_num:
        summ = summ + number
    if summ % 2 == 0:
        return 'Evenish'
    else:
        return 'Oddish'