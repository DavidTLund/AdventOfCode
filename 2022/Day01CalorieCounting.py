data_file= "C:\\work\\AdventOfCode\\2022\\Data\\Day01.txt"

elves = {}
elf = 1
elves[elf] = 0
with open(data_file) as f:
    for item in f:
        item = item.rstrip()
        if item == "":
            elf += 1
            elves[elf] = 0
        else:
            elves[elf] += int(item)

maxCals = max(elves, key=elves.get)
print('Max calories elf is', maxCals, 'value is:', elves[maxCals])
max3 = sorted(elves, key=elves.get, reverse=True)[:3]
print(max3)
sumCals3 = 0
for idx in max3:
    sumCals3 += elves[idx]

print('Sum top 3 elves calories:', sumCals3)
