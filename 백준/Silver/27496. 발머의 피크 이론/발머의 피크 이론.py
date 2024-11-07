N, L = map(int, input().split())
A = list(map(int, input().split()))

count = 0
A_c = 0
C = 0
C_c = 0
for i in A:
    count +=1
    C += i
    D = L//count
    if D== 0:
        C -= A[A_c]
        A_c +=1
    if 129 <= C and C <= 138:
        C_c +=1
    
print(C_c)
