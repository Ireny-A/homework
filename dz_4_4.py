#  Для каждого натурального числа в промежутке от M до N вывести все делители, кроме единицы и самого числа (range)

m = int(input())
n = int(input())

for i in range (m,n+1):
    for e in range(2,i):
        if i % e == 0:
            print(i,':',e)

#  Для каждого натурального числа в промежутке от M до N вывести все делители, кроме единицы и самого числа (while)

m = int(input())
n = int(input())
a = 1
while m <= n :
    a = a + 1
    if a == m:
        a = 2
        m = m + 1
    if m % a == 0:
        print(m,':',a)









