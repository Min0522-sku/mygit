n = int(input())
s = []
for i in range(n):
    H, W, N = map(int, input().split())
    a = N / H
    b = N % H
    if a > 1 and N/H != N//H:
        a = (N//H)+1
    else:
        a = N//H
    if b == 0:
        b = H
    if a < 10:
        s.append(str(b)+'0'+str(a))
    else:
        s.append(str(b)+str(a))
for i in range(n):
    print(s[i])