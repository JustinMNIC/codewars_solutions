"""Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
Go challenge Build Tower Advanced once you have finished this :)"""


def tower_builder(n_floors):
    count, lis = 1, []
    for f in reversed(range(n_floors)):
        lis.append(" " * f + "*" * count + " " * f)
        count += 2
    return lis

print(tower_builder(3))