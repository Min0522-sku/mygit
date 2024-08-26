import sys
input = sys.stdin.readline

N = int(input())
L = []
for _ in range(N):
    x, y = map(int, input().split())
    L.append([x, y])
L.sort(key= lambda xy: (xy[1], xy[0]))
for x,y in L:
    print(f"{x} {y}")