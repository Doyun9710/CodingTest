import sys
input = sys.stdin.readline


N = int(input())

nums = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

# max_ans, min_ans = None
max_ans, min_ans = -sys.maxsize -1, sys.maxsize

def dfs(i, arr):
    global add, sub, mul, div, max_ans, min_ans
    # 주어진 수열을 다 받았을 경우 최댓값과 최솟값 계산
    if i == N:
        max_ans = max(max_ans, arr)
        min_ans = min(min_ans, arr)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, arr + nums[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, arr - nums[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, arr * nums[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, arr / nums[i])
            div += 1

def solution(num, idx, add, sub, mul, div):
    global max_ans, min_ans

    if idx == N:
        max_ans = max(max_ans, num)
        min_ans = min(min_ans, num)
        return 
    
    if add > 0:
        solution(num + nums[idx], idx + 1, add - 1, sub, mul, div)
    if sub > 0:
        solution(num - nums[idx], idx + 1, add, sub - 1, mul, div)
    if mul > 0:
        solution(num * nums[idx], idx + 1, add, sub , mul -1, div)
    if div > 0:
        solution(int(num / nums[idx]), idx + 1, add, sub, mul, div -1)

# dfs, solution 중 하나 선택
# dfs(1, nums[0])
solution(nums[0], 1, add, sub, mul, div)
print(max_ans)
print(min_ans)