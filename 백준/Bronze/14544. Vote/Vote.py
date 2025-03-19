P = int(input().strip())
for i in range(1,P+1):
    n, m = map(int,input().split())
    l = [input().strip() for _ in range(n)]
    vote_dict = {name: 0 for name in l}
    for _ in range(m):
        name, result, center = input().split()
        result = int(result)
        if name in vote_dict:
            vote_dict[name] += result
    max_votes = max(vote_dict.values())
    winner = [name for name, votes in vote_dict.items() if votes == max_votes]
    if len(winner) == 1:
        print(f"VOTE {i}: THE WINNER IS {winner[0]} {max_votes}")
    else:
        print(f"VOTE {i}: THERE IS A DILEMMA")