"""A palindrome is a series of characters that read the same forwards as backwards such as "hannah", "racecar" and "lol".

For this Kata you need to write a function that takes a string of characters and returns the length, as an integer value, of longest alphanumeric palindrome that could be made by combining the characters in any order but using each character only once. The function should not be case sensitive.

For example if passed "Hannah" it should return 6 and if passed "aabbcc_yYx_" it should return 9 because one possible palindrome would be "abcyxycba".

"""

def longest_palindrome(st):
    st = st.lower()
    
    s = ""
    for char in st:
        if char.isalnum():
            s += char
    
    char_count = {}
    
    for i in s:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    
    length = 0
    odd_count = 0
    
    for count in char_count.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            odd_count = 1
    
    return length + odd_count
        
# print(longest_palindrome("Hannah"))
# print(longest_palindrome("xyz__a_/b0110//a_zyx"))
print(longest_palindrome("$aaabbbccddd_!jJpqlQx_.///yYabababhii_"))

