def convert_to(num, base):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    while num > 0:
        result += digits[num % base]
        num //= base
    return result[::-1]


def convert_from(num, base):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = 0
    for i in num:
        value = digits.index(i)
        result = result * base + value
    return result


def convert(num, base_in, base_out):
    return convert_to(convert_from(num, base_in), base_out)


num1 = input()
base_in1, base_out1 = list(map(int, input().split()))
print(convert(num1, base_in1, base_out1))