def toWeirdCase(s):
    # 함수를 완성하세요
    print(s.split(' '))
    result = ''
    for c in s.split(' '):
        for i in range(len(c)):
            if i % 2 == 0:
                result += c[i].upper()
            else:
                result += c[i].lower()
        result += ' '
    return result[:-1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hello world")))