# Cvičení 2 (8. 10. 2026) – Datové typy, čísla a jejich reprezentace, proměnná, příkaz

## 1. Řešení domácího úkolu

Vytvořte soubor `prevod_teploty.py`. Uživatel zadá teplotu ve stupních Celsia a program vypíše odpovídající teplotu ve stupních Fahrenheita podle vztahu

$$
F = \frac{9}{5}C + 32.
$$

Pro převod načteného textu na číslo použijte funkci `float()`.

## 2. Kalkulačka

Uživatel zadá dvě čísla `x` a `y`. Program vypíše výsledky následujících operací:

- součet `x + y`,
- rozdíl `x - y`,
- součin `x * y`.

## 3. Bankomat

Uživatel zadá libovolnou celočíselnou částku. Program simuluje výdej hotovosti z bankomatu a vypíše počet jednotlivých bankovek a mincí, které klientovi vydá.

Uvažujte následující nominální hodnoty:

`5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1`

> **Omezení:** Nepoužívejte cykly, podmínky ani seznamy. Tyto konstrukce budeme probírat později.

## 4. DMS – stupně, minuty a sekundy

Vytvořte program, který převede úhlovou míru:

1. ze zápisu ve stupních, minutách a sekundách (DMS) na desetinné stupně;
2. z desetinných stupňů na zápis ve stupních, minutách a sekundách (DMS).

**Příklad:**

$$
78^\circ 12' 29'' \approx 78{,}20805555555556^\circ
$$

## 5. Zaokrouhlování

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
