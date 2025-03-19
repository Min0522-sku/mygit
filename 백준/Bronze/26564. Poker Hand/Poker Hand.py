from collections import Counter
N = int(input().strip())
for i in range(N):
    l = list(input().split())
    r = [c[0] for c in l]
    print(max(Counter(r).values()))