
def CalcFloor(directions):
    floor = 0
    for ch in directions:
        if ch== '(':
            floor = floor + 1
        elif ch == ')':
            floor = floor - 1
        #else:
    return floor

directions = '()()'
floor = CalcFloor(directions)
print('The directions', directions, 'go to floor', floor, '.')
