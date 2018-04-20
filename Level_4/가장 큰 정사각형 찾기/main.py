def findLargestSquare(board):
    answer = 0
    for i in range(len(board[0])):
        if board[0][i] == 'O':
            board[0][i] = 1
            answer = 1
        else:
            board[0][i] = 0
    for i in range(len(board)):
        if board[i][0] == 'O':
            board[i][0] = 1
            answer = 1
        else:
            board[i][0] = 0
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 'O':
                board[i][j] = min(board[i][j-1], board[i-1][j], board[i-1][j-1])+1
                if answer < board[i][j]:
                    answer = board[i][j]
            else:
                board[i][j] = 0
    return answer*answer

#아래 코드는 출력을 위한 테스트 코드입니다.

testBoard = [['X','O','O','O','X'],['X','O','O','O','O'],['X','X','O','O','O'],['X','X','O','O','O'],['X','X','X','X','X']]
print(findLargestSquare(testBoard))