stack = []
ans = [] #push(append)와 pop연산이 일어날때마다 +와-를 넣기위한 리스트
i = 1     #입력되는 수열의 현재 수와 비교하여 스택에 삽입할 증가되는 변수
result = True #입력되는 수열을 만들수 있는지 확인하는 변수
n = int(input()) 
for _ in range(n): 
    num = int(input()) # 현재 입력되는 수열의 수 받기  
    
    while  num >= i: #입력된 수열의 현재수와 스택에 삽입할 변수 i를 비교하여 같은수까지 스택에 넣기위한 while문
        stack.append(i)
        ans.append('+')
        i += 1

    if stack[-1] == num: #스택 맨 위의 값과 현재 입력되는 수열의 수가 같으면 제거
        stack.pop()
        ans.append('-')
    else: # 입력되는 수열을 만들지 못하니 NO를 출력하기 위해 False로 설정
        result = False
        break

if result == False:
    print("NO")
else:
    for j in ans:
        print(j)