# Úkol 3: Analýza textových dat (CSV/TXT)

> **Zásady používání nástrojů AI:** Student může použít AI pro inspiraci, vysvětlení nebo dílčí pomoc, ale musí umět obhájit vlastní kód, popsat svá rozhodnutí a případně reagovat na operativní požadavky k úpravám či rozšířením.

## Cíl úkolu

Procvičit práci se soubory, výjimkami, funkcemi a statistickým zpracováním dat.

## Zadání

Vytvořte program, který načte textový soubor (`CSV` nebo `TXT`) obsahující informace o studentech ve tvaru:

```text
jméno;příjmení;body_z_testu
```

Program umožní uživateli vybrat operaci:

- vypsat pět nejlepších studentů;
- vypsat studenty pod průměrem;
- uložit statistiku třídění podle bodů do nového souboru.

## Požadavky

1. Ošetřete všechny chyby, například `FileNotFoundError`, špatný formát a prázdné řádky.
2. Použijte minimálně tři funkce: načtení dat, výpočet statistiky a výpis.
3. Data lze zpracovat pomocí seznamů nebo slovníků.
4. Využijte konstrukci `with open()`.

## Výstup

Program vypíše statistiky, uloží zpracovaný soubor a umožní pokračovat v práci.

## Výstup pro obhajobu

Student:

1. předvede funkčnost programu;
2. zodpoví otázky a případně program upraví.
