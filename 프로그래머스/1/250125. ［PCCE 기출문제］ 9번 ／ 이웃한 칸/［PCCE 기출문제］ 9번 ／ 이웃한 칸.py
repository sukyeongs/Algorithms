def compare_color(board, h, w):
    dh, dw = [1, -1, 0, 0], [0, 0, 1, -1]
    color = board[h][w]
    count = 0
    
    for i in range(4):
        nh, nw = h + dh[i], w + dw[i]
        if 0 <= nh < len(board) and 0 <= nw < len(board) and board[nh][nw] == color:
            count += 1
    
    return count
    


def solution(board, h, w):
    return compare_color(board, h, w)