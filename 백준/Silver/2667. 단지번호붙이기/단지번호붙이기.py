# 입력 받기
n = int(input())  # 지도 크기
map_data = [list(map(int, input())) for _ in range(n)]  # 지도 정보 입력 (2차원 배열)

# 상, 하, 좌, 우 이동을 위한 방향 배열
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# DFS로 단지를 탐색하는 함수
def dfs(x, y):
    global count  # 집의 수를 세기 위한 전역 변수
    map_data[x][y] = 0  # 방문한 집은 0으로 바꿔서 다시 방문하지 않도록 처리
    count += 1  # 현재 집을 포함시키므로 count를 증가
    # 상하좌우로 인접한 집을 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 지도의 범위를 벗어나지 않고, 집이 있는 곳(1)이면 계속 탐색
        if 0 <= nx < n and 0 <= ny < n and map_data[nx][ny] == 1:
            dfs(nx, ny)

# 단지 정보를 저장할 리스트
complexes = []

# 지도의 각 위치를 순회하면서 단지 찾기
for i in range(n):
    for j in range(n):
        # 집이 있는 곳(1)을 찾으면 DFS 시작
        if map_data[i][j] == 1:
            count = 0  # 단지 내 집의 수를 세기 위한 변수
            dfs(i, j)
            complexes.append(count)  # 단지의 집 수를 리스트에 저장

# 단지 수와 각 단지의 집 수를 오름차순으로 출력
complexes.sort()  # 오름차순 정렬
print(len(complexes))  # 총 단지 수 출력
for complex_size in complexes:
    print(complex_size)  # 각 단지의 집 수 출력
