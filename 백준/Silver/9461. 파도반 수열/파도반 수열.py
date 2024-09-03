T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    L =[1,1,1,2,2,3,4,5]
    if N >8:
        for i in range(7, N):
            L.append(L[i]+L[i-4])
        ans.append(L[N-1])
    else: ans.append(L[N-1])

for i in ans:
    print(i)
