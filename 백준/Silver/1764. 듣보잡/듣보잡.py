N, M = map(int, input().split())
no_listen = set()
no_see = set()

for _ in range(N):
    no_listen.add(input().strip())

for _ in range(M):
    no_see.add(input().strip())

no_listen_see = sorted(no_listen & no_see)
print(len(no_listen_see))

for name in no_listen_see:
    print(name)