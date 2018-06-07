import math
def solution(n):
    answer = -1
    sqrt = math.sqrt(n)
    
    if sqrt%1 == 0.0:
        answer = (sqrt+1)*(sqrt+1)
    return answer