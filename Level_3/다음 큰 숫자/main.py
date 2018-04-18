def nextBigNumber(n):
    count = bin(n).count('1')
    n += 1
    while bin(n).count('1') != count:
        n += 1
    return n

#아래 코드는 테스트를 위한 출력 코드입니다.
print(nextBigNumber(78))