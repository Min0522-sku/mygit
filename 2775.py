t = int(input())
ans = []

for _ in range(t):
    k = int(input())
    n = int(input())
    
    # 아파트 배열 초기화
    apart = [[0] * (n + 1) for _ in range(k + 1)]
    
    # 0층 초기화
    for i in range(1, n + 1):
        apart[0][i] = i
    
    # 각 층과 호수에 사는 사람 수 계산
    for floor in range(1, k + 1):
        for room in range(1, n + 1):
            apart[floor][room] = apart[floor][room - 1] + apart[floor - 1][room]
    
    # 결과 저장
    ans.append(apart[k][n])

# 결과 출력
for result in ans:
    print(result)
