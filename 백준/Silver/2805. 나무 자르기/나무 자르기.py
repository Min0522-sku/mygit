import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 나무의 수, M: 가져가려는 나무의 길이
N_list = list(map(int, input().split()))  # 각 나무의 길이를 리스트로 입력받음

# 이분 탐색을 위한 시작과 끝 범위 설정
low, high = 1, max(N_list)  # low: 절단기 높이의 최소값, high: 절단기 높이의 최대값 (제일 큰 나무 길이)

# 이분 탐색 시작
while low <= high:  # 절단기 높이를 조정하면서 탐색 (low가 high보다 작거나 같을 때까지 반복)
    sum = 0  # 자른 나무들의 합을 저장하는 변수
    mid = (low + high) // 2  # 절단기 높이(mid)를 중앙값으로 설정
    
    # 모든 나무에 대해 자른 나무 길이를 계산
    for i in N_list:
        if i > mid:  # 나무가 절단기 높이보다 클 때만 자를 수 있음
            sum += i - mid  # 자른 부분의 나무 길이를 더함 (나무 길이 - 절단기 높이)

    # 자른 나무들의 길이 합(sum)이 필요한 길이(M)보다 적으면 절단기 높이를 낮춤
    if sum < M:  # 자른 나무 길이의 합이 목표보다 작을 경우
        high = mid - 1  # 절단기 높이를 낮추기 위해 상한선을 mid - 1로 설정
    else:  # 자른 나무 길이 합이 목표보다 크거나 같으면
        low = mid + 1  # 절단기 높이를 높이기 위해 하한선을 mid + 1로 설정

# 조건을 만족하는 최대 절단기 높이(high)를 출력
print(high)
