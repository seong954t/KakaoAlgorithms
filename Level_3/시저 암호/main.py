def caesar(s, n):
    result = ""
    n %= 26
    for c in s:
        ord_val = ord(c)
        if ord_val > 96:
            ord_val += n
            if ord_val > 122:
                ord_val -= 122
                ord_val += 96
        elif ord_val > 64:
            ord_val += n
            if ord_val > 90:
                ord_val -= 90
                ord_val += 64
        result += chr(ord_val)
    return result
    # 주어진 문장을 암호화하여 반환하세요.


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))