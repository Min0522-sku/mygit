N, K = map(int, input().split())
A = []
for i in range(N):
    b = int(input().strip())
    A.append(b)
A.sort(reverse=True)
count = 0
for i in A:
    count += K//i
    K %= i
print(count)