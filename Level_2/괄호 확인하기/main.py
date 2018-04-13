def is_pair(s):
    # 함수를 완성하세요
    result = []
    for c in s:
        if c == '(':
            result.append(c)
        elif c == ')':
            try:
                result.pop()
            except:
                return False
    return not result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( is_pair("(hello)()"))
print( is_pair(")("))