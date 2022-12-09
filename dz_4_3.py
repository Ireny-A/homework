# вывводим кубы чисел из диапазона используя range

a = int(input())
b = int(input())

for i in range(a,b+1):
    print(i**3)

# вывводим кубы чисел из диапазона используя while

a = int(input())
b = int(input())

while a <= b:
    print(a**3)
    a = a + 1