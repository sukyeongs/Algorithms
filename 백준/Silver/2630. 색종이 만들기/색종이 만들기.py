# BOJ - 2630 색종이 만들기
import sys
input = sys.stdin.readline

N = int(input())  # N: 종이 한 변의 길이
paper = [list(map(int, input().split())) for _ in range(N)]  # 0: 하얀색, 1: 파란색

white_cnt = 0
blue_cnt = 0


def solution(x, y, n):
    global white_cnt, blue_cnt
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != color:
                solution(x, y, n//2)
                solution(x+n//2, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        white_cnt += 1
    else:
        blue_cnt += 1


solution(0, 0, N)
print(white_cnt)
print(blue_cnt)