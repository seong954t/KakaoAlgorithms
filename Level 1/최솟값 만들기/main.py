def solution(A,B):
    answer = 0
    size = len(A)
    A.sort()
    B.sort()
    
    for i in range(size):
        answer += A[i]*B[size-i-1]
    return answer