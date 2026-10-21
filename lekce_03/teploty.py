seznam = [12.5, 13.2, 11.8, 14.0, 14.1, 13.7, 12.9]

print("Všechna měření: ", seznam)

print("První teplota: ", seznam[0])
print("Poslední teplota: ", seznam[-1])

print("Třetí až pátá teplota: ", seznam[2:5])
seznam[1] = 13.0
print("Změňte jednu chybnou hodnotu: ", seznam[1])
seznam.append(15.2)
print("Přidejte nové měření na konec seznamu: ", seznam[-1])
seznam.insert(3, 16.5)
print("Vložte nové měření na zvolenou pozici: ", seznam[3])
