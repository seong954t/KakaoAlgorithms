def hanoi(n):    
    return hanoi_move(n, 1, 2, 3)  # 2차원 배열을 반환해 주어야 합니다.

def hanoi_move(n, start, blank, end):
    if n == 1:
        return [[start, end]]
    else:
        return hanoi_move(n-1, start, end, blank) + hanoi_move(1, start, blank, end) + hanoi_move(n-1, blank, start, end)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(hanoi(2))
