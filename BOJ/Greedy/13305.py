# 13305 - 주유소

n = int(input())

roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

result = roads[0] * costs[0]
cur_cost = costs[0]
dist = 0

for i in range(1, n - 1):
  if costs[i] < cur_cost:
    cur_cost = costs[i]
  else:
    pass
  result += cur_cost * roads[i]

print(result)
