# Předběžný plán cvičení 4 (22. 10. 2026) – Booleovská logika, úplné a neúplné podmínky `if`, `if–else`

## 1. Kvadratická rovnice

Uživatel zadá koeficienty `a`, `b` a `c`. Program vypočítá a vypíše kořeny rovnice

$$
ax^2 + bx + c = 0.
$$

Program musí vhodně reagovat na zadané hodnoty a nesmí předpokládat, že uživatel zadá pouze koeficienty vedoucí ke dvěma různým reálným kořenům.

### Gradace úlohy

1. Upravte program tak, aby správně řešil všechny zvláštní případy, zejména:
   - `a == 0`,
   - `b == 0`,
   - `c == 0`,
   - diskriminant $D = b^2 - 4ac$ je záporný.
2. Upravte program tak, aby dokázal vypočítat a vypsat také komplexní kořeny.

## 2. Počet číslic

Uživatel zadá celé číslo `a`. Program vypíše, zda je číslo:

- jednociferné,
- dvouciferné,
- tříciferné,
- čtyřciferné,
- pěticiferné,
- šesticiferné,
- nebo více než šesticiferné.

Při řešení uvažujte také záporná čísla.

## 3. Minimum a maximum

Uživatel zadá tři různé číselné hodnoty. Program určí a vypíše jejich minimum a maximum.

> **Omezení:** Nepoužívejte vestavěné funkce `min()` ani `max()`.

## 4. Součiny vektorů

Uživatel zadá dva vektory v prostoru, tedy dva seznamy se třemi souřadnicemi:

$$
\vec{u} = (u_1, u_2, u_3), \qquad \vec{v} = (v_1, v_2, v_3).
$$

Program vypočítá a vypíše:

1. vektorový součin $\vec{w} = \vec{u} \times \vec{v}$;
2. skalární součin $\vec{u} \cdot \vec{v}$;
3. délku vektoru $\vec{w}$, tedy $|\vec{w}|$.

## 5. Bankomat se seznamem

Vyřešte znovu úlohu **Bankomat** z Cvičení 2. Uživatel zadá libovolnou celočíselnou částku a program vypíše počet jednotlivých bankovek a mincí, které klientovi vydá.

Nominální hodnoty uložte do seznamu:

```python
[5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
```
