# Написать функцию которая принимает непозиционные элементы и выводит элемент с самым длинным ключом

def longKey(**kwargs):
    a = 0
    maxLen = ''
    for key, value in kwargs.items():
        if len(key) > len(maxLen):
            maxLen = key
            a = value
    print(a)

longKey(Egor = 12, Vasya = 32, Sergey = 40)
