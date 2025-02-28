def is_prime(number):
    for i in range(2, int((number**0.5) + 1)):
        if number % i == 0:
            return False
    return True
n = int(input())
count = 1
while count <= n:
    if is_prime (number):
        print(number, end=" ")
        count += 1