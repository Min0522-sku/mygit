n = int(input())
tlist = list(map(int, input().split()))
t, p = map(int, input().split())
anst = 0

for i in range(len(tlist)):
    if tlist[i] % t == 0:
        anst += tlist[i]//t
    else:
        anst += tlist[i]//t + 1
print(anst)
print(n//p, n%p)
