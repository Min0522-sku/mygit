N, Q = map(int, input().split())
h =[0]
for _ in range(N):
    h.append(int(input()))

sum = [0] * (N+1)
for i in range(1, N+1):
    sum[i] = sum[i-1] + h[i]
for _ in range(Q):
    S, E = map(int, input().split())
    print(sum[E]-sum[S-1])