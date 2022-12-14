# перевести символ в верхний регистр (функции)

a = input()

if a.isupper():
    print(a)
else:
    print(a.upper())

# с юникодом

a = input()

if 97 <= ord(a) <= 122:
    print(chr(ord(a)-32))
else:
    print(a)

