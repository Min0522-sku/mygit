n = int(input())
c = []
d= []
for i in range(n):
    x, y = input().split()
    c.append(y)
    d.append(x)
for i in range(n):
    for k in range(len(c[i])):
        for j in range(int(d[i])):
            print(c[i][k] ,end="")
    print()