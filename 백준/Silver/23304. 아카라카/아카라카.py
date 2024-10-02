import sys
input = sys.stdin.readline

s = input().strip()

def akaraka(string):
    if len(string) == 1:
        return True
    else: 
        if string != string[::-1]:
            return False
        half = len(string)//2
        left = string[: half]
        return akaraka(left)


if akaraka(s):
    print("AKARAKA")
else:
    print("IPSELENTI")