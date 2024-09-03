T = int(input())
ans = []
for _ in range(T):
    n = int(input())
    L = {}
    for _ in range(n):
        a, b = map(str, input().split())
        if b in L:
            L[b] += 1
        else:
            L[b] = 1
    total = 1
    for i in L.values():
        total *= (i+1)
    ans.append(total-1)

for i in ans:
    print(i)
