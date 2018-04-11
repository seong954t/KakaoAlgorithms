def gcdlcm(a, b):
    mul = a*b
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a%b)
    return [a, (int)(mul/a)]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))