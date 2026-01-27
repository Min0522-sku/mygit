import sys
input = sys.stdin.readline

N, M = map(int, input().split()) ## N,M을 입력받기

treeList = list(map(int, input().split())) ##treeList 입력받기

low, high = 0, max(treeList) ##low 는 0 high는 treeList에서 가장 큰값
while low <= high: ##low 가 high보다 커질때 까지 반복
    sum = 0 ## 자른 나무들의 길이
    mid = (low + high)//2 ## 나무 자르는 기준점

    for i in treeList:
        if i> mid: ## 트리 리스트안에 있는 나무들의 길이가 mid 기준점 보다 높으면 
            sum += i-mid ##잘라서 sum에 저장
    
    if sum < M:  ## 원하는 값보다 작을때 
        high = mid-1 ## high값을 기준점의 -1로 변경해서 자르는 높이를 확 낮춤 
    else: ## 원하는 값 보다 클때
        low = mid +1  ##low값을 기준점의 +1로 변경해서 자르는 높이를 확 높임

print(high)