def obratText(text):
    vysledek = ""

    for znak in text:
        vysledek = znak + vysledek

    return vysledek


vstup = input("Zadejte text: ")
obraceny = obratText(vstup)

if vstup == obraceny:
    print(f"{vstup} je palindrom.")
else:
    print(f"Text {vstup} pozpátku je {obraceny}.")
