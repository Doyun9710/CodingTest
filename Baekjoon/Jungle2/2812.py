import sys

n, k = list(map(int, sys.stdin.readline().split()))
str = sys.stdin.readline().rstrip()
# strlist = list(str)
# strlist.pop()
numlist = list(map(int, str))
stack = []

# while k > 0:
for num in numlist:
    while stack and k > 0 and stack[-1] < num:
        stack.pop()
        k -= 1
    stack.append(num)

    # print(stack)

if k > 0:   # 뻐킹!
    for i in stack[:-k]:
        print(i, end='')
else:
    for i in stack:
        print(i, end='')






































# def findmax(list, p, k):
#     # if (k-p) == 1:
#     #     if len(list) > p+1:
#     #         return max(list[p+1:p+2])
#     #     else:
#     #         return max(list[p+1])

#     klist = list[p:k]
#     maxnum = max(klist)
#     return maxnum

# def findnum(p, k, m):
#     global strlist
#     for i in range(len(strlist)):
#         if strlist[p] == m:
#             p += 1
#             k -= (i+1)
#             break
#         else:
#             del strlist[p]
#     return p, k

# n, k = list(map(int, sys.stdin.readline().split()))
# str = sys.stdin.readline()
# # k += 1
# strlist = list(str)
# strlist.pop()
# strlist = list(map(int, strlist))

# # 처음부터 k까지 list0보다 큰 숫자가 있다면 거기까지 자르기
# # k - 자른 길이 > 0 라면 반복
# p = 0
# # klist = strlist[p:k]
# while k > 0:
#     if k == 1:
#         if (p+1) == (len(strlist)):
#             if strlist[p] < strlist[p+1]:
#                 del strlist[p]
#             else:
#                 del strlist[p+1]
#         else:
#             if strlist[p+1] < strlist[p+2]:
#                 del strlist[p+1]
#             else:
#                 del strlist[p+2]
#         break
            
#     maxnum = findmax(strlist, p, p+k)
#     p, k = findnum(p, k, maxnum)
#     # for i in range(cut):
#     #     del strlist[p+1]
# print(*strlist)