import sys
input = sys.stdin.readline

N = int(input().strip())
M = []
for _ in range(N):
    M.append(list(map(int, input().split())))

# 종료시간이 제일 작은 순, 시작시간이작은순 으로 정렬
M.sort(key = lambda x: (x[1], x[0])) 

cnt = 0
end_time = 0

for start, end in M: 
    if start >= end_time: # 앞외의가 끝나고 바로 시작 가능하거나 그 이후라면
        cnt += 1 # 카운트 += 1
        end_time = end # 회의끝나는 시간 변경

print(cnt)