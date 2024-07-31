import math
n = int(input())
if n == 1:
    print(1)
else:
    a = (math.sqrt(12*n-3)-3)/6
    print(math.ceil(a)+1)