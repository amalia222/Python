def is_per(num):
    summ = 0
    for i in range(1, num):
        if num % i == 0:
            summ += i
    return num == summ
n = int(input())
count = 0
number = 1
while count < n:
    if is_per(number):
        print(number, end=" ")
        count += 1
    number += 1
