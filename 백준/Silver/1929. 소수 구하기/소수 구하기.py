import sys
input = sys.stdin.readline

M, N = map(int, input().split())

def is_prime(n):
    if n < 2:  # 0과 1은 소수가 아님
        return False
    for i in range(2, int(n**0.5) + 1):  # 제곱근까지만 검사
        if n % i == 0:  # 나누어 떨어지면 소수가 아님
            return False
    return True

for i in range(M, N + 1):
    if is_prime(i):  # 소수인 경우만 출력
        print(i)
