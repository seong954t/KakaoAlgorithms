def solution(board):
    answer = 0
    for i in range(len(board[0])):
        if board[0][i] == 1:
            board[0][i] = 1
            answer = 1
        else:
            board[0][i] = 0
    for i in range(len(board)):
        if board[i][0] == 1:
            board[i][0] = 1
            answer = 1
        else:
            board[i][0] = 0
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i][j-1], board[i-1][j], board[i-1][j-1])+1
                if answer < board[i][j]:
                    answer = board[i][j]
            else:
                board[i][j] = 0
    return answer*answer