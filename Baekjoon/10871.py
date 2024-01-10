import sys

n, x = map(int, sys.stdin.readline().split())
li = [*map(int, sys.stdin.readline().split())]

for i in range(n):
    if li[i] < x:
        print(li[i])

# 정수 배열 입력받기
# https://bio-info.tistory.com/157#2)_%ED%95%9C_%EC%A4%84%EC%9D%98_%EC%97%AC%EB%9F%AC_%EC%A0%95%EC%88%98_%EC%9E%85%EB%A0%A5%EB%B0%9B%EA%B8%B0_-_%EB%A6%AC%EC%8A%A4%ED%8A%B8%EB%A1%9C
