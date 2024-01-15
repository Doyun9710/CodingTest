import sys
# 막대기
n = int(sys.stdin.readline())
stack = []
result = 1

for _ in range(n):
    stack.append(int(sys.stdin.readline()))

max = stack[-1]

for i in range(len(stack)-1, -1, -1):
    if stack[i] > max:
        result += 1
        max = stack[i]

print(result)