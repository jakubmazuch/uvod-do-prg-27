mereni = {
    "stanice": "Kolín",
    "teplota": 14.5,
    "vlhkost": 68,
    "srazky": 0.2
}

# 1. Přístup pomocí klíče
print("Stanice: ", mereni["stanice"])
print("Teplota: ", mereni["teplota"])

# 2. Změna teploty
mereni["teplota"] = 15.2

# 3. Přidání tlaku
mereni["tlak"] = 1015

# 4. Odstranění vlhkosti
del mereni["vlhkost"]

# 5. Klíče a hodnoty dict
print("Klíče: ", mereni.keys())
print("Hodnoty: ", mereni.values())

# 6. Bezpečné získání chybějící hodnoty
print("Vítr: ", mereni.get("vitr", "Údaj není k dispozici."))