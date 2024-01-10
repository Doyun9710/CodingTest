import sys

def factorialscore(num):
    if num > 1:
        factorialscore(num-1)
        return num
    else:
        return 1

n = int(sys.stdin.readline())

for i in range(n):
    arrnum = list(sys.stdin.readline())
    re = 0
    score = 0

    for j in range(len(arrnum)):
        if arrnum[j] == "O":
            re += 1
            score += factorialscore(re)
        else:
            re = 0

    print(score)