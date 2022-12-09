# выводим на экран двумерную таблицу умножения

for i in range (1,10):
    print(list(range(i,((i*9)+1),i)))


# или

for i in range(1, 11):
    for a in range(1, 11):
        print((i*a), end="\t")