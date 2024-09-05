import sys
input = sys.stdin.readline
ans = 0
N = int(input())
result = [[0]*3 for _ in range(N)]
colorcost = []
for _ in range(N):
    colorcost.append(list(map(int, input().split())))

result[0][0] = colorcost[0][0]
result[0][1] = colorcost[0][1]
result[0][2] = colorcost[0][2]

for i in range(1, N):
    result[i][0] = colorcost[i][0] + min(result[i-1][1], result[i-1][2])
    result[i][1] = colorcost[i][1] + min(result[i-1][0], result[i-1][2])
    result[i][2] = colorcost[i][2] + min(result[i-1][0], result[i-1][1])

print(min(result[N-1][0], result[N-1][1], result[N-1][2]))