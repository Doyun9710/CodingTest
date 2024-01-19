# 단어 정렬
import sys
# 퀵 정렬
# 길이가 짧은 것부터, 길이가 같으면 사전 순으로
# 우선순위 높은 조건 마지막 정렬 (순서 1.중복제거, 2.사전정렬, 3.길이정렬)
def sort(arr, l, r):
    i = l
    for j in range(l, r):
        if arr[j] <= arr[r]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i
def arrsort(arr, l, r):
    if l < r:
        p = sort(arr, l, r)

        arrsort(arr, l, p-1)
        arrsort(arr, p+1, r)


def merge_sort(array):
    if len(array)<=1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i,j,k = 0,0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k+=1
    
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array

n = int(sys.stdin.readline())
# arr = [sys.stdin.readline() for _ in range(n)]
# arr = list(set(arr))
arr = list(set([sys.stdin.readline().strip() for _ in range(n)]))
arrlen = len(arr)

arrsort(arr, 0, arrlen-1)
print("시작 :", arr)
merge_sort(arr)
# print("최종 :", arr)

for i in range(len(arr)):
    print(arr[i])



# # 함수 이용 시 ------------------------------------------------------------
# import sys
# n = int(sys.stdin.readline())
# # set 자료형을 통해 중복을 제거하고 정렬을 위해 list 자료형으로 감싸준다.
# word = list(set(str(sys.stdin.readline().strip()) for _ in range(n)))
# word.sort() # 오름차순 정렬
# word.sort(key=len) # 단어의 길이를 기준으로 오름차순 정렬

# # 반복문을 통해 단어를 출력
# for i in word:
#     print(i)
# # 함수 이용 시 ------------------------------------------------------------