# выполнение арифметических операций с условием приоритетности при чтении из файла (вариант 2)

def rezNonPriority(a):                    # функция для работы только с неприоритетными операциями (выводит результат вычислений)
    c = a.split(' ')
    num = int(float(c[0]))

    for i in range(1, len(c) - 1, 2):
        if c[i] == '+':
            num += int(float(c[i + 1]))
        if c[i] == '-':
            num -= int(float(c[i + 1]))

    return str(num)


def priorityOperations(n):                 # функция выполняет приоритетные операции
    a = []
    num = 0
    n = n.split(' ')

    i = 0
    while i != len(n) -1:                 # создаем лист после выполнения вычислений

        if n[i+1] == '=':
            a.append(n[i])
            a.append(n[i+1])
            break

        if n[i+1] == '+' or n[i+1] == '-':
            a.append(n[i])
            a.append(n[i+1])
            i = i + 2
            continue

        if n[i+1] == '*':
            num = int(n[i]) * int(n[i + 2])
            a.append(str(num))
            a.append(n[i + 3])
            i = i + 4
            continue

        if n[i+1] == '/':
            num = int(n[i]) / int(n[i + 2])
            a.append(str(num))
            a.append(n[i + 3])
            i = i + 4
            continue

        if n[i+1] == '%':
            num = int(n[i]) % int(n[i + 2])
            a.append(str(num))
            a.append(n[i + 3])
            i = i + 4

    a.append(n[-1])

    if '*' in a or '/' in a or '%' in a:          # проверяем лист на наличие приоритетных операций
        n = ' '.join(map(str, a))                 # переводим лист в строку для дальнейшей работы с ним
        return priorityOperations(n)              # если приоритеты встречаются, снова вызываем функцию
    else:
        a = ' '.join(map(str, a))
        return rezNonPriority(a)                  # если нет, то вызываем функцию для работы со сложением и вычитанием и сохраняем результат


f = open('test.txt', 'w+')                        # создаем текстовый файл и записываем в него информацию
f.write('1 * 5 * 8 - 3 / 1 + 6 % 2 = 40')
f.close()

f = open('test.txt', 'r')
n = f.read()

if priorityOperations(n) == n[-1]:                # используя функцию сверяем результат вычисления с тем, что занесено в файл
    print('True')
else:
    print('False')

f.close()

