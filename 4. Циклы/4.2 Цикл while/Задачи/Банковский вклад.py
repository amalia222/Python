start_sum = float(input())
percent = float(input())
target_sum = float(input())
months = 0
while start_sum < target_sum:
    start_sum = start_sum + (start_sum * (percent/12)/100)
    months += 1
    print(f"{months} - {start_sum:.2f}")