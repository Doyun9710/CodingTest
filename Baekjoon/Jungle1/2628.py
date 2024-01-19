import sys

r, c = map(int, sys.stdin.readline().split())

row = [0, r]   
col = [0, c]
n = int(sys.stdin.readline())

for i in range(n):
    is_xy, n = map(int, sys.stdin.readline().split())  
    if is_xy == 1:             
        row.append(n)
    else :
        col.append(n)

row.sort()    
col.sort() 
              
sub_r = []  
sub_c = [] 

for i in range(len(row)-1):   
    sub_r.append(row[i + 1] - row[i])
for i in range(len(col) -1):
    sub_c.append(col[i+1]- col[i]) 

print(max(sub_r) * max(sub_c))


# box = [list(map(int, input().split())) for _ in range(1)]
# n = int(sys.stdin.readline())

# for i in range(n):
#     xy = [list(map(int, input().split())) for _ in range(1)]
#     box += xy


# subW = []
# subH = []

# for j in range(1, len(box)-2):
#     if box[i][0] == 0:
#         print(box)
