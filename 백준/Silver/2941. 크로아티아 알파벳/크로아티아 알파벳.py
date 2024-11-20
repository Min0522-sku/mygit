alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
w = input().strip()
for i in alphabet:
    w = w.replace(i, "*")
print(len(w)) 