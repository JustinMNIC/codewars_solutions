"""ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating."""

def rot13(message):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alpha = alphabet.lower()
    answer = []
    
    for char in message:
        if char.isalpha():
            if char.islower():
                answer.append(lower_alpha[(lower_alpha.index(char) + 13) % 26])
            else:
                answer.append(alphabet[(alphabet.index(char) + 13) % 26])
        else:
            answer.append(char)

    return "".join(answer)