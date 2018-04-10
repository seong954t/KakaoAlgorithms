def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    for i in range(len(strings)):
        strings[i] = strings[i][n:]+strings[i][:n]
    strings.sort()
    for i in range(len(strings)):
        string_len = len(strings[i])
        strings[i] = strings[i][string_len-n:]+strings[i][:string_len-n]
    return strings



# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( strange_sort(["sun", "bed", "car"], 1) )