first = input()             
N = int(input())            

current_owner = first       
history = set([first])      

for _ in range(N):
    winner, loser = input().split()
    if loser == current_owner:
        current_owner = winner
        history.add(winner)

print(current_owner)
print(len(history))