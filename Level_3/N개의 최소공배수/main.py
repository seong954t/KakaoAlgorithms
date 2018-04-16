def nlcm(num):
    answer = 0
    if len(num) == 1:
        return num[0]
    gcd_val = num[0]*num[1]//gcd(num[0], num[1])
    num.append(gcd_val)
    return nlcm(num[2:])

def gcd(a, b):
    if b == 0:
        return a
    if a < b:
        a, b = b, a
    return gcd(b, a%b)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([2,6,8,14]))