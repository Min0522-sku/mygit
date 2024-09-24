import sys
input = sys.stdin.readline
ans = 0
N = int(input())
N_list = list(map(int, input().split()))
M = int(input())

low, high = 1, max(N_list)
while low <= high:  
    mid = (low + high) //2
    money = 0
    for i in N_list:
        if i > mid:
            money += mid
        else:
            money += i
    if money <= M:
        ans = mid
        low = mid +1
    else:
        high = mid -1

print(ans)