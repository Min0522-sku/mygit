def abc(l):
    l = list(l)
    i = len(l) -2

    while i >= 0 and l[i] >= l[i+1]:
        i -= 1
    
    if i == -1:
        return ''.join(l)
    
    j = len(l) -1
    while l[j] <= l[i]:
        j -= 1
    
    l[i], l[j] = l[j], l[i]

    l = l[:i +1] + l[i +1:][::-1]
    return ''.join(l)
        


N = int(input().strip())
ans = []
for _ in range(N):
    l = input().strip()
    result = abc(l)
    ans.append(result)



for i in range(len(ans)):
    print(ans[i]) 