from datetime import datetime

s = input()
current = datetime.strptime(s, "%B %d, %Y %H:%M")

start = datetime(current.year, 1, 1, 0, 0)
end = datetime(current.year + 1, 1, 1, 0, 0)

e = current - start
total = end - start

p = (e.total_seconds() / total.total_seconds()) * 100

print(p)