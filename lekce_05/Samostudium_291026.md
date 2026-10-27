# Úlohy k samostudiu

<p style="color: red;"><strong>Lekce dne 29. 10. 2026 se nekoná.</strong></p>

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

## 4. Minimum a maximum

Uživatel zadá tři různé číselné hodnoty. Program určí a vypíše jejich minimum a maximum.

> **Omezení:** Nepoužívejte vestavěné funkce `min()` ani `max()`.
