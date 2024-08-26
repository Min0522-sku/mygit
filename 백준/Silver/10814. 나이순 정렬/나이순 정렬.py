N = int(input())
L = []
for _ in range(N):
    age, name = input().split()
    age = int(age)
    L.append([age, name])
L.sort(key= lambda x: x[0])
for x,y in L:
    print(f"{x} {y}")