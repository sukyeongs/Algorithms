# BOJ - 14500 테트로미노
import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 세로, M: 가로
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


# DFS - 깊이 제한 필요
def dfs_form(r: int, c: int, depth: int):
    """
    법규 모양을 제외한 나머지 케이스
    만약 현재 깊이가 3이라면 값 반환, 아니라면 현재 + 이동할 부분의 tetromino 함수 값 (재귀)
    :param depth: 현재 깊이
    :param r: x 좌표
    :param c: y 좌표
    :return result: 최댓값
    """
    if depth == 3:
        return paper[r][c]

    visited[r][c] = 1
    result = 0
    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
            result = max(result, paper[r][c] + dfs_form(nx, ny, depth + 1))
    visited[r][c] = 0

    return result


def other_form(r: int, c: int):
    """
    법규 모양의 경우, dfs 형태로 풀 수 없음
    가능한 4가지 케이스 직접 구현
    :param r: row
    :param c: column
    :return result: 최댓값
    """
    result = 0
    # ㅗ
    if r - 1 >= 0 and c - 1 >= 0 and c + 1 < M:
        result = max(result, paper[r][c] + paper[r][c-1] + paper[r-1][c] + paper[r][c+1])
    # ㅏ
    if r - 1 >= 0 and c + 1 < M and r + 1 < N:
        result = max(result, paper[r][c] + paper[r-1][c] + paper[r][c+1] + paper[r+1][c])
    # ㅜ
    if c - 1 >= 0 and r + 1 < N and c + 1 < M:
        result = max(result, paper[r][c] + paper[r][c-1] + paper[r+1][c] + paper[r][c+1])
    # ㅓ
    if c - 1 >= 0 and r - 1 >= 0 and r + 1 < N:
        result = max(result, paper[r][c] + paper[r][c-1] + paper[r-1][c] + paper[r+1][c])

    return result


ans = 0

for i in range(N):
    for j in range(M):
        ans = max(ans, dfs_form(i, j, 0))
        ans = max(ans, other_form(i, j))

print(ans)
