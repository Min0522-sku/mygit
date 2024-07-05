n = list(map(int, input().split()))
count = 0
decount = 0
for i in range(len(n)-1):
        if n[i]+1 == n[i+1]:
            count += 1 
        if n[i]-1 == n[i+1]:
            decount += 1

if count == 7:
    print("ascending")
elif decount == 7:
    print("descending")
else:
    print("mixed")