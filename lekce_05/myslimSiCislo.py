from random import randint

a = int(input("Zadejte dolní hranici: "))
b = int(input("Zadejte horní hranici: "))

if a > b:
    a, b = b, a

nahodne = randint(a, b)

while True:
    tip = int(input("Zadejte svůj tip: "))

    if tip < nahodne:
        print(f"Váš tip ({tip}) je menší než hledané číslo.")
    elif tip > nahodne:
        print(f"Váš tip ({tip}) je větší než hledané číslo.")
    else:
        print(f"BINGO, hledané číslo je {nahodne}")
        break
