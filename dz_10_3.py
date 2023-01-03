# Написать сортировку позиционных элементов

def sortTurple(*args):
    a = []
    for i in args:
        a.append(i)
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                a[i],a[j] = a[j],a[i]

    print(a)

sortTurple(9,1,5,4,2)

