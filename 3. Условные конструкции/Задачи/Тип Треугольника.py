a= int(input())
b= int(input())
c= int(input())


if a**2+b**2 == c**2 or b**2+c**2 == a**2 or a**2+c**2 == b**2:
    print ("Прямоугольный")
elif a**2+b**2 > c**2 or b**2+c**2 > a**2 or a**2+c**2 > b**2:
    print ("Остроугольный")
elif a**2+b**2 < c**2 or b**2+c**2 < a**2 or a**2+c**2 < b**2:
    print ("Тупоугольный")
else: print ("Не существует")
