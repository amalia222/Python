def encode(text, offset):
    alp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = ''
    offset = offset % len(alp)
    for i in text:
        if i in alp:
            new_pos = (alp.index(i) + offset) % len(alp)
            result += alp[new_pos]
        elif i in alp.lower():
            new_pos = (alp.lower().index(i) + offset) % len(alp)
            result += alp[new_pos].lower()
        else:
            result += i
    return result


def decode(text, offset):
    return encode(text, -offset)


text2 = input()
offset = int(input())
print(decode(text2, offset))