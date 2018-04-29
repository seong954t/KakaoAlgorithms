def tiling(n):
    answer = [0 for i in range(n//2)]
    answer[0] = 3
    if n%2 == 1:
        return 0
    for i in range(1, n//2):
        answer[i] = (answer[i-1]*3+2)%100000
        for j in range(i-1):
            answer[i] = (answer[i]+answer[j]*2)%100000
    return answer[n//2-1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(tiling(2))