# A + B - 5 - Implementation

result = list()

while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break
  result.append(a+b)

for i in result:
  print(i)
