import re

line = open('Пример 2.txt').read()

line = re.sub(r'(\d)(\d*)(\d)', r'\1 \3', line)
parts = line.split()
words = []
for part in parts:
    if len(re.findall(r'[A-Z]+', part)) >= 10000:
        words.append(part)
print(min(words, key=len))