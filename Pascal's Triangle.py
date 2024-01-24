"""In mathematics, Pascal's triangle is a triangular array of the binomial coefficients expressed with formula

(
�
�
)
=
�
!
�
!
(
�
−
�
)
!
( 
k
n
​
 )= 
k!(n−k)!
n!
​
 
where n denotes a row of the triangle, and k is a position of a term in the row.

Pascal's Triangle

You can read Wikipedia article on Pascal's Triangle for more information.

Task
Write a function that, given a depth n, returns n top rows of Pascal's Triangle flattened into a one-dimensional list/array.

Example:
n = 1: [1]
n = 2: [1,  1, 1]
n = 4: [1,  1, 1,  1, 2, 1,  1, 3, 3, 1]


<link> https://www.codewars.com/kata/5226eb40316b56c8d500030f/train/python <\link>"""

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def apply_formula(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def pascals_triangle(n):
    return [apply_formula(N, k) for N in range(n) for k in range(N + 1)]


print(pascals_triangle(3))


            