T = int(input())
ans =[]
for _ in range(T): # 테스트 케이스 만큼 반복
    M, N, K = map(int, input().split())
    field = [[0]* N for _ in range(M)] # 0 으로 이루어진 필드 생성
    for _ in range(K):
        a, b = map(int, input().split()) # 주어진 위치에 배추 심기
        field[a][b] = 1
    visit = [[False]* N for _ in range(M)] # dfs를 위해 방문여부 리스트 생성
    dir = [(1,0), (-1,0), (0,1), (0,-1)] #상하좌우 방향
    count = 0
    for i in range(M):
        for j in range(N):
            if field[i][j] == 1 and not visit[i][j]:
                stack = [(i,j)]
                visit[i][j] = True
                while stack:
                    row, col = stack.pop()
                    for dr, dc in dir:
                        new_row, new_col = row + dr, col + dc
                        if (0 <= new_row < M and 0 <= new_col < N and
                                field[new_row][new_col] == 1 and not visit[new_row][new_col]):
                            stack.append((new_row, new_col))
                            visit[new_row][new_col] = True
                count += 1
    ans.append(count)
for h in ans:
    print(h)