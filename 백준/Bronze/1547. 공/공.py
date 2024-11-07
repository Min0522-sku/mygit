M = int(input().strip())
cup = [0,1,0,0]
for i in range(M):
    X, Y = map(int, input().split())
    A = cup[X]
    B = cup[Y]
    cup[X] = B
    cup[Y] = A
for i in range(len(cup)):
    if cup[i] == 1:
        print(i)