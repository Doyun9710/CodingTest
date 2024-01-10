# 하노이 탑
import sys

N = int(input())

def HANOI(x, y, z, cnt):
    if cnt == 0:
        # print(z,y)
        return

    HANOI(x, z, y, cnt - 1) # N == 홀, 짝? 홀: 패스, 짝: y, z 교환 후 출력. ※ N 홀수 시 z 먼저
    print(x, z)
    HANOI(y, x, z, cnt - 1)

print((1 << N) - 1)
if N <= 20:
    HANOI(1, 2, 3, N)





# case 3
# n = int(sys.stdin.readline())

# a = []
# b = []
# c = []

# def hanoi(n, a, b, c):
#     if n == 1:
#         print(1)
#     elif n == 2:
#         print(3)
#     else:
#         # k = 8
#         k1 = math.pow(2, n)
#         c.append(a.pop())
#         b.append(a.pop())
#         b.append(c.pop())
#         c.append(a.pop())
#         a.append(b.pop())
#         c.append(b.pop())
#         c.append(a.pop())
#         k = int(math.pow(2, 3))
#         # k += int(math.pow(2, 3))
#         # 
#         if k == k1:
#             print(k-1)
#             print(a, c)
#         else:
#             k = int(math.pow(k, 2))
#             b.append(a.pop)
#             hanoi(k, n-3, c, a, b)
#             print(a, c)
#     # print(a, b, c)

# for i in range(n):
#     a.append(n-i)

# answer = hanoi(n, a, b, c)
