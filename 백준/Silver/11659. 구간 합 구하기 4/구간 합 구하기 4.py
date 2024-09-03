import sys
input = sys.stdin.readline
N, M = map(int, input().split())
L = list(map(int, input().split()))
ans = []
sum = [0] * N
sum[0] = L[0]
for i in range(1, N):
    sum[i] = sum[i-1] +L[i]

for _ in range(M):
    a, b = map(int, input().split())

    if a == 1:
        ans.append(sum[b-1])
    else:
        ans.append(sum[b-1]-sum[a-2])
    
for i in ans:
    print(i)
