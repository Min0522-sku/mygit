from collections import defaultdict
import sys
input = sys.stdin.readline
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    l = defaultdict(int)
    for i in range(N):
        a = int(input())
        l[a] += 1
    for i in range(M):
        b = int(input())
        l[b] += 1
    l = list(l.values())
    print(l.count(2))