import sys
input = sys.stdin.readline

K, N = map(int, input().split())
K_list = []
for _ in range(K):
    K_list.append(int(input()))

low, high = 1, max(K_list)

while low <= high:  
    mid = (low + high) //2
    counter = 0
    
    for i in K_list:
        counter += i//mid
    
    if counter >= N:
        low = mid +1
    else:
        high = mid -1

print(high)
