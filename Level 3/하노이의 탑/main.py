def solution(n):
    return hanoi_move(n, 1, 2, 3)

def hanoi_move(n, start, blank, end):
    if n == 1:
        return [[start, end]]
    else:
        return hanoi_move(n-1, start, end, blank) + hanoi_move(1, start, blank, end) + hanoi_move(n-1, blank, start, end)