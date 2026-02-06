import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cardList = list(map(int, input().split()))
bestSum = 0
for i in range(N): # 0 부터 n-3
    for j in range(i+1, N): # i+1 부터 n-2 
        for k in range(j+1, N): # j+1 부터 n-3
            currentSum = cardList[i] + cardList[j] + cardList[k]

            if currentSum <= M:
                if currentSum > bestSum:
                    bestSum = currentSum

print(bestSum)
