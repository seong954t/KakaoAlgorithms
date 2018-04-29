def parenthesisCase(n):
    answer = [[1]*(n+1)]+[[0 for i in range(n+1)] for j in range(n)]
    for i in range(1, n+1):
        for j in range(i, n+1):
            answer[i][j] = answer[i][j-1]+answer[i-1][j]
    
    return answer[n][n]
    
# 실행을 위한 테스트코드입니다.
if parenthesisCase(3) == 5:
    print("parenthesisCase(3)이 정상 동작합니다. 제출을 눌러서 다른 경우에도 정답인지 확인해 보세요.")
else:
    print("parenthesisCase(3)이 정상 동작하지 않습니다.")
