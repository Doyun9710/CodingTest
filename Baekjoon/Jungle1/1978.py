import sys, math

n = int(sys.stdin.readline())
numlist = [*map(int, sys.stdin.readline().split())]
checknumlist = []

for i in range(n):
    check = 0
    if numlist[i] > 1:
        for j in range(2, numlist[i]):
            if numlist[i] % j == 0:
                check = 1
                # print(numlist[i])
        if check == 0:
            checknumlist.append(numlist[i])
# print(checknumlist)
print(len(list(set(checknumlist))))


# print(checknumlist)

# 직접 나누기
# 직접 나누기 (Trial Division)는
# 소수판별법 중에서 가장 간단한 예시로,
# 어떤 수 N의 양의 제곱근(=N**(1/2)) 이하의 수들로 N을 나눠서
# 한 번이라도 나누어떨어지면 합성수,
# 아니면 소수라고 판정하는 방법이다.
