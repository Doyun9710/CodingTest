import sys

input = sys.stdin.readline

testCase = int(sys.stdin.readline())
queue = []
cnt = 0

for i in range(testCase):
    comm = sys.stdin.readline().strip()
    if comm.split()[0] == 'push':
        queue.append(int(comm.split()[1]))
    elif comm.split()[0] == 'pop':
        if len(queue)-cnt == 0:
            print(-1)
        else:
            print(queue[cnt])
            cnt += 1

    elif comm.split()[0] == 'size':
        print(len(queue)-cnt)
    elif comm.split()[0] == 'empty':
        if len(queue)-cnt == 0:
            print(1)
        else:
            print(0)
    elif comm.split()[0] == 'front':
        if len(queue)-cnt == 0:
            print(-1)
        else:
            print(queue[cnt])
    elif comm.split()[0] == 'back':
        if len(queue)-cnt == 0:
            print(-1)
        else:
            print(queue[-1])


# list 사용 코드. 시간초과
# import sys

# n = int(sys.stdin.readline())
# queue = []

# for i in range(n):
#     com = sys.stdin.readline().split()
#     if com[0] == 'push':
#         queue.append(com[1])
#     elif com[0] == 'pop':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue.pop(0))
#     elif com[0] == 'size':
#         print(len(queue))
#     elif com[0] == 'empty':
#         if len(queue) == 0:
#             print(1)
#         else:
#             print(0)
#     elif com[0] == 'front':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[0])
#     elif com[0] == 'back':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[-1])


# deque 사용 코드
# import sys
# from collections import deque
# n = int(input())
# queue = deque([])
# for i in range(n):
#     com = sys.stdin.readline().split()
#     if com[0] == 'push':
#         queue.append(com[1])
#     elif com[0] == 'pop':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue.popleft())
#     elif com[0] == 'size':
#         print(len(queue))
#     elif com[0] == 'empty':
#         if len(queue) == 0:
#             print(1)
#         else:
#             print(0)
#     elif com[0] == 'front':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[0])
#     elif com[0] == 'back':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[-1])
