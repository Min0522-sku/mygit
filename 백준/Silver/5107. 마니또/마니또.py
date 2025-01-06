import sys
from collections import defaultdict
input = sys.stdin.readline
visited = {}

def dfs(node, parent):
    global is_cycle
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, node)
        elif neighbor != parent:
            is_cycle = True


count = 1
while True:
    
    N = int(input().strip())
    if N == 0:
        break

    edges = []
    graph = defaultdict(list)

    for i in range(N):
        a , b = input().split()
        graph[a].append(b)
        graph[b].append(a)
        edges.append(a)
        edges.append(b)

    visited = {node: False for node in set(edges)}
    
    cycle_count = 0
    for node in visited:
        if not visited[node]:
            is_cycle = False
            dfs(node, None)
            if is_cycle:
                cycle_count += 1
    
    print(f"{count} {cycle_count}")
    count += 1