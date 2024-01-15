import sys

n = sys.stdin.readline()
N = sorted(map(int, sys.stdin.readline().split()))
m = sys.stdin.readline()
M = map(int, sys.stdin.readline().split())

# 값이 크다 => 중간보다 윗부분에서 탐색
# 값이 작다 => 중간보다 작은 부분에서 탐색
# 위 과정을 확인할 리스트가 없을 때까지 계속해서 반복


def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)


for l in M:
    start = 0
    end = len(N)-1
    print(binary(l, N, start, end))
