import itertools
n, m = map(int, input().split())
nlist = list(map(int, input().split()))
combin = itertools.combinations(nlist, 3)
combinmax = 0
for i in combin:
    isum = sum(i)
    if isum == m:
        combinmax = isum
        break
    elif isum > combinmax and m > isum:
        combinmax = isum
print(combinmax)