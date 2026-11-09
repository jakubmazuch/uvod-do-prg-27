# Cvičení 5 (5. 11. 2026) – Cykly `for` a `while`

## 1. Evidence bodů studentů

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

## 2. Minimum a maximum

Uživatel zadá tři různé číselné hodnoty. Program určí a vypíše jejich minimum a maximum.

> **Omezení:** Nepoužívejte vestavěné funkce `min()` ani `max()`.

## 3. Bankomat se seznamem

Vyřešte znovu úlohu **Bankomat** z Cvičení 2. Uživatel zadá libovolnou celočíselnou částku a program vypíše počet jednotlivých bankovek a mincí, které klientovi vydá.

Nominální hodnoty uložte do seznamu:

```python
[5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
```

## 4. Bankomat pomocí cyklu

Vyřešte znovu úlohu **Bankomat** z předchozích cvičení. Uživatel zadá libovolnou celočíselnou částku a program vypíše počet jednotlivých bankovek a mincí, které klientovi vydá.

Nominální hodnoty uložte do seznamu:

```python
[5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
```

Seznam nominálních hodnot zpracujte pomocí cyklu.

## 5. Myslím si číslo

Uživatel zadá celočíselné hranice `a` a `b`. Program náhodně zvolí celé číslo z uzavřeného intervalu $\langle a, b \rangle$.

Uživatel opakovaně hádá číslo a program po každém pokusu vypíše, zda je zadaná hodnota:

- menší než hledané číslo;
- větší než hledané číslo;
- rovna hledanému číslu.

V případě správného tipu program vypíše `BINGO` a ukončí se.

## 6. Množiny studijních předmětů

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

## 7. Geografický bod

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

## 8. Součiny vektorů

Uživatel zadá dva vektory v prostoru, tedy dva seznamy se třemi souřadnicemi:

$$
\vec{u} = (u_1, u_2, u_3), \qquad \vec{v} = (v_1, v_2, v_3).
$$

Program vypočítá a vypíše:

1. vektorový součin $\vec{w} = \vec{u} \times \vec{v}$;
2. skalární součin $\vec{u} \cdot \vec{v}$;
3. délku vektoru $\vec{w}$, tedy $|\vec{w}|$;
4. úhel $\varphi$ mezi vektory $\vec{u}$ a $\vec{v}$, kde

   $\varphi = \arccos\left(\dfrac{\vec{u} \cdot \vec{v}}{|\vec{u}| \cdot |\vec{v}|}\right)$.

Při výpočtech vhodně využijte cyklus.
