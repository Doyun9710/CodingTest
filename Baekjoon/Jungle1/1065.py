import sys

n = int(sys.stdin.readline())
count = 0
arr = []

if n < 100:
    print(n)
else:
    for i in range(100, n+1):
        arr = list(map(int, str(i)))
        if (arr[0]-arr[1]) == (arr[1]-arr[2]):
            count += 1
    print(count+99)