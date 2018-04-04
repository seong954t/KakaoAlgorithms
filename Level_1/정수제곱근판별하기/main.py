import math

def nextSqure(n):
    # 함수를 완성하세요
    sqrt = math.sqrt(n)
    if sqrt%1 == 0.0:
        return (sqrt+1)*(sqrt+1)
    else:
        return 'no'

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)))