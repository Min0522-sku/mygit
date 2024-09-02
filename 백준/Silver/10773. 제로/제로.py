K = int(input())
ans = []
for i in range(K):
    a = int(input())
    if a == 0:
        ans.pop()
    else: ans.append(a)
print(sum(ans))