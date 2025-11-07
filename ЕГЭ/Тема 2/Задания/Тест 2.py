n = ''
def tb(num):
    if num == 0:
        return
    tb(num // 27)
    global n
    n += str(num % 27)
    return num % 27

tb(2 * 729 ** 75 + 2 * 243 ** 78 + 81 ** 81 + 2 + 27 ** 84 + 2 * 9 ** 87 + 58)
n = n.lstrip('0')
print(n.count('0'))

def convert_to(num, base):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    while num > 0:
        result += digits[num % base]
        num //= base
    return result[::-1]