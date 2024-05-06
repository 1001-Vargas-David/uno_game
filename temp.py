


players = [1,2,3,4]

player = players[1]


for x in range(-1,len(players)-1):
    if players[x] == player:
        p = players[x+1]
        
print(p)