import sys

year = int(sys.stdin.readline())

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0: print(1)
        else: print(0)
    else: print(1)
else: print(0)


# 6/7크기지만 속도가 같다
# year = int(input())
# if year%4 == 0:
#     if year%100 == 0:
#         if year%400 == 0: print(1)
#         else: print(0)
#     else: print(1)
# else: print(0)