import math
T = int(input())
for i in range(T):
    L = input().strip()
    Ls = L[0:math.ceil(len(L)/3)]
    r_Ls = Ls[::-1]
    t_r_Ls = r_Ls[1:]
    t_Ls = Ls[1:]
    if L == Ls + r_Ls + Ls or L == Ls+t_r_Ls+Ls or L == Ls+r_Ls+t_Ls or L == Ls+t_r_Ls+t_Ls:
        print("1")
    else:
        print("0")
