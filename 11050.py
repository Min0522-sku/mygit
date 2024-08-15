import math
N, K = map(int, input().split())
ans = math.factorial(N) // (math.factorial(K) * math.factorial(N-K))
print(ans)