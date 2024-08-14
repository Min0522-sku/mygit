a = [0] * 10001
n = int(input())
for _ in range(n):
    N = int(input())
    a[N] +=1
for N in range(1, 10001):
    for _ in range(a[N]):
        print(f"{N}")
