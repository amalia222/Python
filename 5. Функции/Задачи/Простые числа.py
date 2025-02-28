def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int((number**0.5) + 1)):
        if number % i == 0:
            return False
    return True
n = int(input())
count = 1
num = 1
while count <= n:
    if is_prime(num):
        print(num, end=" ")
        count += 1
    num += 1