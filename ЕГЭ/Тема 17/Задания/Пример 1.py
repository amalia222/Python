nums = list(map(int, open('Пример 1.txt').readlines()))

# Кол-во элементов, абсолютное значение которых является четырёхзначным числом и оканчивается на 3
count = sum(1 for i in nums if 1000 <= abs(i) <= 9999 and str(abs(i))[-1] == '3')
result_count = 0
result_sum = 0
for i in range(len(nums) - 2):
    triple = sorted(nums[i:i + 3])
    if sum(triple[1:]) > count ** 2:
        result_count += 1
        s = sum(triple)
        if s > result_sum:
            result_sum = abs(s)
print(result_count, result_sum)