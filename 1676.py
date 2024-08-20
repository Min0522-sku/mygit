import math
N = int(input())
a = list(str(math.factorial(N)))
a.reverse()
count = 0
for i in a:
    if i =='0':
        count += 1
    else: break
print(count)
