D = int(input("Zadej celé stupně: "))
M = int(input("Zadej celé minuty: "))
S = int(input("Zadej celé vteřiny: "))

numD = D+M/60+S/3600

print(numD, "°")
