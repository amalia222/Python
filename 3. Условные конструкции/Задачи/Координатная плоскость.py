x1 = int(input())
y1 = int(input())
if x1 > 0 and y1 > 0:
    print("Первая четверть")
elif x1 > 0 and y1 < 0:
    print("Вторая четверть")
elif x1 < 0 < y1:
    print("Четвертая четверть")
elif x1 < 0 and y1 < 0:
    print("Третья четверть")
else x1 == 0 or y1 == 0:
    print("Точка лежит на оси координат")
