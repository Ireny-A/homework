# найти количество слов в строке

a = input()
count = 1
for i in a:
    if i == ' ':
        count = count + 1

print(count)

