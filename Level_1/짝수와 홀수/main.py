def evenOrOdd(num):
    s = ""
    #함수를 완성하세요
    if num % 2 == 0:
        s = "Even"
    else:
        s = "Odd"
    return s

#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))
