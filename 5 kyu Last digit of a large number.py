"""Define a function that takes in two non-negative integers 
�
a and 
�
b and returns the last decimal digit of 
�
�
a 
b
 . Note that 
�
a and 
�
b may be very large!

For example, the last decimal digit of 
9
7
9 
7
  is 
9
9, since 
9
7
=
4782969
9 
7
 =4782969. The last decimal digit of 
(
2
200
)
2
300
(2 
200
 ) 
2 
300
 
 , which has over 
1
0
92
10 
92
  decimal digits, is 
6
6. Also, please take 
0
0
0 
0
  to be 
1
1.

You may assume that the input will always be valid.

Examples
last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
Remarks
C++, R, PureScript, COBOL"""

def last_digit(a, b):
    if b == 0:
        return 1
    return pow(a, b, 10)
