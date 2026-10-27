cislo = int(input("Zadej celé číslo. "))

if cislo < 0:
    print("Tvojr číslo ", cislo, " je záporné.")
elif cislo == 0:
    print("Tvoje číslo ", cislo, " je nula.")
else:
    print("Tvojr číslo ", cislo, " je kladné.")