N = int(input())
count = 0
num = 666
while count < N:
    if '666' in str(num):
        count += 1
    if count < N:
        num += 1
print(num)