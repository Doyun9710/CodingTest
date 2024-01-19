import sys

n = int(sys.stdin.readline())

for i in range(n):
    for j in range(i+1):
        print('*', end="")
    print("")

# 출력문 사이 빈칸 or 끼워넣기
# https://gilu-world.tistory.com/40
