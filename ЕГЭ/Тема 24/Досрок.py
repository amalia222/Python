text = open('Досрок.txt').read()
text = text.replace('BC', '*')
parts = text.split('*')
max_len = 0
for i in range(len(parts) - 180):
    length = len('BC'.join(parts[i:i+181]))
    if i > 0:                        # есть BC слева — берём 'C'
        length += 1
    if i + 181 < len(parts):         # есть BC справа — берём 'B'
        length += 1
    max_len = max(max_len, length)

print(max_len)
