def productMatrix(A, B):
    answer = []
    A_x_range = len(A)
    A_y_range = len(A[0])
    B_y_range = len(B[0])
    
    for x in range(A_x_range):
        a_val = []
        for y in range(B_y_range):
            val = 0
            for idx in range(A_y_range):
                val += A[x][idx]*B[idx][y]
            a_val.append(val)
        answer.append(a_val)
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [ [ 1, 2 ], [ 2, 3 ]]
b = [[ 3, 4], [5, 6]]
print("결과 : {}".format(productMatrix(a,b)))