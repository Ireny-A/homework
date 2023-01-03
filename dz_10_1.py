# заменить все числовые значения в args на строки с такими же значениями

def digitStr(*args):
    b = []
    for i in args:
        if isinstance(i,int):
            i = str(i)
            b.append(i)
        else:
            b.append(i)
    return b

print(digitStr(1,'2',4,7))