def solution(str):
    # 함수를 완성하세요
    str_len = len(str)
    str_len_2 = str_len//2
    if str_len%2 == 0:
        return str[str_len_2-1:str_len_2+1]
    else:
        return str[str_len_2:str_len_2+1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("powwer"))