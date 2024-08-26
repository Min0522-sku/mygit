import sys
input = sys.stdin.readline

N = int(input())
L = []
for _ in range(N):
    x, y = map(int, input().split())
    L.append([x, y])
L.sort(key= lambda xy: (xy[0], xy[1]))
for x,y in L:
    print(f"{x} {y}")