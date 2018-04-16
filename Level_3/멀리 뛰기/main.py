def jumpCase(num):
    answer = 0
    dp = [0, 1, 2]
    for i in range(3, num+1):
        dp.append(dp[i-1]+dp[i-2])
    return dp[len(dp)-1]

#아래는 테스트로 출력해 보기 위한 코드입니다.
print(jumpCase(4))