nominaly = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
castka = int(input("Zadejte částku: "))

if castka <= 0:
    print("Částka musí být kladná.")
else:
    zbyva = castka
    i = 0  # počítadlo iterací (od 0), počítadlo bude ukazovat na index v seznamu nominaly

    while zbyva > 0:
        bankovka = nominaly[i]
        pocet = zbyva // bankovka
        zbyva = zbyva % bankovka

        if pocet > 0:
            print(f"{pocet}× {bankovka} Kč")

        i += 1  # zvyš i o jedna
