from sys import setrecursionlimit
setrecursionlimit(10000)

def g(n):
  if n <= 25:
    return 2 * (n + 1)
  else:
    return g(n - 4) + n

def f(n):
  return g(n - 1) - g(n - 5)

print(f(150774))