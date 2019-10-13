# Check whether a string is a Palindrome or not

s = "A nut for a jar of tuna"


def IsPalindrome(string):
    if ''.join(string.lower().split()) == ''.join(string[::-1].lower().split()):
        return f'{string }, is a palindrome'
    else:
        return f'{string }, is not a palindrome'

print(IsPalindrome(s))