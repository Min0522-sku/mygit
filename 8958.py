n = int(input())


ans = []
for i in range(n):
    sum = 0
    count = 0
    s = list(input())
    while s:
        a = s.pop()
        if a == 'O':
            count += 1
            sum += count
        elif a == 'X':
            count = 0
    ans.append(sum)

for i in range(len(ans)):
    print(ans[i])