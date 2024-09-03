T = int(input())
ans = []
for _ in range(T):
    n = int(input())
    dp = [1,2,4]
    if n > 3:
        for i in range(3, n):
            dp.append(dp[i-3]+dp[i-2]+dp[i-1])
        ans.append(dp[n-1])
    else: ans.append(dp[n-1])

for j in ans:
    print(j)