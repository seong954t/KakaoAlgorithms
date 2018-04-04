def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(3))