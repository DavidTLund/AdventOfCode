
def CalcFloor(directions):
    floor = 0
    for ch in directions:
        if ch== '(':
            floor = floor + 1
        elif ch == ')':
            floor = floor - 1
        #else:
    return floor

def FirstToBasement(directions):
    floor = 0
    ipos = 0
    for ch in directions:
        if ch== '(':
            floor = floor + 1
        elif ch == ')':
            floor = floor - 1
        ipos = ipos + 1
        #else:
        if floor == -1:
            return ipos
    return 0

#puzzle_directions = "(((())))()((((((((())()(()))(()((((()(()(((()((()((()(()()()()()))(((()(()((((((((((())(()()((())()(((())))()(()(()((()(()))(()()()()((()((()(((()()(((((((()()())()((((()()(((((()(())()(())((())()()))()(((((((())(()())(()(((())(()))((())))(()((()())))()())((((())))(()(((((()(())(((()()((()((()((((((((((())(()())))))()))())()()((((()()()()()()((((((())())(((()())()((()()(((()()()))(((((()))(((()(()()()(()(()(((())()))(()(((()((())()(()())())))((()()()(()()(((()))(((()((((()(((((()()(()())((()())())(()((((((()(()()))((((()))))())((())()()((()(()))))((((((((()))(()()(((())())(())()((()()()()((()((()((()()(((())))(()((())()((((((((()((()(()()(((())())())))(())())))()((((()))))))())))()()))()())((()())()((()()()))(()()(((()(())((((())())((((((((()()()()())))()()()((((()()))))))()((((()(((()))(()()())))((()()(((()))()()())())(((())((()()(())()()()(((())))))()())((()))()))((())()()())()())()()(()))())))())()))(())((()(())))(()(())(()))))(()(())())(()(())(()(()))))((()())()))()((((()()))))())))()()())((())()((()()()))()(((()(()))))(())()()))(((()())))))))))(((())))()))())()))))()()(((())))))))()(()()(()))((()))))((())))((()((())))())))()()(()))())()(()((()())(()(()()())())(()()))()))))(()())()()))()()()()))(()(()(()))))))()(()))()))()()(()((())(()(())))()(((())(())())))))()(()(()))))()))(()()()(())()(()(())))()))))()()(((((())))))())()())())())()())()))))()))))))))())()()()()()()())))()))((())()))())))()((())()))))()))())))))))())()()()))()()(()((((()(((((((()(())((()())((()()))()))))(())))()()()(())((())()())))(())))(())))(((()()))()(())(((()(()))((())))())()))((((()))())()))))))))()(())())))(()))()(()()))())()()(())())))())()()(()())))()((()())(()(())(())))))))))))))(()))))()))))))()()())(()(((((()(()())))())()))(()))()))(()()))()())(()))())()(())((()()))))))())))())()(((())))(()(()))()()))()(()))))))((()())(()))))))()())))()()))))))))((((((((()()()(()))))))()())))())))()()((())()))((())(())))())())))()()()((()((()(())))())()(())))))))))()())))()()()()()()))()))((())())(()(()))))))(()()))()))(())))()))))))))))))(()))))))))()))))()))()())()))()()))))))()))))((()))))(()))())()(())))(()())((((()())))()))))(()))()(()()(())))))())))))()))))))())))())))))())))())())))())(()))))(())()(())))())()))((()()))))))())))((())))))))())))(())))))()()())))))())))))()))))))()))()()()(()(((()())())())(()))())))))((()(())(()))))))))(())))()()()())())(()))))()()()))()))())())())()(())))()(((()((((())))))))()))))))))))))))))))))((())()())(()))))()()))))))(()()(())())))())))((())))((())))))))))))))()))))()(()))))))())))))()))(()()())(()())))))))))()))))))(())))))()()))()())(((())))()))(()))))))))(())())))())))())())())()()))((())()(())()())()))()())(())(()))))()())))(()(((()))))))()(()())()()()))()))))))))()()()(())()())()(((((()))()())())(()))))()()()(())))())))()((()())))(()))())()(()())())(()))()()))((()()))((()()()()())))(())()))(()(())))((()()))))))))())))))))())()()))))))))))))))))(())()(())(())()())())()))()(()))))())())))))()())()(()))()()(())))(())())))))(()))))))))))))))())())(())(())))(((()))()))))())((())(()))())))))))())))))())))()))()))))))))))))())()))))()))))((()))(())))()(())))(())()))()))())))())))))))()(()())())))()()())))(())))))(()))))))))))))(()))()))()))())))(((()()()(())((()())))()())(((()))(())()))((()()()())))())(())(()))))()(((((())))(()))())())))))))((((()()()))())())()(()(()())))))))))()())())))(())))()())(((()(())())()()))())())))))))((()())((()()(()))(()(())))()))()))(()))(()))()()(()(((())((((()))()(()))((())()(()(()())()(()))()())))))(()))()))())()())))())))(())))((())(()())))))()))(())(()))()())()(()()((()(()))))))()(())(()())(())()))(((())()))(()()(()()()))))(()(())))()))))())))))())(()()()()()()(((())))(()()))()((())(((((()()())))(()))(()))()()))(((())())()(((()()()()))))(()))(())())))()())(()()())())))))))()))))((())))()())(()))(()(()))())))))())(())))))()()())())()))()()(())))(()))(())((((((())(()))(()))())()))(()()(())))()))(()()))()))()(())))(())))((()(()))(())()()())())))(((()()())(())()))))))()(((()(((((()()(((())(())))())()((()))))((()())()(())(((())))(((()((()(()(()))(()()))())(()))(())(())))()))))))((((()))()((((()(()))()))()()))))()(()(()))()(()((()(((()(()()(((()))))()(((()(()(()(((()(()())())()()(()(()())())(()((((())(()))()))(((((()()())(())()((()()())))()()(((()()))()((((((((()(())))())((()))))(())))(()))))((()((((()()(())(((((()))(((((((((((((()())))((((()(((()((())())()))((()))()(()()((()()()()(()()(()(()(((())()(()((((((()((()()((())()((((()((()()(()()())((()()()((()((())()(()(((()((())((((())(()))((()(()))(()())()((((((((()(((((((((((()))(()(((()(()()()((((())((())()())()))(())((())(()))(((()((()(())))(()))))((()()))))((((()(()(()())(()(())((((((((()((((()((()(((((()))())()(()))(()()((()(())(((((()(())()(((((()()))))))()(((())()(()()((((())()((())((()(((())(((()))((()()((((()(())))))((()((((()((()((()(((())((()))(((((((()(((()((((((((())()))((((())(((((()((((((((()(((()((()(((()()(((()((((((()()(()((((((((()()(()(()(())((((()())()))))(((()))((((())((((()())((()(())()((()((((((()((((((()(())))()())(((())())())()(())()(()())((()()((((())((((((())(()(((((()((((())()((((()(()(())(()())(((())()((())((((()))()((((((())(()(((()(((()((((((()(((()))(()()())())((()((()())()((((())(((()(()(((((((((())(())))()((()()()()(())((()))(((((((()(((((((((()(()))))(()((((((((()((((()((()()((((((()()(((((((()(()(())()(())((()()()((()(((((()())()(((((()())()()((()(()())(()()()(((()()(((((()((((((()()((()(()()()((((((((((((()((((((((()()(((()())))()(((()()(())())((((()((((()((((()()()(())(())((()(()(((((((((((((((()(())(())))))()()))((()(((()(())((()(((()(()()((((()()(((()(((()(((((()()((()(()(((()))((((((()((((((((()((()((())(((((()(((())(())())((()()))((((())()()((()(((()(((((()()(((()))(((()(()(((((((((((((()))((((((((()(((()))))())((((((((((((())((())((()())(((())((())(()((((((((((()(((())((()()(()((())(((((((((((()))((((((((((((()(()())((()((()((()(()(((()((((((((()()(()((()(()(((()))((()))(((((((((((((()(())((((((())(((()(())(()(()(()((()()))((((()((((()((((())))())((((()((((()))((((((()((((((()((()(((())))((())(()))(()((()((((()((()(((()()))((((()()()(((((((())(((())(()))())((((()())(((()(((((((((((()(()(()((()(((((((((((((((()()((((()((((((((()(((()()((()((((()))(((()(())((((((()((((())()((((()((()))(())()(()(((()((())())((((((()(()(())())(((())(()(()())(((((()((()((())()())(())))(((()(())))))))(((()(((()))()((()(((()()((()())()()))())))(((()))(()(((()(((((((((()(()(((((()()(((()())()()))))()(((()))(((()(()(()(()(()))()(())()))(()(((())))(()))))))))))(())((()((())((()(())()(())((()()((((()()((()()))((())(((()((()(())(())))()(()(((((()((()))())()(((((()()(((()(()((((((())(()))(())()))((()(()()))(())())()))(((())))(()((()(((())(())())))((()()((((((((((((((()((()(()()(()(((()))())()()((()()()(())(()))(()())(((())((())()(())()()(()()(())))((()(((()))))(((()()(()()))())((()((())()))((((()()()())((())))(((()(())(((((()(((((()((()(()((((()()(((()()()(((()())(((()()((((())(()))(((()))(())())((()))(((()((()))(((()()((())((()(((((()((((()()())((()))()((((()((()(()()()("

