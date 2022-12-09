# вывести все элементы массива с четными индексами

a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
print(*a)
for i in range(0,n,2):
    print(a[i],end='\t')


