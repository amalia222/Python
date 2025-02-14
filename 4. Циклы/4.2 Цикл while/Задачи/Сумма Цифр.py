n = int(input())
sd = 0
while n>0:
    sd += n%10
    n //= 10
print(sd)