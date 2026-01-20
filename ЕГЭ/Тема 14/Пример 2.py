number = 2 * 2187**2020 + 729**2021 - 2 * 243**2022 + 81**2023 - 2 * 27**2024 - 6561

count = 0
while number > 0:
    if number % 27 > 9:
        count += 1
    number //= 27
print(count)