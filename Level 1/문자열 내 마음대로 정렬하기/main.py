def solution(strings, n):
    strings.sort()
    result = [x[n] for x in strings]
    result.sort()
    for string in strings:
        result[result.index(string[n])] = string
    return result