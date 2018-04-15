def productMatrix(A, B):
    answer = []
    x_range = len(A)
    y_range = len(A[0])
    for i in range(x_range):
        a_val = []
        for j in range(x_range):
            val = 0
            for k in range(y_range):
                val += A[i][k]*B[k][j]
            a_val.append(val)
        answer.append(a_val)
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [ [ 1, 2 ], [ 2, 3 ]]
b = [[ 3, 4], [5, 6]]
print("결과 : {}".format(productMatrix(a,b)))