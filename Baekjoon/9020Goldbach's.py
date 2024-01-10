import sys

numsize = 10000

prime_list = [False, False] + [True] * numsize
for i in range(2, numsize):
    if prime_list[i]:
        for j in range(2 * i, numsize, i):
            prime_list[j] = False

t = int(sys.stdin.readline())       # 문제 수
for i in range(t):
    n = int(sys.stdin.readline())   # 계산할 수 
    a = n // 2

    while a > 1:
        if prime_list[a] and prime_list[n-a]:
            print(a, n-a)
            break
        else:
            a -= 1