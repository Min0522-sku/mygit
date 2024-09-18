def char_to_num(char):
    return ord(char) - ord('a') + 1

N = int(input())
L = list(map(str, input().strip()))
result = 0
for i in range(len(L)):
    result += (char_to_num(L[i]) * 31**i)
print(result % 1234567891)