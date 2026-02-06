import sys
input = sys.stdin.readline

N = int(input())
count = 0 # 666 나온 갯수 찾기
num = 0 # 0에서 증가하는 변수
while  count < N: # count 가 N에 도달하면 종료
    num +=1
    if "666" in  str(num): # num을 str 타입으로 강제 변환 했을때 666이 존재하면
        count +=1 #count 에 +1
print(num)