def solution(s):
    sList = [int(i) for i in s.split()]
    answer = str(min(sList))+" "+str(max(sList))
    return answer