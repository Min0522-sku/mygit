import sys
input = sys.stdin.readline

N, M = map(int, input().split())
di = {}
result =[]

for _ in range(N):
    name, password = input().split()
    di[name] = password

for _ in range(M):
    a = input().strip()
    if a in di:
        result.append(di[a])
   

for j in result:
    print(j)