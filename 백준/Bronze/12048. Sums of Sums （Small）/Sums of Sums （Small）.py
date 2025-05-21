T = int(input())
for t in range(1,T+1):
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    q = [tuple(map(int, input().split())) for _ in range(Q)]

    s_sum = [0] * (N+1)
    for i in range(N):
        s_sum[i+1] = s_sum[i] + A[i]

    ans = []
    for i in range(N):
        for j in range(i, N):
            sub = s_sum[j+1] - s_sum[i]
            ans.append(sub)

    ans.sort()

    print(f"Case #{t}:")
    for Li, Ri in q:
        result = sum(ans[Li -1 : Ri])
        print(result)
