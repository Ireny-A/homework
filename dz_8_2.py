# определить, есть ли среди 8-ми ферзей пара бьющих друг друга

n = 8
x = []
y = []

for i in range(n):
    x.append(int(input()))
    y.append(int(input()))
print(x,y)

finita = False

for i in range(n):
    for j in range(i+1,n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i]-x[j]) == abs(y[i]-y[j]):
            finita = True
            break

if finita == True:
    print('YES')
else:
    print('NO')
