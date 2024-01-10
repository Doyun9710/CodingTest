import sys
x, y, w, h = map(int, sys.stdin.readline().split())
# x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))