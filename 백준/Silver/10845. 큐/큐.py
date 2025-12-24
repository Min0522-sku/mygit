import sys
input = sys.stdin.readline  
queue = []  
N = int(input()) ## 명령어 갯수 int 형으로 입력 받기
for i in range(N): ## N 번만큼 반복 그만큼 명령어 받기 위해서
    cmd = input().split() ## 명령어 배열 형식으로 받기 명령어와 push의 숫자값을 받기 위해서

    if cmd[0] == "push":   
        queue.append(int(cmd[1])) 
    elif cmd[0] == "pop":  
        if len(queue) != 0: 
            print(queue[0])
            del queue[0]
        else:
            print('-1')
    elif cmd[0] == "size":
        print(len(queue)) 
    elif cmd[0] == "empty":
        if len(queue) != 0: 
            print('0')
        else:
            print('1')
    elif cmd[0] == "front":
        if len(queue) != 0:
            print(queue[0])
        else:
            print('-1')
    elif cmd[0] == "back":
        if len(queue) != 0:
            print(queue[-1])
        else:
            print('-1')