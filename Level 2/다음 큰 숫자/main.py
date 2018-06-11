def solution(n):
    binN = list(bin(n))[2:]
    binN.reverse()
    lastOneIndex = binN.index('1')
    subNum = bin(n).count('1') - bin(n+2**lastOneIndex).count('1')
    return n + (2 ** lastOneIndex) + (2 ** subNum) -1