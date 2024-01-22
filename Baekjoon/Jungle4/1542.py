import sys
input = sys.stdin.readline

math = input().split('-')


subnumlist = []
for i in math:
    cnt = 0
    addnumlist = i.split('+')
    for j in addnumlist:
        cnt += int(j)
    subnumlist.append(cnt)


answer = subnumlist[0]
for i in range(1, len(subnumlist)):
    answer -= subnumlist[i]

print(answer)