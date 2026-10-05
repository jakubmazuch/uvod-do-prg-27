# Úkol 1: Síť kartografického zobrazení

> **Zásady používání nástrojů AI:** Student může použít AI pro inspiraci, vysvětlení nebo dílčí pomoc, ale musí umět obhájit vlastní kód, popsat svá rozhodnutí a případně reagovat na operativní požadavky k úpravám či rozšířením.

## Cíl úkolu

Vytvořte program, který pomocí knihovny `turtle` vykreslí kartografickou síť (poledníky a rovnoběžky) pro zvolené nekonformní zobrazení. Cílem je procvičit algoritmizaci, matematické transformace a vizualizaci.

## Specifikace výstupu

1. Výstupem je vykreslení kartografické sítě pomocí knihovny `turtle`.
2. Musí být zobrazeny poledníky a rovnoběžky v daném rozsahu.
3. Výstup musí být čitelný i při vyšší hustotě čar.
4. Uživatel může změnit měřítko, barvy, posun a parametry vzorkování.

## Vstupní parametry programu

Program umožní nastavit:

- `u_min`, `u_max` - rozsah zeměpisné délky;
- `v_min`, `v_max` - rozsah zeměpisné šířky;
- krok poledníků a rovnoběžek;
- `sampling_step` - hustotu vzorkování;
- výběr kartografického zobrazení.

## Povolená kartografická zobrazení

Implementujte minimálně dvě z následujících zobrazení:

- azimutální ekvidistantní;
- azimutální Lambertovo (rovnoploché);
- kónické zobrazení (např. Lambertovo konformní);
- azimutální stereografické.

Válcová zobrazení nejsou povolena.

## Požadavky na implementaci

- Minimálně dvě funkce: výpočet transformace a vykreslení čar.
- Použijte pouze standardní knihovny (`math`, `turtle`).
- Kroky musí být parametrizovatelné.
- Použitý algoritmus musíte umět vysvětlit.

## Minimální rozsah projektu

1. Minimálně dvě kartografická zobrazení.
2. Kód rozdělený do funkcí.
3. Každé zobrazení se vykreslí zvlášť.
4. Ošetřené výjimky.

## Výstup pro obhajobu

Student:

1. ukáže funkční vykreslení;
2. vysvětlí klíčové výpočetní funkce;
3. zodpoví otázky a případně program upraví.
