# выполнение арифметических операций с условием приоритетности при чтении из файла


def priorityOpeations(n):                  # функция, выполняющая приоритетные операции
    n = n.split(' ')
    a = []
    c = []

    for i in range(0, len(n)):             # создаем лист, где цифры - целые числа, а операторы строки
        if i % 2 == 0:
            a.append(int(float(n[i])))     # переводим в целое число число с плавающей точкой, которое могло получиться в результате деления
        else:
            a.append(n[i])

    i = 0
    while i != len(a) - 1:                 # заходим в цикл
        if a[i + 1] == '=':                # если после последнего числа соит =, в список добавляем число и знак =
            c.append(a[i])
            c.append(a[i + 1])
            break

        if a[i + 1] == '+' or a[i + 1] == '-':  # если после числа стоит + или - , добавляем число и оператор за ним
            c.append(int(a[i]))
            c.append(a[i + 1])
            i = i + 2
            continue

        if a[i + 1] == '*':
            num = int(a[i]) * int(a[i + 2])     # если после числа стоит оператор *, перемножаем соседние числа и добавляем следующий оператор
            c.append(num)
            c.append(a[i + 3])
            i = i + 4
            continue

        if a[i + 1] == '/':
            num = int(a[i]) / int(a[i + 2])     # если после числа стоит оператор /, делим соседние числа и добавляем следующий оператор
            c.append(num)
            c.append(a[i + 3])
            i = i + 4
            continue

        if a[i + 1] == '%':
            num = int(a[i]) % int(a[i + 2])     # если после числа стоит оператор %, делим с остатком соседние числа и добавляем следующий оператор
            c.append(num)
            c.append(a[i + 3])
            i = i + 4

    c.append(a[-1])                             # в готовый лист добавляем последний элемент

    return (c)

f = open('test.txt', 'w+')                     # создаем файл и записываем в него информацию
f.write('1 * 5 * 8 - 3 / 1 + 6 % 2 = 40')
f.close()

f = open('test.txt', 'r')
b = []
n = f.read()                           # n = '1 * 5 * 8 - 3 / 1 + 6 % 2 = 40'
num = 0
b = priorityOpeations(n)               # к введенной строке применяем функцию
print(b)

if '*' in b or '/' in b or '%' in b:  # проверем условие, все ли приоритетные операции выполнены. если нет, то вызываем функцию снова
    n = ' '.join(map(str, b))         # преобразование листа после обработки функцией в строку для возможности нового старта функции
print(n)
b = priorityOpeations(n)
print(b)

num = b[0]
for i in range(1,len(b)-1,2):         # после того, как приоритетные операции выполнены, работаем с + и -
    if b[i] == '+':
        num += b[i+1]
    if b[i] == '-':
        num -= b[i+1]
print(num)

if num == b[-1]:
    print('True')
else:
    print('False')

f.close()                            # закрываем файл




