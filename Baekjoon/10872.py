import sys

def factNum(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factNum(num-1)
        
n = int(sys.stdin.readline())
a = factNum(n)

print(a)