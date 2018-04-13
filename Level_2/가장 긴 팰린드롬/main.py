def longest_palindrom(s):
    # 함수를 완성하세요
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    right = longest_palindrom(s[1:])
    left = longest_palindrom(s[:-1])
    mid = longest_palindrom(s[1:-1])
    
    if s[:1] == s[-1:]:
        mid += 2
    return max([right, left, mid])


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(longest_palindrom("토마토맛토마토"))
print(longest_palindrom("토마토맛있어"))