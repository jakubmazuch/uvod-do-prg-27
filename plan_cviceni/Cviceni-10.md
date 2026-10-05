# Předběžný plán cvičení 10 (17. 12. 2026) – Objektově orientované programování II

## 1. Obecný senzor

Vytvořte základní třídu `Senzor`.

### Atributy objektu

- `nazev` – název senzoru;
- `jednotka` – jednotka měřené veličiny;
- `hodnota` – aktuální naměřená hodnota.

### Metody

- `aktualizuj(nova_hodnota)` změní aktuální hodnotu senzoru;
- `info()` vrátí text ve formátu `název: hodnota jednotka`.

Hodnotu ukládejte do atributu `_hodnota`. Pro její čtení vytvořte vlastnost `hodnota` pomocí dekorátoru `@property`. Metoda `aktualizuj()` musí ověřit, že nová hodnota je číslo; v opačném případě vyvolá výjimku `TypeError`.

## 2. Specializované senzory

Pomocí dědičnosti vytvořte dvě třídy odvozené ze třídy `Senzor`.

### `TeplotniSenzor`

- Jednotka je vždy `°C`.
- Metoda `je_mraz()` vrátí `True`, pokud je hodnota nižší než `0`.
- Metoda `info()` doplní k běžnému výpisu text `– mráz`, pokud je teplota záporná.

### `Srazkomer`

- Jednotka je vždy `mm`.
- Záporná hodnota není přípustná; metoda `aktualizuj()` v takovém případě vyvolá `ValueError`.
- Metoda `je_dest()` vrátí `True`, pokud je hodnota větší než `0`.

Vytvořte alespoň dva objekty každého typu a ověřte jejich metody včetně neplatných vstupů.

## 3. Polymorfní zpracování senzorů

Vložte objekty tříd `TeplotniSenzor` a `Srazkomer` do jednoho seznamu. Pomocí jediného cyklu zavolejte u každého objektu metodu `info()`.

Pozorujte, že stejný příkaz může u různých typů objektů vyvolat odlišné chování.

Následně:

1. vypište informace o všech senzorech;
2. určete počet teplotních senzorů;
3. určete počet srážkoměrů;
4. pomocí vlastnosti `hodnota` vypište pouze senzory, jejichž hodnota je větší než nula.

## 4. Meteorologická stanice – kompozice

Vytvořte třídu `MeteorologickaStanice`, která bude obsahovat:

- atribut `nazev`;
- atribut `senzory` – seznam objektů typu `Senzor` a jeho potomků.

### Metody

- `pridej_senzor(senzor)` přidá senzor do stanice;
- `odeber_senzor(nazev)` odstraní senzor se zadaným názvem;
- `vypis_prehled()` vypíše název stanice a informace o všech senzorech;
- `najdi_senzor(nazev)` vrátí odpovídající objekt, nebo `None`, pokud senzor neexistuje.

Metoda `pridej_senzor()` musí ověřit, že předaný objekt je instancí třídy `Senzor` nebo jejího potomka. V opačném případě vyvolá `TypeError`.

Vytvořte jednu stanici, přidejte do ní alespoň čtyři různé senzory a vyzkoušejte všechny metody.

## 5. Rozšíření – textový report

Přidejte třídě `MeteorologickaStanice` metodu `uloz_report(nazev_souboru)`. Metoda uloží aktuální stav stanice do textového souboru.

**Příklad souboru:**

```text
Stanice: Kolín
Teplota vzduchu: -1.8 °C – mráz
Teplota půdy: 2.1 °C
Srážky: 0.4 mm
```

Ošetřete případnou chybu při zápisu do souboru a uživateli vypište srozumitelnou zprávu.
