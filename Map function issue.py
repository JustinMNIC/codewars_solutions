"""In computer science, a programming language is said to have first-class functions if it treats functions as first-class citizens. Specifically, this means the language supports passing functions as arguments to other functions, returning them as the values from other functions, and assigning them to variables or storing them in data structures.

First-class functions are a necessity for the functional programming style, in which the use of higher-order functions is a standard practice. A simple example of a higher-ordered function is the map function, which takes, as its arguments, a function and a list, and returns the list formed by applying the function to each member of the list. For a language to support map, it must support passing a function as an argument. See more on https://en.wikipedia.org/wiki/First-class_function

Your task is to rewrite your own map function which takes :

an array
a predicate function func which returns true (boolean) with even arguments
For example :

map([1,2,3,4],func)

produces

[ false, true, false, true ]  
The code also has to perform input validation, return :

'given argument is not a function' if func is not a function
'array should contain only numbers' if any elements are not numbers"""

def func(n):
    return n % 2 == 0

def map(arr, func):
    if not callable(func):
        return 'given argument is not a function'
    answer = []
    for element in arr:
        try:
            answer.append(func(int(element)))
        except:
            return "array should contain only numbers"
    return answer
    
print(map([1,2,3,'8'],func))



# PS:
"""Random Tests
Testing for [-3, 5, 4, -1, 1]
It should work for random inputs too: [False, False, True, False, False] should equal ['given argument is not a function', 'given argument is not a function', 'given argument is not a function', 'given argument is not a function', 'given argument is not a function']
Completed in 0.05ms
Testing for [4, 0]
It should work for random inputs too: [True, True] should equal ['given argument is not a function', 'given argument is not a function']
Completed in 0.03ms
Testing for [-2, -5, -1, -4]
It should work for random inputs too: [True, False, False, True] should equal ['given argument is not a function', 'given argument is not a function', 'given argument is not a function', 'given argument is not a function']
Completed in 0.04ms
Testing for [-1, -1]
It should work for random inputs too: [False, False] should equal ['given argument is not a function', 'given argument is not a function']
Completed in 0.03ms
Testing for [-3, 5, 2, 'a', 6, -3]
It should work for random inputs too: 'given argument is not a function' should equal 'array should contain only numbers'"""