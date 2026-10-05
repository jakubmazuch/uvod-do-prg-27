# Předběžný plán cvičení 8 (3. 12. 2026) – Práce se soubory

## 1. Operace se seznamem

Napište program, který umožní uživateli zadat index a následně vypíše odpovídající prvek seznamu. Pokud je zadaný index mimo rozsah seznamu, zachyťte výjimku `IndexError` a vypište srozumitelnou chybovou zprávu.

## 2. Práce se souborem `jmena.csv`

Následující úlohy pracují se souborem `jmena.csv`, který je dostupný v GitHub repozitáři. Soubor obsahuje seznam frekventantů pokročilého kurzu mandarínštiny a jejich data narození.

## 3. Počet frekventantů

Napište program, který načte soubor `jmena.csv` a vypíše celkový počet frekventantů jazykového kurzu.

## 4. Věk frekventantů

Napište program, který vytvoří nový soubor se stejnými osobami, ale datum narození nahradí aktuálním věkem frekventanta.

**Ukázka výstupního souboru:**

```text
Martina Holá,49
Jana Jemelíková,84
Alena Škorvagová,23
```

## 5. Nejmladší frekventant

Napište program, který vypíše jméno, příjmení a věk nejmladšího frekventanta.

## 6. Průměrný věk frekventantů

Napište program, který vypočítá a vypíše průměrný věk frekventantů kurzu mandarínštiny.

## 7. Generování e-mailových adres

Vzdělávací jazyková instituce zajišťuje svým klientům školní e-mailové adresy. Pro každého frekventanta vygenerujte adresu ve formátu:

```text
prijmeni.j@example.com
```

Příjmení zapište bez diakritiky malými písmeny. Za tečkou následuje první písmeno křestního jména. Vygenerované adresy uložte do souboru `e-maily.csv`.

**Ukázka výstupního souboru:**

```text
hola.m@example.com
jemelikova.j@example.com
skorvagova.a@example.com
```

## 8. Kontrola duplicitních e-mailových adres

Vytvořte program, který ověří, zda se v souboru `e-maily.csv` nacházejí duplicitní adresy. Pokud ano, upravte generování adres tak, že ke každé další duplicitní místní části doplníte pořadové číslo.

Příklad řešení duplicity:

```text
bohaty.a@example.com
bohaty.a2@example.com
```

Funkčnost lze ověřit na řádcích 108 a 109 se záznamy Andreje a Alexeje Bohatových.

## 9. Sloučení generování a kontroly e-mailů

Slučte řešení úloh 6 a 7 do jednoho programu. Program načte soubor `jmena.csv`, vygeneruje jedinečné e-mailové adresy a uloží je do souboru `e-maily.csv`.

Řešení rozdělte do vhodně pojmenovaných funkcí.

## 10. Četnost křestních jmen

Zjistěte, kolikrát se v souboru `jmena.csv` vyskytuje každé křestní jméno. Výsledky vypište sestupně podle četnosti; jména se stejnou četností seřaďte abecedně.

Výstup současně uložte do souboru `cetnost-jmen.csv` ve formátu:

```text
jmeno,pocet
Jan,8
Petr,6
Anna,5
```
