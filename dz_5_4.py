# вывести все элементы массива, которые больше предыдущего

a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
print(*a)
for i in range(0,n):
    if a[i-1] < a[i]:
        print(a[i],end='\t')