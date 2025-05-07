n, m = map(int, input().split())
strokes = {
    'A':3, 'B':2, 'C':1, 'D':2, 'E':4, 'F':3, 'G':1, 'H':3, 'I':1, 'J':1,
    'K':3, 'L':1, 'M':3, 'N':2, 'O':1, 'P':2, 'Q':2, 'R':2, 'S':1, 'T':2,
    'U':1, 'V':1, 'W':1, 'X':2, 'Y':2, 'Z':1
}
name1, name2 = map(str, input().split())
mix = []
min_len = min(len(name1), len(name2))
for i in range(min_len):
    mix.append(name1[i])
    mix.append(name2[i])
if len(name1) > len(name2):
    mix.extend(name1[min_len:])
else:
    mix.extend(name2[min_len:])

num = [strokes[c] for c in mix]

while len(num)>2:
    num =[(num[i] + num[i+1]) % 10 for i in range(len(num)-1)]

if num[0] == 0:
    print(f"{num[1]}%")
else:
    print(f"{num[0]}{num[1]}%") 