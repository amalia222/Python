# Неправильные последовательности
# ** и более подряд
# -- и более подряд
# 8, 9
#
import re

line = open('Пример 1.txt').read()
# s = sorted(re.findall(r'(?=((?:0|[1-7][0-7]*)(?:\*(?:0|[1-7][0-7]*))*(?:-(?:0|[1-7][0-7]*))*))', line), key=len, reverse=True)

line = re.sub(r'\*{2,}', ' ', line)
line = re.sub(r'-{2,}', ' ', line)
line = re.sub(r'-\*', ' ', line)
line = re.sub(r'\*-', ' ', line)
line = re.sub(r'8', ' ', line)
line = re.sub(r'9', ' ', line)

parts = line.split()

parts = [p.strip('-*0') for p in parts]

for p in sorted(parts, key=len, reverse=True)[:100]:
    print(p, len(p))
