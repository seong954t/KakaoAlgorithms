def solution(s):
    answer = ''
    for c in s.split(' '):
        for i in range(len(c)):
            if i % 2 == 0:
                answer += c[i].upper()
            else:
                answer += c[i].lower()
        answer += ' '
    return answer[:-1]