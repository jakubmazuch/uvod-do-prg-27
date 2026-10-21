# Cvičení 3 (15. 10. 2026) – Dynamické datové struktury

## 1. Zaokrouhlování (DÚ)

Vytvořte program pro zaokrouhlování reálných čísel na zadaný počet desetinných míst. Uvažujte také záporná čísla.

**Příklad vstupu:**

```text
cislo = 13.568842
pocet_desetinnych_mist = 2
```

**Příklad výstupu:**

```text
13.57
```

## 2. Seznam naměřených teplot

Vytvořte seznam alespoň sedmi naměřených teplot. Bez použití cyklu:

1. vypište celý seznam;
2. vypište první a poslední hodnotu;
3. vypište třetí až pátou hodnotu pomocí řezu;
4. změňte jednu chybnou hodnotu;
5. přidejte nové měření na konec seznamu;
6. vložte nové měření na zvolenou pozici;
7. odstraňte jednu hodnotu.

Nakonec vypište počet měření, nejnižší a nejvyšší teplotu.

## 3. Souřadnice bodu a n-tice

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

## 4. Slovník meteorologické stanice

Údaje o jednom měření uložte do slovníku s klíči `stanice`, `teplota`, `vlhkost` a `srazky`.

1. Vypište název stanice a teplotu pomocí jejich klíčů.
2. Změňte hodnotu teploty.
3. Přidejte položku `tlak`.
4. Odstraňte položku `vlhkost`.
5. Vypište všechny klíče a následně všechny hodnoty slovníku.
6. Pomocí metody `get()` bezpečně zjistěte hodnotu klíče `vitr`, který ve slovníku nemusí existovat.
