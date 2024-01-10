import sys

num1, num2 = sys.stdin.readline().split()
# arr[::-1] : 역출력
num1 = int(num1[::-1])
num2 = int(num2[::-1])

if num1 > num2:
    print(num1)
else :
    print(num2)