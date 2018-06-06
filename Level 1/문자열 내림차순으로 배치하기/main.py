def solution(s):
    answer = ''
    s = list(s)
    s.sort()
    s.reverse()
    answer = ''.join(s)
    return answer