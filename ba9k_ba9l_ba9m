""" General functions """

def bwt(arr):
    permutations = sorted([f"{arr[i:len(arr)]}{arr[0:i]}" for i in range(len(arr))])
    lcol = ''.join(list(map(lambda x: x[-1], permutations)))
    ind = permutations.index(arr)
    return ind, lcol


def bw_restore(I, L, key='string'):
    n = len(L)
    X = sorted(list(enumerate(L)), key=lambda x: x[1])

    T = [None for i in range(n)]
    for i, y in enumerate(X):
        T[y[0]] = i

    Tx = [I]
    for i in range(1, n):
        Tx.append(T[Tx[i-1]])

    S = list(map(lambda x: L[x], Tx))
    S.reverse()

    if key == 'pos':
        return T
    else:
        return ''.join(S)


arr = 'abracadabra'
LastToFirst = 'T$GACCA'


'''BA9K'''


def lastToFirst(i, Transform):
    return bw_restore(i, Transform, key='pos')[i]


with open(str(input()), 'r') as handle:
    handle = list(handle.readlines())
    Transform, i = handle[0].rstrip('\n'), int(handle[1].rstrip('\n'))

print(lastToFirst(i, Transform))


""" BA9L """

import re

def bwmatchlist(LastColumn, Patterns):
    matchlist = []

    def bwmatching(LastColumn, Pattern):
        top, bottom = 0, len(LastColumn) - 1
        while top <= bottom:
            if len(Pattern) > 0:
                symbol, Pattern = Pattern[-1], Pattern[:-1]
                if LastColumn[top:bottom+1].count(symbol) > 0:
                    subIndices = list(map(lambda x: x.start(), re.finditer(symbol, LastColumn)))
                    subIndices = [x for x in subIndices if x in range(top, bottom + 1)]
                    topIndex, bottomIndex = subIndices[0], subIndices[-1]
                    top, bottom = lastToFirst(topIndex, LastColumn), lastToFirst(bottomIndex, LastColumn)
                else:
                    return 0
            else:
                return bottom - top + 1

    for Pattern in Patterns:
        matchlist.append(bwmatching(LastColumn, Pattern))

    return ' '.join(list(map(str, matchlist)))

with open(str(input()), 'r') as handle:
    handle = list(handle.readlines())
    Bwt, Patterns = handle[0].rstrip('\n'), handle[1].rstrip('\n').split(' ')

print(bwmatchlist(Bwt, Patterns))


"""BA9M"""


def Count(symbol, i, LastColumn):
    return LastColumn[:i].count(symbol)


def firstOccurrence(symbol, LastColumn):
    FirstColumn = ''.join(sorted(LastColumn))
    occurrence = FirstColumn.find(symbol)
    return occurrence


def betterbwmatching(LastColumn, Pattern):
    top, bottom = 0, len(LastColumn) - 1
    while top <= bottom:
        if len(Pattern) > 0:
            symbol, Pattern = Pattern[-1], Pattern[:-1]
            if LastColumn[top:bottom + 1].count(symbol) > 0:
                fo = firstOccurrence(symbol, LastColumn)
                top = fo + Count(symbol, top, LastColumn)
                bottom = fo + Count(symbol, bottom + 1, LastColumn) - 1
            else:
                return 0
        else:
            return bottom - top + 1

with open('/home/reverend_casy/WPGMA_Malovichko/rosalind_ba9m.txt', 'r') as handle:
    handle = list(handle.readlines())
    Bwt, Patterns = handle[0].rstrip('\n'), handle[1].rstrip('\n').split(' ')

print(' '.join(list(map(lambda x: str(betterbwmatching(Bwt, x)), Patterns))))

