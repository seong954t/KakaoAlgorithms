def solution(s, n):
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