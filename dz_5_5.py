# вывести два соседних элемента одного знака

a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
print(*a)
for i in range(0,n-1):
    if a[i] * a[i+1] > 0:
        print(a[i],a[i+1],end='\t')
        break