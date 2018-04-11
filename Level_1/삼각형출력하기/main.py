def printTriangle(num):
    s = ""
    #함수를 완성하세요
    for i in range(num):
        s += "*"*(i+1)+"\n"
    return s


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( printTriangle(3) )