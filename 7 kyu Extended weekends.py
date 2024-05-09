"""If the first day of the month is a Friday, it is likely that the month will have an Extended Weekend. That is, it could have five Fridays, five Saturdays and five Sundays.

In this Kata, you will be given a start year and an end year. Your task will be to find months that have extended weekends and return:

- The first and last month in the range that has an extended weekend
- The number of months that have extended weekends in the range, inclusive of start year and end year.
For example:

solve(2016,2020) = ("Jan","May",5). #The months are: Jan 2016, Jul 2016, Dec 2017, Mar 2019, May 2020
More examples in test cases. Good luck!

If you found this Kata easy, please try myjinxin2015 challenge version here
"""

def solve(a, b):
    from datetime import datetime
    from calendar import monthrange
    from collections import defaultdict
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    d = defaultdict(list)
    for year in range(a, b+1):
        for month in range(1, 13):
            if datetime(year, month, 1).weekday() == 4 and monthrange(year, month)[1] == 31:
                d[year].append(months[month-1])
    return (d[min(d.keys())][0], d[max(d.keys())][-1], len([month for months in d.values() for month in months]))