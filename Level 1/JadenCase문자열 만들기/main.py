def solution(s):
    answer = ''
    for i in s.split(' '):
        answer += i[:1].upper()+i[1:].lower()+' '
    return answer[:-1]