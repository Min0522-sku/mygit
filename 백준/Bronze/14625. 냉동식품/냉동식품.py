H, M = map(int, input().split())
end_H, end_M = map(int, input().split())
N = int(input().strip())

count = 0
while True:
    if H-(N*10)<10 and H-(N*10)>=0:
        count +=1
    elif (H%10) == N:
        count +=1
    elif M-(N*10)<10 and M-(N*10)>=0:
        count +=1
    elif (M%10) == N:
        count +=1
    if H == end_H and M == end_M:
        break
    M+=1
    if M== 60:
        M = 0
        H +=1
        if H == 25:
            H = 0
print(count)