def solution(arr, divisor):
    answer = list(filter(lambda i: i%divisor == 0, arr))
    answer.sort()
    if len(answer) == 0:
        return [-1]
    return answer