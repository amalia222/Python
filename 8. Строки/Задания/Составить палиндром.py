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
        count1 = sps[i]
        if count1 % 2 == 1:
            mid = char
        for j in range(count1 // 2):
            left += char

    return left + mid + left[::-1]


st = input()
print(can_form_palindrome(st))