N = int(input().strip())
platform = []
for i in range(N):
    platform.append(list(map(int, input().split())))
southermost = min(platform, key= lambda coord: coord[1])
print(southermost[0], southermost[1])