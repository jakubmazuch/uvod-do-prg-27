# Faktorál pomocí rekurze


def faktorial(n):
    if n < 0:
        return None

    if n == 0:
        return 1

    return n*faktorial(n-1)


n = int(input("Zadej nezáporné číslo: "))
if n < 0:
    print("Nelze vypočítat faktoriál ze záporného čísla.")
print(f"{n}! = {faktorial(n)}")
