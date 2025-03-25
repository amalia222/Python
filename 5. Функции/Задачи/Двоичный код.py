def tobin(num):
    if num == 0:
        return
    tobin(num // 2)
    print(num % 2, end="")
n = int(input())
tobin(n)
