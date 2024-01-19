import sys

t = int(sys.stdin.readline())

for i in range(t):
    num, s = sys.stdin.readline().split()
    answer = ''

    for i in s:
        answer += int(num) * i
    print(answer)