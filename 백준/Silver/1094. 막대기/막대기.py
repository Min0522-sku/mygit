X = int(input())
s = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in range(len(s)):
    if X >= s[i]:
        count +=1
        X -= s[i]
    if X == 0:
        break
print(count)