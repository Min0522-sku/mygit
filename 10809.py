S = list(input())
N=[-1] * 26
for i in range(len(S)):
    current = ord(S[i]) - ord('a')
    if N[current] == -1:
        N[current] = i
print(' '.join(map(str, N)))