"""This is a hard version of How many are smaller than me?. If you have troubles solving this one, have a look at the easier kata first.

Write

function smaller(arr)
that given an array arr, you have to return the amount of numbers that are smaller than arr[i] to the right.

For example:

smaller([5, 4, 3, 2, 1]) === [4, 3, 2, 1, 0]
smaller([1, 2, 0]) === [1, 1, 0]
Note
Your solution will be tested against inputs with up to 120_000 elements."""

import bisect

def smaller(nums):
    sorted_nums = []
    result = []
    for num in reversed(nums):
        idx = bisect.bisect_left(sorted_nums, num)
        result.append(idx)
        sorted_nums[idx:idx] = [num]
    return result[::-1]

import random

test = [random.randint(0, 1000) for _ in range(120000)]


import time
start = time.time()
smaller(test)
print(time.time() - start)