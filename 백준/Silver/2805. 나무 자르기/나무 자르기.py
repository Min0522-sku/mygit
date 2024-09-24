import sys
input = sys.stdin.readline



N, M = map(int, input().split())
N_list = list(map(int, input().split()))

low, high = 0, max(N_list)

while low <= high:
    sum = 0
    mid = (low + high) //2
    
    for i in N_list:
        if i > mid:
            sum += i -mid
    
    if sum < M:
        high = mid -1
    else:
        low = mid + 1
print(high)