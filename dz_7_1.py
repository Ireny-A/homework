a = {'Pencil':[30,5],'Pen':[10,3],'Pencil box':[40,1],'Copybook':[20,6],'Eraser':[3,2],'Ruler':[5,2]}
maxPeace = 0
totaiWeight = 0
maxWaight = 0
minWaight = 2**31
b = []
count = 0

# вычисляем общий вес

for i in a.values():
    totaiWeight = totaiWeight + i[0]*i[1]
print(totaiWeight)

# находим вещь, количество штук которой больше всего

for i in a.values():
    if i[1] > maxPeace:
        maxPeace = i[1]
print(maxPeace)

for key, value in a.items():
    if maxPeace in value:
        print(key)

# находим самую тяжелую вещь в рюкзаке

for i in a.values():
    if i[0] > maxWaight:
        maxWaight = i[0]
print(maxWaight)

for key, value in a.items():
    if maxWaight in value:
        print(key)

# находим вещь, все экземпляры которой весят меньше всего

for i in a.items():
    for j in a.values():
        if minWaight > j[0] * j[1]:
            minWaight = j[0] * j[1]
            b = j
print(b)

for key, value in a.items():
    if value == b:
        print(key)








