import sys
input = sys.stdin.readline

def binary_search(arr, target):
    low, high = 0, len(arr) -1

    while low <= high:
        mid = (low + high) //2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            low = mid +1
        else:
            high = mid -1
    return 0

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))
N_list.sort()
for arr in M_list:
    print(binary_search(N_list, arr))