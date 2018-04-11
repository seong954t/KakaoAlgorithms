def numPY(s):
    # 함수를 완성하세요
    s = s.lower()
    return s.count('p') == s.count('y')



# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )