import sys
sys.setrecursionlimit(10**6)
# 입력 받기
n = int(input())  # 지역의 크기 N
height_map = [list(map(int, input().split())) for _ in range(n)]

# 상, 하, 좌, 우 방향을 탐색하기 위한 좌표 변화값 (델타 배열)
dx = [1, -1, 0, 0]  # x축 방향 (오른쪽, 왼쪽)
dy = [0, 0, 1, -1]  # y축 방향 (아래쪽, 위쪽)

# DFS로 물에 잠기지 않는 영역을 탐색하는 함수
def dfs(x, y, height, visited):
    visited[x][y] = True  # 현재 위치를 방문 처리
    # 상, 하, 좌, 우로 인접한 네 방향을 확인
    for i in range(4):
        nx = x + dx[i]  # 새로운 x 좌표
        ny = y + dy[i]  # 새로운 y 좌표
        # 새 좌표가 유효한 범위 내에 있고, 방문하지 않았으며, 현재 높이 기준 물에 잠기지 않는 곳이라면
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and height_map[nx][ny] > height:
            dfs(nx, ny, height, visited)  # 그 지점에서 다시 DFS로 탐색

# 주어진 높이에서 안전한 영역의 개수를 세는 함수
def get_safe_areas_count(height):
    visited = [[False] * n for _ in range(n)]  # 방문 여부를 확인하는 배열, 모든 지점을 처음엔 False로 초기화
    count = 0  # 안전한 영역의 개수를 저장할 변수
    # 모든 지점을 순회하면서 물에 잠기지 않는 영역을 찾기
    for i in range(n):
        for j in range(n):
            # 현재 지점이 물에 잠기지 않았고 아직 방문하지 않았다면
            if height_map[i][j] > height and not visited[i][j]:
                dfs(i, j, height, visited)  # 그 지점에서 DFS로 연결된 모든 영역을 방문 처리
                count += 1  # 새로운 안전한 영역을 발견했으므로 개수를 증가시킴
    return count  # 해당 높이에서 발견된 안전한 영역의 개수를 반환

# 지역 내에서 가장 높은 값을 찾음
max_height = max(map(max, height_map))  # 2차원 배열에서 가장 큰 값을 찾음

# 가능한 모든 높이에 대해 안전한 영역의 최대 개수를 계산
max_safe_areas = 0  # 최대 안전한 영역의 개수를 저장할 변수
for height in range(max_height + 1):  # 가장 높은 값까지만 반복
    max_safe_areas = max(max_safe_areas, get_safe_areas_count(height))  # 모든 높이에 대해 안전한 영역의 최대값을 계산

# 결과 출력
print(max_safe_areas)
