import sys
input = sys.stdin.readline

N = int(input())

flist = [0] * (N+1)

flist[0] = 0
flist[1] = 1
for i in range(2, N+1):
    flist[i] = flist[i-2] + flist[i-1]

print(flist[N])