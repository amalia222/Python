n = int(input())
eng_to_lat = {}
for i in range(n):
    line = input().split(' - ')
    eng_to_lat[line[0]] = line[1].split(', ')


lat_to_eng = {}
for eng_word, lat_words in eng_to_lat.items():
    for lat_word in lat_words:
        if lat_word not in lat_to_eng:
            lat_to_eng[lat_word] = []
        lat_to_eng[lat_word].append(eng_word)

print(len(lat_to_eng.keys()))

for lat_word in sorted(lat_to_eng.keys()):
    eng_words = sorted(lat_to_eng[lat_word])
    print(f"{lat_word} - {', '.join(eng_words)}")