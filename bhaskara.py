import math

a = int(input("Informe a:"))
b = int(input("Informe b:"))
c = int(input("Informe c:"))

x = (b ** 2) - (4 * a * c)

if x < 0:
    print("Raizes negativas não podem ser extraídas.")
    exit()

else:
    x = math.sqrt(x)
    x1 = (-b + x) / (2 * a)
    x2 = (-b - x) / (2 * a)

print("\n\nX\' = %s \nX\'\' = " % x1, x2)



               
