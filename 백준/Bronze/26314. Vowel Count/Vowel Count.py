N = int(input())
V = "aeiou"
ans = []
for _ in range(N):
    V_count = 0
    C_count = 0
    name = input().strip()
    ans.append(name)
    for ch in name:
        if ch in V:
            V_count +=1
        else:
            C_count +=1
    if V_count > C_count:
        ans.append(1)
    else:
        ans.append(0)
for i in ans:
    print(i)