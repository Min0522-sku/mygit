N = int(input())
l = [''] * 50
for i in range(N):
    m = list(input().strip())
    l[i] = m

for i in range(N, 50):
    l[i] = l[0]

ans = ""
k = 0

for j in range(len(l[0])):
    if l[k][j] == l[k+1][j] == l[k+2][j] == l[k+3][j] == l[k+4][j] == l[k+5][j] == l[k+6][j] == l[k+7][j] == l[k+8][j] == l[k+9][j] == l[k+10][j] == l[k+11][j] == l[k+12][j] == l[k+13][j] == l[k+14][j] == l[k+15][j] == l[k+16][j] == l[k+17][j] == l[k+18][j] == l[k+19][j] == l[k+20][j] == l[k+21][j] == l[k+22][j] == l[k+23][j] == l[k+24][j] == l[k+25][j] == l[k+26][j] == l[k+27][j] == l[k+28][j] == l[k+29][j] == l[k+30][j] == l[k+31][j] == l[k+32][j] == l[k+33][j] == l[k+34][j] == l[k+35][j] == l[k+36][j] == l[k+37][j] == l[k+38][j] == l[k+39][j] == l[k+40][j] == l[k+41][j] == l[k+42][j] == l[k+43][j] == l[k+44][j] == l[k+45][j] == l[k+46][j] == l[k+47][j] == l[k+48][j] == l[k+49][j]:
        ans += l[0][j]
    else:
        ans += '?'

print(ans)
