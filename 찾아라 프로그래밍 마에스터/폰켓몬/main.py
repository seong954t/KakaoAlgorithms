def solution(nums):
    answer = len(nums)//2
    kinds = len(list(set(nums)))
    if answer > kinds:
        answer = kinds
    return answer