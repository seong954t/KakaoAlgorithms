def Jaden_Case(s):
    # 함수를 완성하세요
    result = ''
    for i in s.split(' '):
        result += i[:1].upper()+i[1:].lower()+' '
    return result[:-1]
    
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))