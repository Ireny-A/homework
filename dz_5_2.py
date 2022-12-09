# вывести все четные элементы массива

a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
print(*a)
for i in range(0,n):
    if a[i]%2 == 0:
        print(a[i],end='\t')
