# Předběžný plán cvičení 5 (5. 11. 2026) – Cykly `for` a `while`, želví grafika

## 1. Součiny vektorů

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

## 2. Bankomat pomocí cyklu

Vyřešte znovu úlohu **Bankomat** z předchozích cvičení. Uživatel zadá libovolnou celočíselnou částku a program vypíše počet jednotlivých bankovek a mincí, které klientovi vydá.

Nominální hodnoty uložte do seznamu:

```python
[5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
```

Seznam nominálních hodnot zpracujte pomocí cyklu.

## 3. Myslím si číslo

Uživatel zadá celočíselné hranice `a` a `b`. Program náhodně zvolí celé číslo z uzavřeného intervalu $\langle a, b \rangle$.

Uživatel opakovaně hádá číslo a program po každém pokusu vypíše, zda je zadaná hodnota:

- menší než hledané číslo;
- větší než hledané číslo;
- rovna hledanému číslu.

V případě správného tipu program vypíše `BINGO` a ukončí se.

## 4. Želví grafika

Pomocí modulu `turtle` postupně vykreslete:

1. čtverec;
2. pravidelný pětiúhelník;
3. spirálu.

Při vykreslování opakujících se částí použijte cyklus.

## 5. Text pozpátku

Uživatel zadá text. Program jej vypíše v opačném pořadí znaků.

> **Omezení:** Úlohu vyřešte pomocí cyklu. Nepoužívejte řez `[::-1]` ani funkci `reversed()`.
