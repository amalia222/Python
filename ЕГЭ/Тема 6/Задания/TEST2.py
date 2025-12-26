alg = 18 * 7 ** 108 - 5 * 49 ** 76 + 343 ** 35 - 50
summ = 0
while alg != 0:
  summ += alg % 49
  alg = alg // 49
print(summ)