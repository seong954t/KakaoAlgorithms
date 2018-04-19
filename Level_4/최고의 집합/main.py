def bestSet(n, s):
    answer = []
    share = s//n
    remainder = s%n
    if share == 0:
        return [-1]
    answer = [share]*(n-remainder)
    if s%n == 0:
        return answer
    return answer + bestSet(remainder, s-share*(n-remainder))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(bestSet(3,13))