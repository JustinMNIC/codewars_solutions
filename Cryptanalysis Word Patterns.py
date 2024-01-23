"""In cryptanalysis, words patterns can be a useful tool in cracking simple ciphers.

A word pattern is a description of the patterns of letters occurring in a word, where each letter is given an integer code in order of appearance. So the first letter is given the code 0, and second is then assigned 1 if it is different to the first letter or 0 otherwise, and so on.

As an example, the word "hello" would become "0.1.2.2.3". For this task case-sensitivity is ignored, so "hello", "helLo" and "heLlo" will all return the same word pattern.

Your task is to return the word pattern for a given word. All words provided will be non-empty strings of alphabetic characters only, i.e. matching the regex "[a-zA-Z]+".
"""

def word_pattern(word):
    dictt = {}
    index = 0
    response = ""
    for letter in word.lower():
        if letter not in dictt.keys():
            dictt[letter] = str(index)
            index += 1
    for L in word.lower():
        response += dictt.get(L) + "."
    response = response[:-1]
    return response
        
print(word_pattern("Hippopotomonstrosesquippedaliophobia"))