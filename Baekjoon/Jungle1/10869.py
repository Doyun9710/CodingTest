import sys
a = list(map(int,sys.stdin.readline().split()))
print(a[0]+a[1])
print(a[0]-a[1])
print(a[0]*a[1])
print(a[0]//a[1])
print(a[0]%a[1])

# 3ms 정도 느림
# a, b = map(int, input('').split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)