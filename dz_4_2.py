# вывод факториала при помощи range

a = 1
n = int(input())
f = 1
for i in range(1,n + 1):
        f *= i
print(f)

# вывод факториала при помощи while

n = int(input())
f = 1

while n > 1:
        f *= n
        n = n - 1
print(f)
