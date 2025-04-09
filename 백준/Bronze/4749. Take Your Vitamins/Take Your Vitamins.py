ans = []
while True:
    line = input()
    A_str, U, R_str, V = line.split(maxsplit=3)
    A = float(A_str)
    R = float(R_str)
    if A < 0:
        break
    P = (A/R) * 100
    if P < 1:
        ans.append(V)
    else:
        print(F"{V} {A:.1f} {U} {round(P)}%")
if ans:
    print("Provides no significant amount of:")
    for i in ans:
        print(i)