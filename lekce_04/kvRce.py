from math import sqrt
try:
    a = int(input("Zadej hodnotu a: "))
except ValueError:
    a = 0

b = int(input("Zadej hodnotu b: "))
c = int(input("Zadej hodnotu c: "))

if a == 0:
    if b != 0:
        print("Řešením je lineární rovnice a ne kvadratická, protože hodnota a je 0")
    else:
        print("Řešením je lineární rovnice a nelze vyřešit, protože hodnoty a, b jsou obě 0")
else:
    D = b**2 - 4*a*c
    if D > 0:
        print(f"x1={round((-b + sqrt(D))/(2*a), 2)} x2={round((-b - sqrt(D))/(2*a), 2)}")
    elif D == 0:
        print(f"Řešení je: {-b/2*a}")
    else:
        print("Diskriminant je záporný s hodnotou: ", D)
