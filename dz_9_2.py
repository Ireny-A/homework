# вывести элементы массива, которые встречаются только один раз (функция)

def nonRepeat(a):

    for i in range(n):
        a.append(int(input()))

    for i in range(len(a)):
        for j in range(len(a)):
            if i != j and a[i] == a[j]:
                break
        else:
            print(a[i],end=' ')

n = int(input())
a = []
nonRepeat(a)