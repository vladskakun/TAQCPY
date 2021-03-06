"""
A Circle and Two Squares
Imagine a circle and two squares: a smaller and a bigger one. For the smaller one, the circle is a circumcircle and for the bigger one, an incircle.
 
Create a function, that takes an integer (radius of the circle) and returns the square area of the square inside the circle.
Examples
square_areas_difference(5) ➞ 50

square_areas_difference(6) ➞ 72

square_areas_difference(7) ➞ 98
Notes
Use only positive integer parameters.

"""


def square_areas_difference(r):
    return 2 * r * r

#print(square_areas_difference(6))