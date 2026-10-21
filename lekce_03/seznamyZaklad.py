teploty = [12.5, 13.2, 11.8, 14.0, 14.1, 13.7, 12.9]

print((teploty[0]+teploty[1])/2)

print(teploty[2:5])  # řez seznam od index 2 (vč.) do index 5 (mimo)
print(teploty[:3])  # První tři prvky
print(teploty[3:])  # Od čtvrtého prvku do konce
print(teploty[::2])  # Každý druhý prvek, počínaje prvním
print(teploty[::-1])  # Nový seznam v opačném pořadí

print("Původní teplota na indexu 2: ", teploty[2])
teploty[2] = 12.0  # změna hodnoty
print("Nová teplota na indexu 2: ", teploty[2])

# Vkládání nových prvků
teploty.append(15.4)  # přidá hodnotu na konec seznamu
print(teploty)

teploty.insert(1, 10.5)  # na index 1 vloží hodnotu float(10.5) a původní hodnoty posune (zvýši index)
print(teploty)

# Odstraňování prvků
print("-----------------------------------------")
del teploty[0]  # odstanění prvku na indexu 0
teploty.remove(14.0)  # odstraní první výskyt hodnoty 14.0
print(teploty)

# Výpočty se seznamy
print(len(teploty))  # Počet prvků
print(min(teploty))  # Minimální hodnota v seznamu
print(max(teploty))  # Maximální hodnota v seznamu
print(sum(teploty))  # Součet hodnot v seznamu

prumer = sum(teploty) / len(teploty)
print("Průměrná teplota: ", prumer, "°C")

jmeno = "JAKUB"
jmenoOpacne = jmeno[::-1]
print(jmenoOpacne)
