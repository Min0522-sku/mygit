ans_list = []
while True:
    n = input()
    if n == '0':
        break
    reversed_n = n[::-1]
    if n == reversed_n:
        ans_list.append("yes")
    else:
        ans_list.append("no")
for i in range(len(ans_list)):
    print(ans_list[i])
