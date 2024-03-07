# BOJ - 14503 로봇 청소기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N: row, M: column
r, c, d = map(int, input().split())  # r, c: 청소기 좌표, d: 청소기 방향(0: 북, 1: 동, 2: 남, 3: 서)
room = [list(map(int, input().split())) for _ in range(N)]  # 0: 청소 X, 1: 벽
answer = 0
"""
- 현재 칸이 청소되지 않은 경우 - 현재 칸 청소

- 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
1. 반시계 방향으로 90도 회전
2. 바라보는 방향 기준 앞쪽이 청소되지 않으면 한칸 전진
3. 이동한 칸 청소

- 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
1. 후진할 수 있다면 한 칸 후진 후 현재 칸 확인
2. 후진할 수 없다면 작동 멈춤
"""

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

while True:
    if room[r][c] == 0:
        room[r][c] = 2  # 2: 청소 함
        answer += 1

    clean_flag = 1
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if room[nr][nc] == 0:
            clean_flag = 0

    if clean_flag == 0:
        d = (d + 3) % 4
        nr, nc = r + dr[d], c + dc[d]
        if room[nr][nc] == 0:
            r, c = nr, nc
            room[nr][nc] = 2
            answer += 1

    else:
        nr, nc = r + dr[(d+2) % 4], c + dc[(d+2) % 4]
        if room[nr][nc] != 1:
            r, c = nr, nc
        else:
            break

print(answer)
