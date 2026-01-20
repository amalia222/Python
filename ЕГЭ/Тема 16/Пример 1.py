f = [0] * 1_600_000_000
count = 0
for i in range(1, len(f)):
    f[i] = f[i // 10] + i % 10

for n in range(765432015, 154261340):
    if f[n] > f[n + 1]:
        count += 1
print(count)