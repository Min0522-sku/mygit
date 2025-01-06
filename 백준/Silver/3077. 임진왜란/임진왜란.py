# 입력 처리
import sys
input = sys.stdin.readline

N = int(input().strip())
l = input().split()  # 정답 순서
ansl = input().split()  # 사용자 입력 순서

# 각 단어의 위치 저장
l_index = {l[i]: i for i in range(N)}  # 정답 순서의 위치 인덱스
ans_index = {ansl[i]: i for i in range(N)}  # 사용자 입력 순서의 위치 인덱스

# 정답 순서쌍 개수 및 일치하는 순서쌍 개수 계산
total_pairs = 0
correct_pairs = 0

for i in range(N):
    for j in range(i + 1, N):
        total_pairs += 1
        # 상대적 순서가 맞는지 비교
        if l_index[l[i]] < l_index[l[j]] and ans_index[l[i]] < ans_index[l[j]]:
            correct_pairs += 1

# 결과 출력
print(f"{correct_pairs}/{total_pairs}")
