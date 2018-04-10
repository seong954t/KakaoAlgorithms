def water_melon(n):
    # 함수를 완성하세요.
    if n < 1:
        return ""
    elif n%2 == 1:
        return water_melon(n-1)+"수"
    else:
        return water_melon(n-1)+"박"
    return ""


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3))
print("n이 4인 경우: " + water_melon(4))