a, b, c, d, e = map(int, input().split())
while not(a == 1 and b == 2 and c == 3 and d == 4 and e == 5):
    if a > b:
        N = a
        M = b
        a = M
        b = N
        print(a, b, c, d, e)
    if b > c:
        N = b
        M = c
        b = M
        c = N
        print(a, b, c, d, e)
    if c > d:
        N = c
        M = d
        c = M
        d = N
        print(a, b, c, d, e)
    if d > e:
        N = d
        M = e
        d = M
        e = N
        print(a, b, c, d, e)