"""Write a function which receives 4 digits and returns the latest time of day that can be built with those digits.

The time should be in HH:MM format.

Examples:

digits: 1, 9, 8, 3 => result: "19:38"
digits: 9, 1, 2, 5 => result: "21:59"
Notes
Result should be a valid 24-hour time, between 00:00 and 23:59.
Every input has a valid answer.
"""

from itertools import permutations

def latest_clock(a, b, c, d):
    digits = [a, b, c, d]
    max_time = -1

    for perm in permutations(digits):
        hours = perm[0] * 10 + perm[1]
        minutes = perm[2] * 10 + perm[3]

        if 0 <= hours <= 23 and 0 <= minutes <= 59:
            current_time = hours * 60 + minutes
            max_time = max(max_time, current_time)

    if max_time == -1:
        return "Invalid input"
    
    return f"{max_time // 60:02d}:{max_time % 60:02d}"

print(latest_clock(1, 9, 8, 3))
print(latest_clock(9, 1, 2, 5))
print(latest_clock(1, 2, 8, 9))