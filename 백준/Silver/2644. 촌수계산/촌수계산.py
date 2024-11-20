from collections import deque

def bfs(n, start, end, r):
    graph = {i: [] for i in range(1, n+1)}
    for x, y in r:
        graph[x].append(y)
        graph[y].append(x)

    visit = [-1] * (n+1)
    queue = deque([start])
    visit[start] = 0

    while queue:
        current = queue.popleft()
        for ch in graph[current]:
            if visit[ch] == -1:
                visit[ch] = visit[current] +1
                queue.append(ch)
    return visit[end]

n = int(input())
start, end = map(int, input().split())
m = int(input())
r = [tuple(map(int, input().split())) for _ in range(m)]
ans = bfs(n, start, end, r)
print(ans if ans != -1 else -1)