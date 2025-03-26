N = int(input())
for _ in range(N):
    y = int(input())
    x = y ** 2
    y = str(y)
    x = str(x)
    if x.endswith(y):
        print("YES")
    else:
        print("NO")