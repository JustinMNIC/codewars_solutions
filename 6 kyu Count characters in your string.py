"""The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}."""

def count(s):
    dictt = {}
    for i in s:
        if i in dictt:
            dictt[i] += 1
        else:
            dictt[i] = 1
    return dictt