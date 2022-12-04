import os
script_dir = os.path.dirname(__file__)
data_file = os.path.join(script_dir, "Data/Day02.txt")

def pointsForResult(player1, player2):
    #print('P1:', player1, ', P2:', player2)
    if player1 == 'A':
        if (player2 == 'X'):
            # rock - rock tie
            return 1 + 3
        elif (player2 == 'Y'):
            # rock - paper win
            return 2 + 6
        elif (player2 == 'Z'):
            # rock - scissor loss
            return 3 + 0
    elif player1 == 'B':
        if (player2 == 'X'):
            # paper - rock loss
            return 1 + 0
        elif (player2 == 'Y'):
            # paper - paper tie
            return 2 + 3
        elif (player2 == 'Z'):
            # paper - scissor win
            return 3 + 6
    elif player1 == 'C':
        if (player2 == 'X'):
            # scissor - rock win
            return 1 + 6
        elif (player2 == 'Y'):
            # scissor - paper loss
            return 2 + 0
        elif (player2 == 'Z'):
            # scissor - scissor tie
            return 3 + 3
    return 0

def pointsForAdjustedResult(player1, player2):
    #print('P1:', player1, ', P2:', player2)
    if player1 == 'A':
        if (player2 == 'X'):
            # rock - scissor lose
            return 3 + 0
        elif (player2 == 'Y'):
            # rock - rock tie
            return 1 + 3
        elif (player2 == 'Z'):
            # rock - paper win
            return 2 + 6
    elif player1 == 'B':
        if (player2 == 'X'):
            # paper - rock loss
            return 1 + 0
        elif (player2 == 'Y'):
            # paper - paper tie
            return 2 + 3
        elif (player2 == 'Z'):
            # paper - scissor win
            return 3 + 6
    elif player1 == 'C':
        if (player2 == 'X'):
            # scissor - paper loss
            return 2 + 0
        elif (player2 == 'Y'):
            # scissor - scissor tie
            return 3 + 3
        elif (player2 == 'Z'):
            # scissor - rock win
            return 1 + 6
    return 0

def main_part1():
    score = 0
    with open(data_file) as f:
        for item in f:
            vals =item.rstrip().split(' ')
            #print('Item:', item, vals)
            now = pointsForResult(vals[0], vals[1])
            #print('Now:', now)
            score += now

    print('Part 1 score:', score)

def main_part2():
    score = 0
    with open(data_file) as f:
        for item in f:
            vals =item.rstrip().split(' ')
            #print('Item:', item, vals)
            now = pointsForAdjustedResult(vals[0], vals[1])
            #print('Now:', now)
            score += now

    print('Part 2 score:', score)

main_part1()

main_part2()
