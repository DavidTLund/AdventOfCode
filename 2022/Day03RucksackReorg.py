import os
script_dir = os.path.dirname(__file__)
data_file = os.path.join(script_dir, "Data/Day03.txt")

def splitRuckSack(rucsack):
    rucsack = rucsack.rstrip()
    chs = list(rucsack)
    l1 = int(len(chs)/2)
    r0 = int(len(chs)/2)
    r1 = int(len(chs))
    l = chs[0:l1]
    r = chs[r0:r1]
    return [l, r]

def findCommonChInRow(l, r):
    for ch in l:
        if ch in r:
            return ch

def scoreLetter(ch):
    if ch == None:
        return 0
    if ch.islower():
        return ord(ch) - ord('a') + 1
    return ord(ch) - ord('A') + 27

def getData():
    with open(data_file) as f:
        alltext =f.read()
        rucksacks = alltext.split('\n')
        return rucksacks

def main_part1():
    score = 0
    rucksacks = getData()
    for rucksack in rucksacks:
        #print(rucksack)
        rucksack = rucksack.rstrip()
        sides = splitRuckSack(rucksack)
        #print('Rucksack:', rucksack, sides)
        ch = findCommonChInRow(sides[0], sides[1])
        tscore = scoreLetter(ch)
        #print('Letter', ch, tscore)
        score += tscore
    print('Score:', score)

def findCommonChIn3rows(rucksack0, rucksack1, rucksack2):
        r0 = rucksack0.rstrip()
        r1 = rucksack1.rstrip()
        r2 = rucksack2.rstrip()
        for ch in r0:
            if ch in r1:
                if ch in r2:
                    return ch
        return None


def main_part2():
    score = 0
    rucksacks = getData()

    for idx in range(0, len(rucksacks)-1, 3):
        if rucksacks[idx] == None:
            break
        ch = findCommonChIn3rows(rucksacks[idx], rucksacks[idx+1], rucksacks[idx+2])
        tscore = scoreLetter(ch)
        print('Letter', ch, tscore)
        score += tscore
    print('Score:', score)

main_part1()

main_part2()
