# посчитать, сколько пар элементов в списке

a = []
b = []
c = []
rez = []
n = int(input())
for i in range(n):
    a.append(int(input()))
print(*a)

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(*a)

for i in range(0,n-1,2):
    if a[i] == a[i+1]:
        b.append(a[i])
for i in range(1, n-1, 2):
    if a[i] == a[i + 1]:
        c.append(a[i])

rez = len(b+c)
print(rez)

# посчитать, сколько пар элементов в списке (вариант 2)

a = []
count = 0
n = int(input())
for i in range(n):
    a.append(int(input()))
print(*a)

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(*a)

for i in range(0,n-1):
    if a[i] == a[i+1]:
        i = i + 2
        count = count + 1

print(count)