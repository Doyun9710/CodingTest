import sys
input = sys.stdin.readline

N = int(input())
# N+1 은 왜 오류???
# 11번째 줄 flist 에서 2번째 공간을 지정했기 때문! N=1일 때 오류!
# flist = [0] * (N+1)
flist = [0] * (N+2)

flist[1] = 1
flist[2] = 2
'''
flist[3] = 3    # 001 100 111
flist[4] = 5    # 0000 0011 1001 1100 1111
flist[5] = 8    # 00001 00100 10000 00111 10011 11001 11100 11111
'''

# if N == 1 or N == 2:
#     print(N)
# else:
#     for i in range(3, N+1):
#         flist[i] = (flist[i-2] + flist[i-1]) % 15746
#     print(flist[N])

for i in range(3, N+1):
    flist[i] = (flist[i-2] + flist[i-1]) % 15746

print(flist[N])

# 메모리초과!!!
# print(flist[N]%15746)