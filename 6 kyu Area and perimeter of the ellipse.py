"""Task:
Based on the received dimensions, a and b, of an ellipse, calculare its area and perimeter.

Example:
Input: ellipse(5,2)

Output: "Area: 31.4, perimeter: 23.1"
Note: The perimeter approximation formula you should use: π * (3/2(a+b) - sqrt(ab))"""

import math

def ellipse(a, b):
    area = round(math.pi * a * b, 1)
    perimeter = round(math.pi * (3/2 * (a+b) - math.sqrt(a*b)), 1)
    return f"Area: {area}, perimeter: {perimeter}"