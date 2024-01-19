import sys
# 탑
n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))

# case 1
stack = []
answer = [0 for i in range(n)]
for i in range(n):
    t = tower[i]
    while stack and tower[stack[-1]] < t:
        stack.pop()
    if stack:
        answer[i] = stack[-1] + 1
    stack.append(i)
print(*answer)


# case 2
stack = [[tower[-1],n-1]]
ans = [0 for i in range(n)]
for i in range(len(tower)-2,-1,-1):
    check = True
    while stack:
        if stack[-1][0] <= tower[i]:
            pp = stack.pop(-1)
            ans[pp[1]] = i + 1
        else:
            stack.append([tower[i],i])
            check = False
            break
    if check:
        stack.append([tower[i], i])
for i in range(0,len(ans)-1):
    print(ans[i],end=" ")
print(ans[len(ans)-1])



# 시간 초과
# import sys

# n = int(sys.stdin.readline())
# toplist = list(map(int, sys.stdin.readline().split()))
# stack = [0 for i in range(n)]

# for i in range(n-1, 0, -1):
#     p = i - 1
#     while p > -1:
#         if toplist[i] < toplist[p]:
#             stack[i] = p+1
#             break
#         else:
#             p -= 1
# print(*stack)