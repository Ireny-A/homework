# определть, является ли строка палиндромом (функция)

def palindrome(a):

    b =''.join(reversed(a))
    if a == b:
        print('Palindrome')
    else:
        print('Not a palindrome')

a = input()
palindrome(a)

# или

def palindrome1(a):

    if str(a) == str(a[::-1]):
        print('Palindrome')
    else:
        print('Not a palindrome')

a = input()
palindrome1(a)