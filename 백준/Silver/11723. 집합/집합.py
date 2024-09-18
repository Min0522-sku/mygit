import sys
input = sys.stdin.readline

S = set()

M = int(input()) 

for _ in range(M):
    command = input().strip().split()

    if command[0] == "add":
        S.add(int(command[1]))

    elif command[0] == "remove":
        S.discard(int(command[1]))  # remove는 없으면 에러를 발생시키니 discard 사용

    elif command[0] == "check":
        if int(command[1]) in S:
            print(1)
        else:
            print(0)

    elif command[0] == "toggle":
        x = int(command[1])
        if x in S:
            S.remove(x)
        else:
            S.add(x)

    elif command[0] == "all":
        S = set(range(1, 21))

    elif command[0] == "empty":
        S.clear()