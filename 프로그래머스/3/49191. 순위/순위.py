def solution(n, results):
    answer = 0
    board = [[0]*n for _ in range(n)]
    
    for winner, loser in results:
        board[winner-1][loser-1] = 1
        board[loser-1][winner-1] = -1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or board[i][j] in [1,-1]:
                    continue
                if board[i][k] == board[k][j] == 1:
                    board[i][j] = 1
                    board[j][i] = board[k][i] = board[j][k] = -1
    
    for row in board:
        if row.count(0) == 1:
            answer += 1
    return answer