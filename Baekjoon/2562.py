import sys

list = []
for i in range(9):
    list.append(int(sys.stdin.readline()))
    
print(max(list))
print(list.index(max(list))+1)

# 결과는 같은데 이건 왜 안되는지 모르게땅
# arr = []
# for i in range(9):
#     x = int(sys.stdin.readline())
#     arr.append(x)

# max = [arr[0], 0]
# for i in range(8):
#     if arr[i] < arr[i+1]:
#         max[0] = arr[i+1]
#         max[1] = i+2

# print(max[0])
# print(max[1])