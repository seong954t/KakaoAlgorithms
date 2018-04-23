def tiling(n):
    answer = [0, 1, 2]
    for i in range(3, n+1):
        answer[i%3] = (answer[(i-1)%3]+answer[(i-2)%3])%100000
    return answer[n%3]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(tiling(2))
