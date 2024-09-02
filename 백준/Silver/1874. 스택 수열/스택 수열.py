stack = []
ans = []
i = 1
result = True
n = int(input()) 
for _ in range(n): 
    num = int(input()) 
    
    while  num >= i:
        stack.append(i)
        ans.append('+')
        i += 1

    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        result = False
        break

if result == False:
    print("NO")
else:
    for j in ans:
        print(j)
        