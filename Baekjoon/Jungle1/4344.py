import sys

n = int(sys.stdin.readline())

for i in range(n):
    sum = 0
    listlen = 0
    passstudent = 0

    classscore = [*map(int, sys.stdin.readline().split())]
    lenstudent = len(classscore) - 1

    for j in range(lenstudent):
        sum += classscore[j+1]

    avg = sum / lenstudent

    for j in range(lenstudent):
        if classscore[j+1] > avg:
            passstudent += 1

    passper = format((passstudent*100/lenstudent), ".3f")
    print(passper, '%', sep = "")