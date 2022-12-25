# вывести элементы массива, которые встречаются только один раз

n = int(input())
a = []


for i in range(n):
    a.append(int(input()))

print(str(a).strip('[]'))

for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i],end=' ')





