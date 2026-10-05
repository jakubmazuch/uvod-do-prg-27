# Úkol 4: Geometrie v Pythonu pro 2D grafický systém

> **Zásady používání nástrojů AI:** Student může použít AI pro inspiraci, vysvětlení nebo dílčí pomoc, ale musí umět obhájit vlastní kód, popsat svá rozhodnutí a případně reagovat na operativní požadavky k úpravám či rozšířením.

## Cíl úkolu

Procvičit objektový návrh, dědičnost, abstrakci, kompozici a polymorfismus.

## Zadání

Navrhněte a implementujte sadu tříd v Pythonu pro reprezentaci a manipulaci s geometrickými objekty ve 2D grafickém systému. Využijte principy OOP, zejména dědičnost, kompozici, abstraktní třídy a metody.

### 1. Abstraktní třída `AGO`

- Vytvořte abstraktní třídu `AGO` (*Abstract Graphical Object*), která bude sloužit jako základ pro všechny grafické objekty.
- Třída bude obsahovat základní atributy `color` (barva), `width` (šířka) a `layer` (vrstva).
- Implementujte pro tyto atributy vlastnosti (`property`) a definujte abstraktní metody `print` a `length`.

### 2. Třída `Point2D`

- Implementujte třídu `Point2D`, která reprezentuje bod ve 2D prostoru se souřadnicemi `x` a `y`.
- Třída bude obsahovat metody pro nastavení a získání souřadnic a metodu pro výpis informací o bodu.

### 3. Třída `Point`

- Vytvořte třídu `Point`, která dědí od tříd `AGO` a `Point2D`. Třída `Point` bude reprezentovat bod s grafickými atributy.
- Přepište (*override*) metody `print` a `length`.

### 4. Třídy `PolyLine` a `Polygon`

- Implementujte třídy `PolyLine` a `Polygon`, které dědí od třídy `AGO`. Tyto třídy budou reprezentovat lomenou čáru a polygon s určenými body.
- Každá třída bude obsahovat metodu pro výpis bodů a výpočet celkové délky.

### 5. Demonstrace funkcionality

- Vytvořte několik instancí tříd `Point` a `Point2D`.
- Sestavte seznam obsahující různé geometrické objekty, včetně instancí tříd `PolyLine` a `Polygon`.
- Pro každý objekt v seznamu vypočítejte a vypište jeho délku.

Řešení musí vycházet z klíčových principů OOP: abstrakce, zapouzdření, dědičnosti a polymorfismu. Implementace musí být čistá, modulární a snadno rozšiřitelná o další geometrické objekty.

## Výstup pro obhajobu

Student:

1. ukáže vytvořené objekty včetně výpisu délek všech čar a polygonů;
2. vysvětlí návrh, princip dědičnosti a polymorfismu;
3. zodpoví otázky a případně program upraví.
