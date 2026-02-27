import bisect
import os


with open ("D:\Lichess Games Feb 2017\lichess_db_standard_rated_2017-02.pgn") as database:
    output = []
    for line in database.readlines():
        if line[:3] == '1. ':
            output.append(line)

    sorted_output = sorted(output)

with open ("D:\Lichess Games Feb 2017\lichess_milanrad_2026-02-26_WHITE.pgn") as played_white:
    personalDBwhite = []
    for line in played_white.readlines():
        if line[:3] == '1. ':
            personalDBwhite.append(line)

with open ("D:\Lichess Games Feb 2017\lichess_milanrad_2026-02-26_BLACK.pgn") as played_black:
    personalDBblack = []
    for line in played_black.readlines():
        if line[:3] == '1. ':
            personalDBblack.append(line)

Wins = 0
Losses = 0 
Draws = 0

DevWins = 0 
DevLosses = 0
DevDraws = 0

noDevWins = 0
noDevLosses = 0
noDevDraws = 0

for game in personalDBwhite:
    i = bisect.bisect_left(sorted_output,game)
    prefix = os.path.commonprefix([game,sorted_output[i]])
    if len(os.path.commonprefix([game,sorted_output[i]])) < len(os.path.commonprefix([game,sorted_output[i-1]])):
        i -= 1
        prefix = os.path.commonprefix([game,sorted_output[i]])

    result = game.rsplit(None, 1)[-1]

    lengthDiscretePlys = prefix.rfind(' ')
    prefix = prefix[:lengthDiscretePlys]

    tempSplit = prefix.split()
    if len(tempSplit) % 3 == 2:
        #print('black to move')
        if result == "1-0":
            Wins += 1
            noDevWins += 1 #since we are playing white, whites last move was found in DB, blacks next move was not, black deviated first
        elif result == '1/2-1/2':
            Draws += 1
            noDevDraws += 1
        else:
            Losses += 1
            noDevLosses += 1
    else:
        #print('white to move')
        if result == "1-0":
            Wins += 1
            DevWins += 1 #since we are playing white, blacks last move was in DB, whites next was not, white deviated first
        elif result == '1/2-1/2':
            Draws += 1
            DevDraws += 1
        else:
            Losses += 1
            DevLosses += 1


print(f'Wins: {Wins}, Losses: {Losses}, Draws: {Draws}. Wins: {Wins/(Wins+Losses+Draws):.2f}, Losses: {Losses/(Wins+Losses+Draws):.2f}, Draws: {Draws/(Wins+Losses+Draws):.2f}')
print(f"When Deviating first: Wins: {DevWins}, Losses: {DevLosses}, Draws: {DevDraws}. Wins: {DevWins/(DevWins+DevLosses+DevDraws):.2f}, Losses: {DevLosses/(DevWins+DevLosses+DevDraws):.2f}, Draws: {DevDraws/(DevWins+DevLosses+DevDraws):.2f} ")
print(f"When not Deviating first: Wins: {noDevWins}, Losses: {noDevLosses}, Draws: {noDevDraws}. Wins: {noDevWins/(noDevWins+noDevLosses+noDevDraws):.2f}, Losses: {noDevLosses/(noDevWins+noDevLosses+noDevDraws):.2f}, Draws: {noDevDraws/(noDevWins+noDevLosses+noDevDraws):.2f}  ")







Wins = 0
Losses = 0 
Draws = 0

DevWins = 0 
DevLosses = 0
DevDraws = 0

noDevWins = 0
noDevLosses = 0
noDevDraws = 0




for game in personalDBblack:
    i = bisect.bisect_left(sorted_output,game)
    prefix = os.path.commonprefix([game,sorted_output[i]])
    if len(os.path.commonprefix([game,sorted_output[i]])) < len(os.path.commonprefix([game,sorted_output[i-1]])):
        i -= 1
        prefix = os.path.commonprefix([game,sorted_output[i]])

    result = game.rsplit(None, 1)[-1]

    lengthDiscretePlys = prefix.rfind(' ')
    prefix = prefix[:lengthDiscretePlys]

    tempSplit = prefix.split()
    if len(tempSplit) % 3 == 2:
        #print('black to move')
        if result == "1-0":
            Losses += 1
            DevLosses += 1 #since we are playing black, whites last move was found in DB, blacks next move was not, black deviated first
        elif result == '1/2-1/2':
            Draws += 1
            DevDraws += 1
        else:
            Wins += 1
            DevWins += 1
    else:
        #print('white to move')
        if result == "1-0":
            Losses += 1
            noDevLosses += 1 #since we are playing black, blacks last move was in DB, whites next was not, white deviated first
        elif result == '1/2-1/2':
            Draws += 1
            noDevDraws += 1
        else:
            Wins += 1
            noDevWins += 1





print(f'Wins: {Wins}, Losses: {Losses}, Draws: {Draws}. Wins: {Wins/(Wins+Losses+Draws):.2f}, Losses: {Losses/(Wins+Losses+Draws):.2f}, Draws: {Draws/(Wins+Losses+Draws):.2f}')
print(f"When Deviating first: Wins: {DevWins}, Losses: {DevLosses}, Draws: {DevDraws}. Wins: {DevWins/(DevWins+DevLosses+DevDraws):.2f}, Losses: {DevLosses/(DevWins+DevLosses+DevDraws):.2f}, Draws: {DevDraws/(DevWins+DevLosses+DevDraws):.2f} ")
print(f"When not Deviating first: Wins: {noDevWins}, Losses: {noDevLosses}, Draws: {noDevDraws}. Wins: {noDevWins/(noDevWins+noDevLosses+noDevDraws):.2f}, Losses: {noDevLosses/(noDevWins+noDevLosses+noDevDraws):.2f}, Draws: {noDevDraws/(noDevWins+noDevLosses+noDevDraws):.2f}  ")

