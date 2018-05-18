def nextBigNumber(n):
    binN = list(bin(n))[2:]
    binN.reverse()
    lastOneIndex = binN.index('1')
    subNum = bin(n).count('1') - bin(n+2**lastOneIndex).count('1')
    return n + (2 ** lastOneIndex) + (2 ** subNum) -1

#아래 코드는 테스트를 위한 출력 코드입니다.
print(nextBigNumber(78))