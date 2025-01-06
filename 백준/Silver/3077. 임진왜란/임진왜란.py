import sys
input = sys.stdin.readline

N = int(input().strip())
Cans = input().split()
l = input().split()

l_index = {l[i]: i for i in range(N)}

total = 0
Ctotal = 0

for i in range(N):
    for j in range(i +1, N):
        total += 1
        if l_index[Cans[i]] < l_index[Cans[j]]:
            Ctotal += 1

print(f"{Ctotal}/{total}")