n = int(input())
a = []
for i in range(n):
    b = str(input().strip())
    a.append(b)
a = list(set(a))
a.sort(key = lambda x: (len(x), x))
for j in a:
    print(j)