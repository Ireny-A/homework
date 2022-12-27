# функция возвращает самое длинное слово из строки

def maxWord(a):
  maxW = 0
  a = a.split()

  for i in range(len(a)-1):
    if len(a[i]) > len(a[i+1]):
      maxW = a[i]
  print(maxW)


a = input()
maxWord(a)





