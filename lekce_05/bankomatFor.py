nominaly = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
castka = int(input("Zadejte částku: "))

if castka <= 0:
    print("Částka musí být kladná.")
else:
    zbyva = castka

    for i in nominaly:
        pocet = zbyva // i
        if pocet > 0:
            print(f"{pocet}× {i} Kč")
        zbyva = zbyva % i
