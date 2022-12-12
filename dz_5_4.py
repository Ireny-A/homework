# вывести все элементы массива, которые больше предыдущего

a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
print(*a)
for i in range(0,n-1):
    if a[i] < a[i+1]:
        print(a[i+1],end='\t')