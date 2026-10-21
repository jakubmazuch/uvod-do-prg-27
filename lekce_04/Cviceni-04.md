# Předběžný plán cvičení 4 (22. 10. 2026) – Booleovská logika, úplné a neúplné podmínky `if`, `if–else`

## 1. Množiny studijních předmětů

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

## 2. Evidence bodů studentů

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

## 3. Geografický bod

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

## 4. Kvadratická rovnice

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

## 5. Počet číslic

Uživatel zadá celé číslo `a`. Program vypíše, zda je číslo:

- jednociferné,
- dvouciferné,
- tříciferné,
- čtyřciferné,
- pěticiferné,
- šesticiferné,
- nebo více než šesticiferné.

Při řešení uvažujte také záporná čísla.

## 6. Minimum a maximum

Uživatel zadá tři různé číselné hodnoty. Program určí a vypíše jejich minimum a maximum.

> **Omezení:** Nepoužívejte vestavěné funkce `min()` ani `max()`.

## 7. Součiny vektorů

Uživatel zadá dva vektory v prostoru, tedy dva seznamy se třemi souřadnicemi:

$$
\vec{u} = (u_1, u_2, u_3), \qquad \vec{v} = (v_1, v_2, v_3).
$$

Program vypočítá a vypíše:

1. vektorový součin $\vec{w} = \vec{u} \times \vec{v}$;
2. skalární součin $\vec{u} \cdot \vec{v}$;
3. délku vektoru $\vec{w}$, tedy $|\vec{w}|$.

## 8. Bankomat se seznamem

Vyřešte znovu úlohu **Bankomat** z Cvičení 2. Uživatel zadá libovolnou celočíselnou částku a program vypíše počet jednotlivých bankovek a mincí, které klientovi vydá.

Nominální hodnoty uložte do seznamu:

```python
[5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
```
