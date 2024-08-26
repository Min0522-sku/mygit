import sys
input = sys.stdin.readline

N = int(input())
L = []
ans = [1]* N
for _ in range(N):
    a, b = map(int, input().split())
    L.append([a, b])

for i in range(N):
    for j in range(N):
        if i != j:
            if L[i][0] < L[j][0] and L[i][1] < L[j][1]:
                ans[i] += 1
print(" ".join(map(str, ans)))