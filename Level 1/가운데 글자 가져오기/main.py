def solution(s):
    str_len = len(s)
    str_len_2 = str_len//2
    if str_len%2 == 0:
        return s[str_len_2-1:str_len_2+1]
    else:
        return s[str_len_2:str_len_2+1]