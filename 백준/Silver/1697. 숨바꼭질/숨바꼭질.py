from collections import deque

def find_fastest_time(n, k):
    # 수빈이의 위치가 동생의 위치보다 같거나 큰 경우에는 무조건 뒤로 걷기만 하면 된다.
    if n >= k:
        return n - k
    
    # 각 위치를 방문했는지 여부를 기록하는 배열과 최대 좌표 범위 설정
    visited = [False] * 100001
    queue = deque([(n, 0)])  # (현재 위치, 시간)
    visited[n] = True
    
    while queue:
        current_position, time = queue.popleft()
        
        # 동생의 위치에 도달하면 시간을 반환
        if current_position == k:
            return time
        
        # 수빈이가 이동할 수 있는 경우의 수를 탐색
        for next_position in (current_position - 1, current_position + 1, current_position * 2):
            if 0 <= next_position <= 100000 and not visited[next_position]:
                visited[next_position] = True  # 해당 위치를 방문 처리
                queue.append((next_position, time + 1))  # 다음 위치와 시간을 큐에 추가

# 입력 받기
n, k = map(int, input().split())
print(find_fastest_time(n, k))
