# написать сортировку непозиционных по ключу
# если ключ имеет тип int

def sortDict(kwargs):
    sortedKwargs = {}
    sortedKwargs = dict(sorted(kwargs.items()))
    print(sortedKwargs)

sortDict({2:'a',5:'f',1:'g'})

# если ключ типа str

def sortDict(**kwargs):
    sortedKwargs = {}
    sortedKwargs = dict(sorted(kwargs.items()))
    print(sortedKwargs)

sortDict(d='a',b=1,k='f',a='g')