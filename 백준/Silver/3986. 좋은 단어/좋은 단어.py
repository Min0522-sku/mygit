N = int(input())
count = 0
for i in range(N):
    stack = []
    s = list(input().split())
    for j in range(len(s[0])):
        stack.append(s[0][j])
        if stack[-1] == stack[len(stack)-2] and len(stack) >=2:
            stack.pop(-1)
            stack.pop(-1)
    if not stack:
        count +=1
    else: continue

print(count)
            
        