n = int(input())
ans = 0
for i in range(1,n):
    a = sum(int(s) for s in str(i))
    if i + a == n:
        ans = i
        break
print(ans)