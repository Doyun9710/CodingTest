import sys, math

list = [*map(int, sys.stdin.readline().split())]
answer = math.ceil((list[2] - list[0]) / (list[0] - list[1]) + 1)

print(answer)