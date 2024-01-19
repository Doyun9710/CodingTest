import sys


def enque(num):
    global size
    size += 1
    queue[size] = num

    p = size
    while p > 1:
        if queue[p] > queue[p//2]:
            queue[p], queue[p//2] = queue[p//2], queue[p]
        else:
            break
        p //= 2


def deque():
    global size
    if size == 0:
        print(0)
        return
    else:
        print(queue[1])
        queue[1] = queue[size]
        queue[size] = 0
        size -= 1

        parent = 1
        while True:
            child = parent * 2
            # 왼쪽 오른쪽 선택
            if child + 1 <= size and queue[child] < queue[child + 1]:
                child += 1

            if child > size or queue[child] < queue[parent]:
                break
            # swap( & heap[parent], & heap[child])
            else: 
                queue[parent], queue[child] = queue[child], queue[parent]
                parent = child

        return


n = int(sys.stdin.readline())
queue = [0 for i in range(n+1)]
size = 0

for i in range(n):
    case = int(sys.stdin.readline())

    if case == 0:
        deque()
    else:
        enque(case)
