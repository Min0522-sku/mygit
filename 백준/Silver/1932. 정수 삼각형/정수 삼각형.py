N = int(input())
T = []

for _ in range(N):
    a = list(map(int, input().split()))
    T.append(a)

dp = [[0]*len(T[i]) for i in range(N)]

dp[-1] = T[-1]
for j in range(N-2, -1, -1):
    for k in range(len(T[j])):
        dp[j][k] = T[j][k] + max(dp[j+1][k], dp[j+1][k+1])
print(dp[0][0])
