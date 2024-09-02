import sys
input = sys.stdin.readline

def newround(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())
if n == 0:
    print(0)
else:
    
    K = []
    for _ in range(n):
        K.append(int(input()))
    K.sort()
    avr = newround(n * 0.15)
    

    print(newround(sum(K[avr:n-avr]) / len(K[avr:n-avr])))
