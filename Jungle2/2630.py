import sys


def recursion(x, y, n):
    global w, b
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                recursion(x, y, n//2)
                recursion(x+n//2, y, n//2)
                recursion(x, y+n//2, n//2)
                recursion(x+n//2, y+n//2, n//2)
                return
                # break
            # else:
            #     if color == 0:
            #         w += 1
            #     else:
            #         b += 1
    if color == 0:
        w += 1
    else:
        b += 1


n = int(sys.stdin.readline())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# arr = [0 for _ in range(n)]
# for i in range(n):
#     arr[i] = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
# print(arr)
w = 0
b = 0

recursion(0, 0, n)

print(w)
print(b)
