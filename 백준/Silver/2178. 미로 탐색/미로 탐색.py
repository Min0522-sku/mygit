from collections import deque

# BFS 함수 정의
def bfs(maze, n, m):
    # 상, 하, 좌, 우 탐색을 위한 방향 벡터
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 큐를 사용한 BFS 탐색 (1,1)에서 시작 (0-index를 고려해서 (0,0)부터 시작)
    queue = deque([(0, 0)])  # 시작점
    maze[0][0] = 1  # 시작점에서의 거리
    
    # BFS 탐색
    while queue:
        x, y = queue.popleft()
        
        # (n, m)에 도착하면 이동한 칸 수 반환
        if x == n - 1 and y == m - 1:
            return maze[x][y]
        
        # 네 방향으로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 미로의 범위를 벗어나지 않고, 이동할 수 있는 칸(1)이어야 함
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                # 이동한 위치까지의 거리 갱신
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    
    return -1  # 도달할 수 없는 경우 -1 반환 (필요할 경우)

# 입력 받기
n, m = map(int, input().split())  # 미로의 크기
maze = [list(map(int, input().strip())) for _ in range(n)]  # 미로 배열

# BFS 실행하여 결과 출력
result = bfs(maze, n, m)
print(result)
