def getMinSum(A,B):
    answer = 0
    size = len(A)
    A.sort()
    B.sort()
    
    for i in range(size):
        answer += A[i]*B[size-i-1]
    return answer

#아래 코드는 출력을 위한 테스트 코드입니다.

print(getMinSum([1,2],[3,4]))