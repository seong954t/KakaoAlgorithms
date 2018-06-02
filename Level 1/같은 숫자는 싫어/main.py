def solution(arr):
    answer = []
    cmp = ""
    for c in arr:
        if cmp != c:
            answer.append(c)
            cmp = c
    return answer