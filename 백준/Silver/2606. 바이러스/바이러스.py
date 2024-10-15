def dfs(graph, v, visited):
    visited[v] = True  # 현재 노드를 방문 처리
    for i in graph[v]:  # 현재 노드와 연결된 다른 노드를 탐색
        if not visited[i]:
            dfs(graph, i, visited)

# 입력받기
n = int(input())  # 컴퓨터 수
m = int(input())  # 연결된 쌍의 수
graph = [[] for _ in range(n + 1)]  # 컴퓨터 번호는 1부터 시작하므로 n+1개의 리스트
visited = [False] * (n + 1)  # 방문 여부 체크 리스트

# 연결된 쌍 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 연결이므로 서로 추가

# 1번 컴퓨터에서 시작하여 바이러스가 퍼지는 컴퓨터 수 세기
dfs(graph, 1, visited)

# 1번 컴퓨터는 제외하고 방문된 컴퓨터의 개수 출력
print(visited.count(True) - 1)
