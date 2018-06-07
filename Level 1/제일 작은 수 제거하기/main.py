def solution(arr):
    arr.remove(min(arr))
    if not arr:
        arr = [-1]
    return arr