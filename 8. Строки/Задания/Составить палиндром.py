def can_form_palindrome(s):
    sps = [0] * 26
    for i in s:
        if i.isalpha():
            inx = ord(i.upper()) - ord('A')
            sps[inx] += 1

    count = 0
    for i in sps:
        if i % 2 != 0:
            count += 1
        if count > 1:
            return 'NO'

    left = ''
    mid = ''
    for i in range(25, -1, -1):
        char = chr(ord('A') + i)
        if sps[i] % 2 == 1:
            mid = char
        left += char * (sps[i] // 2)

    return left + mid + left[::-1]


st = input()
print(can_form_palindrome(st))