S = []
a = True
while a:
    x = list(map(int, input().split()))
    x.sort()
    if x[0] == 0 and x[1] == 0 and x[2] == 0:
        a = False
    elif x[0]*x[0]+x[1]*x[1]==x[2]*x[2]:
        S.append('right')
    else:
        S.append('wrong')
for i in range(len(S)):
    print(S[i])