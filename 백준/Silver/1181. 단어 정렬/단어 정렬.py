import sys
input = sys.stdin.readline

n = int(input())
words = []
for i in range(n):
    words.append(input().strip())
words = list(set(words)) ## 중복제거
words.sort(key=lambda x: (len(x), x)) ## 1순위 길이 2순위 알파벳

for j in words:
    print(j)