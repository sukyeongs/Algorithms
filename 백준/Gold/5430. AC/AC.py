# BOJ - 5430 AC
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())  # 테스트케이스 개수 (최대 100)

for _ in range(T):
    p = input().rstrip()  # 수행할 함수 (ex. RDD)
    n = int(input())  # 원소 개수
    numbers = deque(eval(input()))
    error_flag = False
    r_cnt = 0

    for i in range(len(p)):
        if p[i] == 'R':
            r_cnt += 1
        elif p[i] == 'D':
            if numbers:
                if r_cnt % 2 == 0:
                    numbers.popleft()
                else:
                    numbers.pop()
            else:
                print("error")
                error_flag = True
                break

    if error_flag is False:
        if r_cnt % 2 == 0:
            pass
        else:
            numbers.reverse()
            
        result = "[" + ",".join(list(map(str, list(numbers)))) + "]"
        print(result)
