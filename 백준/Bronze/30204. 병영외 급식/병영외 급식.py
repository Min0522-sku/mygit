N, X = map(int, input().split())
L = list(map(int, input().split()))
if (sum(L)%X) == 0:
    print(1)
else:
    print(0)