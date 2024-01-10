

# case 2
# def checkPrimeNum(num1, num2):
#     for i in range(n):
#         if num1 > 1 and num2 > 1:
#             for j in range(2, num2):
#                 if num1 % j == 0 or num2 % j == 0:
#                     return False
#                 else:
#                     return True
#         else:
#             return False

# n = int(input())
# numlist = []
# answer = []

# for i in range(n):
#     x = int(input())
#     numlist.append(x)

#     for j in range(2, numlist[i]):
#         if checkPrimeNum(j, (numlist[i]-j)):
#             if j <= (numlist[i]-j):
#                 answer.append(j)
#                 answer.append(numlist[i]-j)
#     print(len(answer)-2, len(answer)-1)



# case 1
# def checkPrimeNum(num):
#     for i in range(n):
#         if num > 1:
#             for j in range(2, num):
#                 if num % j == 0:
#                     return False
#                 else:
#                     return True
#         else:
#             return False

# n = int(sys.stdin.readline())
# numlist = []
# answer = []

# for i in range(n):
#     x = int(sys.stdin.readline())
#     numlist.append(x)

#     for j in range(2, numlist[i]):
#         if checkPrimeNum(j):
#             if checkPrimeNum((numlist[i]-j)):
#                 if j <= (numlist[i]-j):
#                     answer.append(j)
#                     answer.append(numlist[i]-j)
#     a = len(answer)
#     print(answer[a-2], answer[a-1])
