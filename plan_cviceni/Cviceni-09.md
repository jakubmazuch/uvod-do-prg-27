# Předběžný plán cvičení 9 (10. 12. 2026) – Objektově orientované programování I

## 1. Bod v rovině

Vytvořte třídu `Bod`, která bude reprezentovat bod v rovině.

### Požadavky

- Konstruktor přijme souřadnice `x` a `y` a uloží je do atributů objektu.
- Metoda `vypis()` vrátí souřadnice bodu ve formátu `(x, y)`.
- Metoda `vzdalenost_od_pocatku()` vypočítá vzdálenost bodu od počátku soustavy souřadnic.
- Vytvořte alespoň tři různé objekty třídy `Bod` a jejich metody vyzkoušejte.

Pro vzdálenost bodu od počátku použijte vztah

$$
d = \sqrt{x^2 + y^2}.
$$

## 2. Obdélník

Vytvořte třídu `Obdelnik`, která bude uchovávat délky dvou stran obdélníku.

### Požadavky

- Konstruktor přijme hodnoty `sirka` a `vyska`.
- Metoda `obsah()` vrátí obsah obdélníku.
- Metoda `obvod()` vrátí obvod obdélníku.
- Metoda `je_ctverec()` vrátí hodnotu `True`, pokud jsou obě strany stejně dlouhé, jinak vrátí `False`.
- Metoda `popis()` vrátí stručný text obsahující rozměry, obsah a obvod objektu.
- Pokud je některá zadaná délka nulová nebo záporná, konstruktor vyvolá výjimku `ValueError`.

Vytvořte několik objektů s různými rozměry a ověřte správnost všech metod. Ověřte také reakci programu na neplatné rozměry.

## 3. Meteorologické měření

Vytvořte třídu `Mereni`, která bude reprezentovat jedno meteorologické měření.

### Atributy objektu

- `stanice` – název měřicí stanice;
- `teplota` – teplota ve stupních Celsia;
- `srazky` – množství srážek v milimetrech.

### Metody

- `popis()` vrátí všechny údaje o měření v čitelné podobě;
- `je_mraz()` vrátí `True`, pokud je teplota nižší než `0 °C`;
- `je_destivy_den()` vrátí `True`, pokud jsou srážky větší než `0 mm`;
- `zmen_teplotu(nova_teplota)` nastaví novou hodnotu teploty.

Vytvořte seznam alespoň pěti objektů třídy `Mereni`. Pomocí cyklu:

1. vypište popis všech měření;
2. vypište pouze měření s teplotou pod bodem mrazu;
3. vypočítejte průměrnou teplotu;
4. určete celkový úhrn srážek.

## 4. Rozšíření – evidence měření

Rozšiřte třídu `Mereni` o atribut `datum`. Přidejte metodu `do_csv()`, která vrátí data objektu jako jeden řádek vhodný k uložení do souboru CSV.

**Příklad výsledku:**

```text
2026-12-10,Kolín,-2.4,1.8
```

Uložte všechna měření ze seznamu do souboru `mereni.csv`. Každý objekt bude zapsán na samostatném řádku.
