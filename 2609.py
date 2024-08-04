a, b = map(int, input().split())
c, d = a, b
if c >= d:
    while d:
        c, d = d, c % d
    print(c)
    print((a*b)//c)
elif c <= d:
    while c:
        d, c = c, d % c
    print(d)
    print((a*b)//d)
    