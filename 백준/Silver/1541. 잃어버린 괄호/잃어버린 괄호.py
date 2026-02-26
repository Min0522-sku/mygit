import sys
input = sys.stdin.readline
result = 0
l = input().split('-') # 입력값을 - 기준으로 싹다 덩어리로 분해
l1 = l[0].split('+') # 첫번째 덩어리는 여기서 빼야하는 값
for i in l1:
    result += int(i) #입력값이 문자열로 들어오므로 정수로 변경해 result에 더해줌

for i in range(1, len(l)):  # 0은 이미 분해 했으니 1부터 시작
    sum = 0 # 빼야할 값 
    sub = l[i].split('+') # 분해한 숫자들
    for num in sub: # 분해한 숫자를  num에 넣고
        sum += int(num) # 빼야할 값에 더해줌
    result -= sum  # result에서 빼기

print(result)