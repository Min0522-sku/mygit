import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coinList =[]
for _ in range(N):
    coinList.append(int(input().strip()))

coinList.reverse() ## 제일 큰수부터 몫을 구하기 위해서 뒤집음
count = 0

for i in coinList:
    count += K//i  ## 목표값을 coinList의 요소로 나눈 몫(나눌수 있다면) 만큼 카운트에 추가
    K %= i ## 목표값을 요소로 나눈 나머지로 수정
print(count)