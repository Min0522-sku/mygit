T = int(input()) #테스트 케이스 갯수
ans =[] #테스트 케이스의 결과들을 담을 리스트
for _ in range(T): # 테스트 케이스 만큼 반복
    M, N, K = map(int, input().split())
    field = [[0]* N for _ in range(M)] # 0 으로 이루어진 필드 생성
    for _ in range(K):
        a, b = map(int, input().split()) # 주어진 위치에 배추 심기
        field[a][b] = 1
    visit = [[False]* N for _ in range(M)] # dfs를 위해 방문여부 리스트 생성
    dir = [(1,0), (-1,0), (0,1), (0,-1)] #상하좌우 방향
    count = 0 #배추밭의 배추군집? 개수를 위한 변수
    for i in range(M): #필드의 모든 위치 검사
        for j in range(N):
            if field[i][j] == 1 and not visit[i][j]: #현재 위치에 배추가 있고 아직 방문하지 않은 경우
                stack = [(i,j)] #dfs 수행을 위한 스택 구현
                visit[i][j] = True #현재 위치 방문 처리
                while stack: #스택이 비어 있지 않은 동안 dfs수행
                    x, y = stack.pop() #스택에서 위치를 꺼냄
                    for dr, dc in dir:
                        new_x, new_y = x + dr, y + dc  #상하좌우 이동하여 새로운 위치
                        if (0 <= new_x < M and 0 <= new_y < N  # 새로운 위치가 필드 내에 있고
                            and field[new_x][new_y] == 1  # 새로운 위치에 배추가 있고
                            and not visit[new_x][new_y]): # 새로운 위치가 방문하지 않은 경우
                            stack.append((new_x, new_y)) #새로운 위치를 스택에 추가 후 방문처리
                            visit[new_x][new_y] = True
                count += 1 # 위치마다 상하좌우 방문을 다하고 스택이 비어서 while문이 끝난경우 하나의 군집을 처리함으로써 카운트 증가
    ans.append(count) #하나의 테스트 케이스가 끝낫음으로 카운트 결과를 리스트에 추가
for h in ans: #결과 출력
    print(h)