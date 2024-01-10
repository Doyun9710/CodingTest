a = int(input())
b = int(input())
arr = []
for i in str(b):
    arr.append(i)
    intList = [int(x) for x in arr]
    
for i in range(3):
    print(a*intList[2-i])
    
print(a*intList[0]*100+a*intList[1]*10+a*intList[2])