import math
n = int(input())
nlist = list(map(int, input().split()))
count = 0
for num in nlist:
    if num > 1:  # 1보다 큰 숫자만 소수 검사
        is_prime = True
        if num <= 3:
            is_prime = True
        elif num % 2 == 0 or num % 3 == 0:
            is_prime = False
        else:
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    is_prime = False
                    break
                i += 6
        if is_prime:
            count += 1
print(count)