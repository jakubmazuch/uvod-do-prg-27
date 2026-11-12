def obratText(text):
    vysledek = ""

    for znak in text:
        vysledek = znak + vysledek

    return vysledek


vstup = input("Zadejte text: ")
print(f"Text {vstup} pozpátku je {obratText(vstup)}.")
