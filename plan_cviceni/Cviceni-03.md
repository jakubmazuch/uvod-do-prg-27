# Předběžný plán cvičení 3 (15. 10. 2026) – Dynamické datové struktury

## 1. Seznam naměřených teplot

Vytvořte seznam alespoň sedmi naměřených teplot. Bez použití cyklu:

1. vypište celý seznam;
2. vypište první a poslední hodnotu;
3. vypište třetí až pátou hodnotu pomocí řezu;
4. změňte jednu chybnou hodnotu;
5. přidejte nové měření na konec seznamu;
6. vložte nové měření na zvolenou pozici;
7. odstraňte jednu hodnotu.

Nakonec vypište počet měření, nejnižší a nejvyšší teplotu.

## 2. Souřadnice bodu a n-tice

Souřadnice bodu v prostoru uložte jako n-tici:

```python
bod = (12.5, -4.0, 8.75)
```

1. Rozbalte n-tici do proměnných `x`, `y` a `z`.
2. Vypište jednotlivé souřadnice.
3. Vypočítejte vzdálenost bodu od počátku soustavy souřadnic.
4. Pokuste se změnit jednu souřadnici přímo v n-tici a vysvětlete vzniklou chybu.

Pro vzdálenost použijte vztah

$$
d = \sqrt{x^2 + y^2 + z^2}.
$$

## 3. Slovník meteorologické stanice

Údaje o jednom měření uložte do slovníku s klíči `stanice`, `teplota`, `vlhkost` a `srazky`.

1. Vypište název stanice a teplotu pomocí jejich klíčů.
2. Změňte hodnotu teploty.
3. Přidejte položku `tlak`.
4. Odstraňte položku `vlhkost`.
5. Vypište všechny klíče a následně všechny hodnoty slovníku.
6. Pomocí metody `get()` bezpečně zjistěte hodnotu klíče `vitr`, který ve slovníku nemusí existovat.

## 4. Množiny studijních předmětů

Dva studenti mají zapsané předměty:

```python
student_a = {"Matematika", "Programování", "Kartografie", "Angličtina"}
student_b = {"Programování", "Statistika", "Kartografie", "Němčina"}
```

Pomocí množinových operací určete:

1. předměty zapsané oběma studenty;
2. všechny předměty zapsané alespoň jedním studentem;
3. předměty, které má zapsané pouze student A;
4. předměty, které má zapsané právě jeden ze studentů.

Přidejte studentovi A nový předmět a jeden původní předmět odeberte.

## 5. Evidence bodů studentů

Vytvořte slovník, jehož klíčem je jméno studenta a hodnotou seznam bodů ze tří krátkých testů.

```python
body = {
    "Anna": [8, 9, 10],
    "Boris": [6, 7, 9],
    "Cyril": [10, 10, 8]
}
```

Bez použití cyklu:

1. vypište všechny body vybraného studenta;
2. opravte jeden chybně zadaný počet bodů;
3. přidejte nového studenta;
4. doplňte vybranému studentovi body za čtvrtý test;
5. vypočítejte součet a průměr bodů jednoho vybraného studenta.

## 6. Geografický bod

Vytvořte slovník popisující geografický bod. Musí obsahovat:

- název místa;
- souřadnice uložené jako n-tici `(zemepisna_sirka, zemepisna_delka)`;
- seznam naměřených nadmořských výšek;
- množinu textových značek, například `mesto`, `stanice` nebo `kontrolni_bod`.

Program:

1. vypíše název a souřadnice místa;
2. doplní novou naměřenou výšku;
3. vypočítá průměrnou nadmořskou výšku;
4. přidá novou značku;
5. vypíše celý aktualizovaný záznam.
