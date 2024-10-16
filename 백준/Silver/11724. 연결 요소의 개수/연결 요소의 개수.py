import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())  # 정점의 개수 n, 간선의 개수 m
graph = [[] for _ in range(n + 1)]  # 1-based 인덱스 사용

# 간선 정보 입력
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 배열 초기화
visited = [False] * (n + 1)

# DFS 함수 정의
def dfs(v):
    visited[v] = True  # 현재 정점 방문 처리
    for neighbor in graph[v]:  # 인접한 모든 정점 탐색
        if not visited[neighbor]:
            dfs(neighbor)

# 연결 요소 개수를 찾기 위한 코드
connected_components = 0
for i in range(1, n + 1):
    if not visited[i]:  # 아직 방문하지 않은 정점이 있다면
        dfs(i)  # 그 정점에서 DFS 실행
        connected_components += 1  # 연결 요소 개수 증가

# 결과 출력
print(connected_components)
