from datetime import datetime

date = input().strip()
N = int(input().strip())
date1 = datetime.strptime(date, "%Y-%m-%d")
count = 0
for i in range(N):
    c_date = input().strip()
    date2 = datetime.strptime(c_date, "%Y-%m-%d")
    if date1 <= date2:
        count +=1

print(count)