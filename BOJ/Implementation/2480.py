# 2480 - 주사위 세개

n = list(map(int, input().split()))
nlist = list()
check_n = list()

for i in n:
  if i not in nlist:
    nlist.append(i)
  else:
    check_n.append(i)

if len(check_n) == 0:
  print(max(nlist) * 100)

elif len(check_n) == 1:
  print(1000 + (check_n[0] * 100))

else:
  print(10000 + (nlist[0] * 1000))
