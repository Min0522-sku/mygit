import math
X_1, Y_1, R_1 = map(int, input().split())
X_2, Y_2, R_2 = map(int, input().split())
D = math.sqrt(((X_2-X_1)**2) +((Y_2- Y_1)**2))
if D < R_1 + R_2:
    print('YES')
else:
    print('NO')