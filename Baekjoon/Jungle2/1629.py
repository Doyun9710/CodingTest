import sys
# 지수법칙 : a^(n+m) = a^n * a^m
# 모듈러 성질 : (a*b)%c = (a%c * b%c)%c

def sol(b):
    
    if b == 1:
        return a % c

    abc = sol(b//2)

    if b % 2 == 0:
        return abc * abc % c
    else:
        return abc * abc * a % c


a, b, c = list(map(int, sys.stdin.readline().split()))

result = sol(b)
print(result)
