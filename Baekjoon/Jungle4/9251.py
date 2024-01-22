import sys
input = sys.stdin.readline

str1 = list(map(str, input().strip()))
str2 = list(map(str, input().strip()))

# print(str1, str2)

check = [0] * (len(str1)+1)

for s in str2:
    cnt = 0
    for i in range(len(str1)):
        if cnt < check[i]:
            cnt = check[i]
        elif str1[i] == s:
            check[i] = cnt + 1
        # elif check[i] < cnt:
        #     check[i] = cnt
        # ?????
        # else:
        #     cnt = check[i]

print(max(check))



'''
반례
VREGDFELK
VLSKD

정답 : 3
'''