import re

def is_naughty_phrase(naughty):
    badPhrases = ['ab', 'cd', 'pq', 'xy']
    for phrase in badPhrases:
        if phrase in naughty:
            print('Found', phrase, 'in', naughty)
            return True
    return False

def find_double_letter(phrase):
    prevch=''
    for ch in phrase:
        if ch == prevch:
            print('Found',prevch, ch, 'in', phrase)
            return True
        prevch = ch
    return False

def main():
    data_file= "C:\\work\\AdventOfCode\\2015\\Data\\Day05.txt"

    with open(data_file) as f:
        numNaughty = 0
        for naughty in f:
            naughty = naughty.rstrip()
            print(naughty)
        print('Number of naughty dtrings:' , numNaughty)

#main()
phrase = 'abcdde'
result = find_double_letter(phrase)
print('Has', phrase, 'doubles?', result)

phrase = 'haegwjzuvuyypxyu'
result = is_naughty_phrase(phrase)
print('Is', phrase, 'bad?', result)
