# 2798 - 블랙잭

from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

card_com = combinations(cards, 3)
result = []

for i in card_com:
  result.append(sum(i))

result.sort(reverse=True)
for i in range(len(result)):
  if result[i] <= m:
    print(result[i])
    break
  else:
    pass
