def sumMatrix(A,B):
    for rowIdx in range(len(B)):
        for cellIdx in range(len(B[rowIdx])):
            A[rowIdx][cellIdx] += B[rowIdx][cellIdx]
    return A

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))