import sys

def enqueue(data):
    queue.append(data)
    
def dequeue():
    del queue[0]

def putanswerlist(data):
    answer.append(data)

queue = []
n, k = list(map(int, sys.stdin.readline().split()))
answer = []

for i in range(1, n+1):
    enqueue(i)
# print('<', end='')
for i in range(n):
    for j in range(k-1):
        enqueue(queue[0])
        dequeue()
    # print(queue[0], end='')
    putanswerlist(queue[0])
    dequeue()
print("<", end='')
print(', '.join(map(str,answer)), end='')
print(">")