W = input()
L = len(W) // 3
w1 = W[0:L]
w2 = W[L:2*L]
w3 = W[2*L:]
if w1 == w2 or w1 == w3:
    print(w1)
else:
    print(w2) 