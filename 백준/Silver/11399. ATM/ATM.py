N = int(input().strip())
P = list(map(int, input().split()))
P.sort()
total_time = 0
t = 0
for i in P:
    t += i
    total_time += t
print(total_time)
