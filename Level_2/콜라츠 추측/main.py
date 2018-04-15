def collatz(num):
    answer = 0
    for i in range(500):
        if num == 1:
            return i
        if num % 2 == 0:
            num //= 2
        else:
            num = num*3+1

    return -1

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz(6))