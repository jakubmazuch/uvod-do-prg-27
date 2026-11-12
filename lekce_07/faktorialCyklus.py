# Faktorál pomocí cyklu


def faktorial(n):
    if n < 0:
        return None

    vysledek = 1

    for cislo in range(1, n+1):
        vysledek = vysledek * cislo

    return vysledek


n = int(input("Zadej nezáporné číslo: "))
if n < 0:
    print("Nelze vypočítat faktoriál ze záporného čísla.")
print(f"{n}! = {faktorial(n)}")
