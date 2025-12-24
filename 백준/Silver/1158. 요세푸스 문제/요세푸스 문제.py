n, x = map(int, input().split())
lst = list(range(1, n+1))
index = 0
result = []

while lst:
    index = (index + x - 1) % len(lst)
    result.append(lst.pop(index))

# 결과를 < 와 > 로 둘러쌓인 형태로 출력
print(f"<{', '.join(map(str, result))}>")
