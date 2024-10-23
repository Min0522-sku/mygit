T = int(input().strip())
ans = []
for _ in range(T):
    N, M = input().strip().split()
    N = float(N)
    if M == "kg":
        ans.append((N * 2.2046, "lb"))
    elif M == "l":
        ans.append((N * 0.2642, "g"))
    elif M == "lb":
        ans.append((N * 0.4536, "kg"))
    elif M == "g":
        ans.append((N * 3.7854, "l"))

for a, b in ans:
    print(f"{a:.4f} {b}")
