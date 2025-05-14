import math
N = int(input())
ans1 = N - (N*22/100)
ans2 = N - (N - (N*80/100))*22/100
print(math.trunc(ans1), math.trunc(ans2))