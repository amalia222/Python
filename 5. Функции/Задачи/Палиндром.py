# Описать функцию is_palindrome(n), возвращающую True, если целый параметр n является палиндромом
# (то есть его запись читается одинаково слева направо и справа налево),
# и False в противном случае. С ее помощью найти количество палиндромов в диапазоне
# значений от a до b, вводимых с клавиатуры.
def is_palindrome(n):
    curr_val = n
    new_val = 0
    while n > 0:
        new_val = new_val * 10 + n % 10
        n = n // 10
    return new_val == curr_val
a = int(input())
b = int(input())
count = 0
for i in range(a, b):
    if is_palindrome(i):
        count += 1
print(count)