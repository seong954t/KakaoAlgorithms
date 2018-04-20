def hopscotch(board, size):
    result = [board[0], board[1]]
    prev = 0
    current = 1
    size = len(board[0])
    # 땅따먹기 게임으로 얻을 수 있는 최대 점수는? 
    for row in board[1:]:
        for i in range(size):
            result[current][i] = max(result[prev][:i]+result[prev][i+1:])+row[i]
        prev, current = current, prev
    return max(result[prev])


#아래는 테스트로 출력해 보기 위한 코드입니다.
board =  [[ 1, 2, 3, 5 ], [ 5, 6, 7, 8 ], [4, 3, 2, 1]]
print(hopscotch(board, 3))