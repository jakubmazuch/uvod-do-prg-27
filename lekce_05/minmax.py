a = float(input("Zadejte první číslo: "))
b = float(input("Zadejte druhé číslo: "))
c = float(input("Zadejte třetí číslo: "))

nejmensi = a
nejvetsi = a

if b < nejmensi:
    nejmensi = b
if b > nejvetsi:
    nejvetsi = b

if c < nejmensi:
    nejmensi = c
if c > nejvetsi:
    nejvetsi = c

print("Minimum: ", nejmensi)
print("Maximum: ", nejvetsi)
