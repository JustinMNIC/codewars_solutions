"""The task is simply stated. Given an integer n (3 < n < 109), find the length of the smallest list of perfect squares which add up to n. Come up with the best algorithm you can; you'll need it!

Examples:

sum_of_squares(17) = 2
17 = 16 + 1 (16 and 1 are perfect squares).
sum_of_squares(15) = 4
15 = 9 + 4 + 1 + 1. There is no way to represent 15 as the sum of three perfect squares.
sum_of_squares(16) = 1
16 itself is a perfect square.
Time constraints:

5 easy (sample) test cases: n < 20

5 harder test cases: 1000 < n < 15000

5 maximally hard test cases: 5e8 < n < 1e9

15 random maximally hard test cases: 1e8 < n < 1e9"""

# actually the number can be much higher than 109
# KEY = Lagrange's Four Square Theorem

def is_perfect_square(num):
    root = int(num ** 0.5)
    return root * root == num

def sum_of_squares(n):
    if is_perfect_square(n):
        return 1
    while n % 4 == 0:
        n /= 4
    if n % 8 == 7:
        return 4
    for i in range(1, int(n**0.5) + 1):
        if is_perfect_square(n - i*i):
            return 2
    return 3

print(sum_of_squares(18)) 
print(sum_of_squares(19))