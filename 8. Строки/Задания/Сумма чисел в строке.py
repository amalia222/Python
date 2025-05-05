s = input()
curr_num = ''
x = 0
summ = 0
while x < len(s):
    if s[x].isdigit():
        curr_num += s[x]
    elif curr_num != '':
        summ += int(curr_num)
        curr_num = ''
    x += 1
if curr_num != '':
        summ += int(curr_num)
print(summ)
