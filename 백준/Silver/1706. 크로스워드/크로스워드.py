R, C = map(int, input().split())
puzzle = [[]  for i in range(R)]
ans = []
for i in range(R):
    puzzle[i] = list(input())

for i in range(R):
    word = ""
    for j in range(C):
        if puzzle[i][j] == '#':
            if len(word) >= 2:
                ans.append(word)
            word = ""
        else:
            word += puzzle[i][j]
    if len(word) >= 2:
        ans.append(word)

for j in range(C):
    word = ""
    for i in range(R):
        if puzzle[i][j] == '#':
            if len(word) >= 2:
                ans.append(word)
            word = ""
        else:
            word += puzzle[i][j]
    if len(word) >= 2:
        ans.append(word)
        
ans.sort()
print(ans[0])