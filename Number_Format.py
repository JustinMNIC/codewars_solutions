"""Format any integer provided into a string with "," (commas) in the correct places.

Example:

For n = 100000 the function should return '100,000';
For n = 5678545 the function should return '5,678,545';
for n = -420902 the function should return '-420,902'.
"""

def number_format(n):
    result = ""
    count = 0
    negative = False
    for i in str(n)[::-1]:
        if i == "-":
            negative = True
        else:
            count += 1
            if count // 3 == 1:
                count = 0
                result = result + i + ","
            else: 
                result = result + i
    if result[-1] == ",":
        result = result[0:-1]
    return result[::-1] if negative == False else "-" + result[::-1]
    
print(number_format(5678545))
print(number_format(100000))