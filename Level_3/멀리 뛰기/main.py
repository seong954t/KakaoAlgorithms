def jumpCase(num):
    answer = 0
    a, b = 1, 2
    for i in range(3, num+1):
        a, b = b, a+b
    return b

#아래는 테스트로 출력해 보기 위한 코드입니다.
print(jumpCase(4))