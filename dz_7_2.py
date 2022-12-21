# Имеем словарь книг, найти автора, у которого больше всего книг

a = {'Viy':'Gogol','Kapitanskaya dochka':'Pushkin','Master i Margarita':'Bulgakov','Shinel':'Gogol',
     'Dubrovsky':'Pushkin','Nos':'Gogol','Pikovaya dama':'Pushkin','Morfiy':'Bulgakov','Metel':'Pushkin'}
b = {}
c = {}
count = 0
maxx = 0

# создаем словарь авторов без дубликатов

b = set(a.values())

# считаем количество произведений каждого автора и добавляем в новый словарь

for key in b:
     count = 0
     for value in a.items():
          if key == value[1]:
               count = count + 1
     c.update({key:count})

# находим максимальное количество произведений

for i in c.items():
     if i[1] > maxx:
          maxx = i[1]

# ищем автора по максимальному количеству произведений, выводи автора и количество произведений

for key, value in c.items():
    if value == maxx:
        print(key,value)







