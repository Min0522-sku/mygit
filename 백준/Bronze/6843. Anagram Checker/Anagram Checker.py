a = input().replace(" ", "")
b = input().replace(" ", "")
if sorted(a) == sorted(b):
    print("Is an anagram.")
else:
    print("Is not an anagram.")