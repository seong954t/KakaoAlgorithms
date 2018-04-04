def findKim(seoul):
    kimIdx = 0
    # 함수를 완성하세요
    kimIdx = seoul.index("Kim")
    return "김서방은 {}에 있다".format(kimIdx)


# 실행을 위한 테스트코드입니다.
print(findKim(["Queen", "Tod", "Kim"]))