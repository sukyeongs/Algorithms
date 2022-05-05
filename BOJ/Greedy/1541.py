# 1541 - 잃어버린 괄호

eq = list(input().split("-"))
add_result = []

for i in eq:
  if "+" in i:
    eq_list = list(map(int, i.split("+")))
    add_result.append(sum(eq_list))
  else:
    add_result.append(int(i))

result = add_result[0]
for i in range (1, len(add_result)):
  result -= add_result[i]

print(result)
