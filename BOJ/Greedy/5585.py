# 5585 - 거스름돈

change = 1000 - int(input())

coin = [500, 100, 50, 10, 5, 1]
count = 0

for i in range(len(coin)):
  count += (change // coin[i])
  change -= (coin[i] * (change // coin[i]))
  if change == 0:
    print(count)
    break
