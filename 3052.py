s = []
namoge = set()
for i in range(10):  
    n = int(input())
    s.append(n)
for i in s:
    namoge.add(i%42)
    

print(len(namoge))

