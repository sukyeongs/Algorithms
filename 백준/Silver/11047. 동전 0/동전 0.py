# BOJ - 11047 동전 0
import sys
sys_input = sys.stdin.readline

coin_type, target = map(int, sys_input().split())
coin_value = []
coin_cnt = 0

for _ in range(coin_type):
    coin_value.append(int(sys_input()))

coin_value.reverse()

for coin in coin_value:
    if target // coin < 1:
        continue
    else:
        coin_cnt += target // coin
        target = target % coin
        if target == 0:
            break

print(coin_cnt)
