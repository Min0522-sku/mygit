import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name = {}
num = {}
result =[]

for i in range(1,N+1):
    N = input().strip()
    name[i] = N
    num[N] = i

for _ in range(M):
    a = input().strip()

    if a.isdigit():
        result.append(name[int(a)])
    else:
        result.append(str(num[a]))

for j in result:
    print(j)
