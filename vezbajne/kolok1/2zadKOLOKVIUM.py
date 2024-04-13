from constraint import *

def myFun(*satori):
    moves = ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1))
    for sator in satori:
        if sator[0] not in range(6) or sator[1] not in range(6):
            return False
        for move in moves:
            sosed = (sator[0] + move[0], sator[1] + move[1])
            if sosed in satori:
                return False
    return True

def kolona(*satori):
    br = 0
    for sator in satori:
        x = sator[0]
        for sator1 in satori:
            if sator1 == sator:
                continue
            if sator1[0] == x:
                br += 1
        if br > 1:
            return False
    return True
"""
6
2 2
5 0
4 1
1 3
2 5
4 4

6
0 5
1 5
2 5
3 5
4 5
5 5

1 2
4 0
4 2
1 4
3 5
5 4
"""

if __name__ == '__main__':
    num_drva = int(input())
    drva = []
    for i in range(num_drva):
        drvo = tuple(map(int, input().split(" ")))
        drva.append(drvo)

    problem = Problem()

    moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for drvo in drva:
        dom_drvo = []
        for move in moves:
            dom_drvo.append((drvo[0] + move[0], drvo[1] + move[1]))
        problem.addVariable(drvo, dom_drvo)

    problem.addConstraint(AllDifferentConstraint(), drva)
    problem.addConstraint(myFun, drva)
    problem.addConstraint(kolona, drva)

    res = problem.getSolution()
    if res:
        for drvo in drva:
            print(str(res[drvo][0]) + " " + str(res[drvo][1]))
    else:
        print("No solution exists")