N = int(input())

def HANOI(x, y, z, cnt):
    if cnt == 0:
        # print(z,y)
        return

    HANOI(x, z, y, cnt - 1) # N == 홀, 짝? 홀: 패스, 짝: y, z 교환 후 출력. ※ N 홀수 시 z 먼저
    print(x, z)
    HANOI(y, x, z, cnt - 1)
    print(y, z)
    HANOI(x, y, z, cnt - 1)

print((1 << N) - 1)
if N <= 20:
    HANOI(1, 2, 3, N)
