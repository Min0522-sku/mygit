def d(n):
    return n + sum(int(digit) for digit in str(n))
limit = 10000
num = set()
for i in range(1, limit+1):
    num.add(d(i))

for i in range(1, limit+1):
    if i not in num:
        print(i)