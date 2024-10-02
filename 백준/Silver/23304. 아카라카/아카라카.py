import sys
input = sys.stdin.readline

s = input().strip()

def akaraka(string):
    if len(string) == 1: #길이가 1이라면 참 리턴
        return True
    else: 
        if string != string[::-1]: #기존문자열과 역순으로한 문자열 이 같지 않으면 실패 리턴
            return False
        half = len(string)//2 #문자열의 반절의 길이 저장
        left = string[: half] #문자열의 첫번째부터 반절의 길이까지 left(왼쪽)에 저장
        return akaraka(left) #left를 넣고 함수 반복 
#왼쪽만 넣는 이유는 위에서 역순과 비교했을때 참이기때문에 왼쪽과 오른쪽은 같은 문자열임으로 한쪽만 선택해서 재귀함수 진행하면됨


if akaraka(s): #함수의 리턴값이 참이면
    print("AKARAKA")
else:
    print("IPSELENTI")
