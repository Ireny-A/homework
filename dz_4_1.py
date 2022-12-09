# находим макс. расстояние между двумя локальными максимумами

if __name__ == '__main__':
    num = int(input())
    preNum = int(input())
    postNum = int(input())
    a = 0
    n = 1
    m = 0
    s = 0
    while postNum != 0:
        n = n + 1
        if num > preNum and num > postNum:
            s = n - a - 1
            a = n
            m = s
        preNum = num
        num = postNum
        postNum = int(input())
        s = max(s,m)
    print(s)

# или

    preNumber = int(input())
    number = int(input())
    postNumber = int(input())

    count = 0
    total = 0

    while postNumber != 0:
        if number > postNumber and number > preNumber:
           while number >= postNumber != 0:
               count += 1
               preNumber = number
               number = postNumber
               postNumber = int(input())
               if total <= count:
                  total = count
        count = 0
        preNumber = number
        number = postNumber
        if postNumber == 0:
            break
        postNumber = int(input())

    print(total)

# или(вариант Кирилла)


preNumber = int(input())
number = int(input())
postNumber = int(input())

count = 0
maxCount = 0


while postNumber != 0:
    if postNumber < number > preNumber:
        if maxCount == 0:
            maxCount = 1
        elif maxCount < count:
            maxCount = count
        count = 1
    count = count + 1
    preNumber = number
    number = postNumber
    postNumber = int(input())


print(maxCount-2)