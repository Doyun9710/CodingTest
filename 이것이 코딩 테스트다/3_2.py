# 큰 수의 법칙

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
nlist = list(map(int, input().split()))
# print(N, M, K, nlist)

nlist.sort()
# print(nlist)
big1 = nlist[N-1]
big2 = nlist[N-2]

sum = 0
sum += (M // (K + 1)) * ((K * big1) + big2)
sum += (M % (K + 1)) * big1

print(sum)



''' input
5 8 3
2 4 5 4 6
'''