directions = '()()'
floor = CalcFloor(directions)
print('The directions', directions, 'go to floor', floor, '.')
directions = '))((((('
floor = CalcFloor(directions)
print('The directions', directions, 'go to floor', floor, '.')

puzzledirections = '(((())))()((((((((())()(()))(()((((()(()(((()((()((()(()()()()()))(((()(()((((((((((())(()()((())()(((())))()(()(()((()(()))(()()()()((()((()(((()()(((((((()()())()((((()()(((((()(())()(())((())()()))()(((((((())(()())(()(((())(()))((())))(()((()())))()())((((())))(()(((((()(())(((()()((()((()((((((((((())(()())))))()))())()()((((()()()()()()((((((())())(((()())()((()()(((()()()))(((((()))(((()(()()()(()(()(((())()))(()(((()((())()(()())())))((()()()(()()(((()))(((()((((()(((((()()(()())((()())())(()((((((()(()()))((((()))))())((())()()((()(()))))((((((((()))(()()(((())())(())()((()()()()((()((()((()()(((())))(()((())()((((((((()((()(()()(((())())())))(())())))()((((()))))))())))()()))()())((()())()((()()()))(()()(((()(())((((())())((((((((()()()()())))()()()((((()()))))))()((((()(((()))(()()())))((()()(((()))()()())())(((())((()()(())()()()(((())))))()())((()))()))((())()()())()())()()(()))())))())()))(())((()(())))(()(())(()))))(()(())())(()(())(()(()))))((()())()))()((((()()))))())))()()())((())()((()()()))()(((()(()))))(())()()))(((()())))))))))(((())))()))())()))))()()(((())))))))()(()()(()))((()))))((())))((()((())))())))()()(()))())()(()((()())(()(()()())())(()()))()))))(()())()()))()()()()))(()(()(()))))))()(()))()))()()(()((())(()(())))()(((())(())())))))()(()(()))))()))(()()()(())()(()(())))()))))()()(((((())))))())()())())())()())()))))()))))))))())()()()()()()())))()))((())()))())))()((())()))))()))())))))))())()()()))()()(()((((()(((((((()(())((()())((()()))()))))(())))()()()(())((())()())))(())))(())))(((()()))()(())(((()(()))((())))())()))((((()))())()))))))))()(())())))(()))()(()()))())()()(())())))())()()(()())))()((()())(()(())(())))))))))))))(()))))()))))))()()())(()(((((()(()())))())()))(()))()))(()()))()())(()))())()(())((()()))))))())))())()(((())))(()(()))()()))()(()))))))((()())(()))))))()())))()()))))))))((((((((()()()(()))))))()())))())))()()((())()))((())(())))())())))()()()((()((()(())))())()(())))))))))()())))()()()()()()))()))((())())(()(()))))))(()()))()))(())))()))))))))))))(()))))))))()))))()))()())()))()()))))))()))))((()))))(()))())()(())))(()())((((()())))()))))(()))()(()()(())))))())))))()))))))())))())))))())))())())))())(()))))(())()(())))())()))((()()))))))())))((())))))))())))(())))))()()())))))())))))()))))))()))()()()(()(((()())())())(()))())))))((()(())(()))))))))(())))()()()())())(()))))()()()))()))())())())()(())))()(((()((((())))))))()))))))))))))))))))))((())()())(()))))()()))))))(()()(())())))())))((())))((())))))))))))))()))))()(()))))))())))))()))(()()())(()())))))))))()))))))(())))))()()))()())(((())))()))(()))))))))(())())))())))())())())()()))((())()(())()())()))()())(())(()))))()())))(()(((()))))))()(()())()()()))()))))))))()()()(())()())()(((((()))()())())(()))))()()()(())))())))()((()())))(()))())()(()())())(()))()()))((()()))((()()()()())))(())()))(()(())))((()()))))))))())))))))())()()))))))))))))))))(())()(())(())()())())()))()(()))))())())))))()())()(()))()()(())))(())())))))(()))))))))))))))())())(())(())))(((()))()))))())((())(()))())))))))())))))())))()))()))))))))))))())()))))()))))((()))(())))()(())))(())()))()))())))())))))))()(()())())))()()())))(())))))(()))))))))))))(()))()))()))())))(((()()()(())((()())))()())(((()))(())()))((()()()())))())(())(()))))()(((((())))(()))())())))))))((((()()()))())())()(()(()())))))))))()())())))(())))()())(((()(())())()()))())())))))))((()())((()()(()))(()(())))()))()))(()))(()))()()(()(((())((((()))()(()))((())()(()(()())()(()))()())))))(()))()))())()())))())))(())))((())(()())))))()))(())(()))()())()(()()((()(()))))))()(())(()())(())()))(((())()))(()()(()()()))))(()(())))()))))())))))())(()()()()()()(((())))(()()))()((())(((((()()())))(()))(()))()()))(((())())()(((()()()()))))(()))(())())))()())(()()())())))))))()))))((())))()())(()))(()(()))())))))())(())))))()()())())()))()()(())))(()))(())((((((())(()))(()))())()))(()()(())))()))(()()))()))()(())))(())))((()(()))(())()()())())))(((()()())(())()))))))()(((()(((((()()(((())(())))())()((()))))((()())()(())(((())))(((()((()(()(()))(()()))())(()))(())(())))()))))))((((()))()((((()(()))()))()()))))()(()(()))()(()((()(((()(()()(((()))))()(((()(()(()(((()(()())())()()(()(()())())(()((((())(()))()))(((((()()())(())()((()()())))()()(((()()))()((((((((()(())))())((()))))(())))(()))))((()((((()()(())(((((()))(((((((((((((()())))((((()(((()((())())()))((()))()(()()((()()()()(()()(()(()(((())()(()((((((()((()()((())()((((()((()()(()()())((()()()((()((())()(()(((()((())((((())(()))((()(()))(()())()((((((((()(((((((((((()))(()(((()(()()()((((())((())()())()))(())((())(()))(((()((()(())))(()))))((()()))))((((()(()(()())(()(())((((((((()((((()((()(((((()))())()(()))(()()((()(())(((((()(())()(((((()()))))))()(((())()(()()((((())()((())((()(((())(((()))((()()((((()(())))))((()((((()((()((()(((())((()))(((((((()(((()((((((((())()))((((())(((((()((((((((()(((()((()(((()()(((()((((((()()(()((((((((()()(()(()(())((((()())()))))(((()))((((())((((()())((()(())()((()((((((()((((((()(())))()())(((())())())()(())()(()())((()()((((())((((((())(()(((((()((((())()((((()(()(())(()())(((())()((())((((()))()((((((())(()(((()(((()((((((()(((()))(()()())())((()((()())()((((())(((()(()(((((((((())(())))()((()()()()(())((()))(((((((()(((((((((()(()))))(()((((((((()((((()((()()((((((()()(((((((()(()(())()(())((()()()((()(((((()())()(((((()())()()((()(()())(()()()(((()()(((((()((((((()()((()(()()()((((((((((((()((((((((()()(((()())))()(((()()(())())((((()((((()((((()()()(())(())((()(()(((((((((((((((()(())(())))))()()))((()(((()(())((()(((()(()()((((()()(((()(((()(((((()()((()(()(((()))((((((()((((((((()((()((())(((((()(((())(())())((()()))((((())()()((()(((()(((((()()(((()))(((()(()(((((((((((((()))((((((((()(((()))))())((((((((((((())((())((()())(((())((())(()((((((((((()(((())((()()(()((())(((((((((((()))((((((((((((()(()())((()((()((()(()(((()((((((((()()(()((()(()(((()))((()))(((((((((((((()(())((((((())(((()(())(()(()(()((()()))((((()((((()((((())))())((((()((((()))((((((()((((((()((()(((())))((())(()))(()((()((((()((()(((()()))((((()()()(((((((())(((())(()))())((((()())(((()(((((((((((()(()(()((()(((((((((((((((()()((((()((((((((()(((()()((()((((()))(((()(())((((((()((((())()((((()((()))(())()(()(((()((())())((((((()(()(())())(((())(()(()())(((((()((()((())()())(())))(((()(())))))))(((()(((()))()((()(((()()((()())()()))())))(((()))(()(((()(((((((((()(()(((((()()(((()())()()))))()(((()))(((()(()(()(()(()))()(())()))(()(((())))(()))))))))))(())((()((())((()(())()(())((()()((((()()((()()))((())(((()((()(())(())))()(()(((((()((()))())()(((((()()(((()(()((((((())(()))(())()))((()(()()))(())())()))(((())))(()((()(((())(())())))((()()((((((((((((((()((()(()()(()(((()))())()()((()()()(())(()))(()())(((())((())()(())()()(()()(())))((()(((()))))(((()()(()()))())((()((())()))((((()()()())((())))(((()(())(((((()(((((()((()(()((((()()(((()()()(((()())(((()()((((())(()))(((()))(())())((()))(((()((()))(((()()((())((()(((((()((((()()())((()))()((((()((()(()()()('
floor = CalcFloor(puzzledirections)
print('The directions', directions, 'go to floor', floor, '.')

pos = FirstToBasement(puzzledirections)
print('Position', pos)

