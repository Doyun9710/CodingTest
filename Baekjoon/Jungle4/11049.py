import sys
input = sys.stdin.readline

N = int(input())
# arr = [0] * (N+1)
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# print(arr)

for f, e in arr:
    pass



'''
입력
5
1 10
10 1
1 10
10 1
1 10

정답
31
'''
'''
입력
4
5 3
3 2
2 6
6 3

정답
96
'''