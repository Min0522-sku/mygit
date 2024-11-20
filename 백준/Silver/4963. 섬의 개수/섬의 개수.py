import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def dfs(x,y):
    visited[x][y] = True
    for d in range(8):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and randmap[nx][ny] == 1:
            dfs(nx, ny)

while True:
    w, h = map(int, input().split()) 
    if w == 0 and h == 0:
        break
    randmap = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if randmap[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1
    print(count)