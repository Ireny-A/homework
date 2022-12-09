# найти количество положительных элементов в массиве

a = []
n = int(input())
rez = 0
for i in range(n):
    a.append(int(input()))
print(*a)
for i in range(n):
    if a[i] >= 0:
        rez = rez + 1
print(rez)