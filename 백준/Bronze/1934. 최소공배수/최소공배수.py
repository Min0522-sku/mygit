import math

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    ans = A * B // math.gcd(A, B)
    print(ans)