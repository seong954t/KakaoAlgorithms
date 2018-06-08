def solution(s):
    result = []
    for c in s:
        if c == '(':
            result.append(c)
        elif c == ')':
            try:
                result.pop()
            except:
                return False
    return not result