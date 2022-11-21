
def GetDimensions(pkg):
    sdims = pkg.split('x')
    #print(sdims)
    dims = []
    for s in sdims:
        dims.append(int(s))
    return dims

def CalcPaper(pkg):
    dims = GetDimensions(pkg)
    #print(dims)
    dims.sort()
    #print(dims)
    return 3*dims[0]*dims[1] + 2*dims[0]*dims[2] + 2*dims[1]*dims[2]

def CalcRibbon(pkg):
    dims = GetDimensions(pkg)
    print(dims)
    dims.sort()
    print(dims)
    return 2*dims[0] + 2*dims[1] + dims[0]*dims[1]*dims[2]

def main():
    data_file= "C:\\work\\AdventOfCode\\2015\\Data\\Day02.txt"

    with open(data_file) as f:
        total_paper = 0
        total_ribbon = 0
        for pkg in f:
            pkg = pkg.rstrip()
            print(pkg)
            paper = CalcPaper(pkg)
            total_paper = total_paper + paper
            total_ribbon = total_ribbon + CalcRibbon(pkg)
            print('Now Total paper:' , total_paper, 'paper:', paper)
        print('Total paper needed:' , total_paper)
        print('Total ribbon needed:' , total_ribbon)
        

main()
pkg = '2x3x4'
#paper = CalcPaper(pkg)
#paper = CalcRibbon(pkg)
#print(paper)
pkg2 ='1x1x10'
#print(CalcRibbon(pkg2))

