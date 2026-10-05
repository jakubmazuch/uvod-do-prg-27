# Cvičení 7 (26. 11. 2026) – Výjimky

## 1. Fibonacciho čísla

Uživatel zadá přirozené číslo $n$. Program vypíše:

1. prvních $n$ členů Fibonacciho posloupnosti;
2. pouze $n$-tý člen Fibonacciho posloupnosti.

Vstup od uživatele bezpečně převeďte na celé číslo. Pomocí výjimek ošetřete neplatný vstup a samostatně zkontrolujte, zda je zadané číslo kladné.

## 2. Bezpečný číselný vstup

Vytvořte program, který požádá uživatele o zadání celého čísla. Pokud uživatel zadá neplatný vstup, například text nebo desetinné číslo, program:

1. zachytí vzniklou výjimku;
2. vypíše srozumitelnou chybovou zprávu;
3. požádá uživatele o nové zadání.

Tento postup se opakuje, dokud uživatel nezadá platné celé číslo. Poté program vypíše zadané číslo zvětšené o jedna.

## 3. Bezpečné dělení

Vytvořte funkci, která přijme dvě reálná čísla a vrátí výsledek jejich dělení.

Funkce musí ošetřit alespoň následující situace:

- vstup nelze převést na reálné číslo;
- dělitel je roven nule.

Pokud dělení nelze provést, funkce vypíše odpovídající chybovou zprávu a vrátí `None`.

## 4. Validace geografických souřadnic

Uživatel zadá geografické souřadnice v jediném řádku ve formátu:

```text
zemepisna_sirka, zemepisna_delka
```

Například:

```text
50.0272, 15.2027
```

Vytvořte funkci `nacti_souradnice()`, která vstup rozdělí, převede obě hodnoty na typ `float` a vrátí je jako dvojici.

Program musí rozlišit a ošetřit následující chyby:

- chybějící nebo přebývající hodnota;
- hodnotu, kterou nelze převést na číslo;
- zeměpisnou šířku mimo interval $\langle -90, 90 \rangle$;
- zeměpisnou délku mimo interval $\langle -180, 180 \rangle$.

Pro souřadnice mimo povolený rozsah vytvořte a použijte vlastní typ výjimky `SouradniceMimoRozsahError`. Neplatný vstup nesmí program ukončit; uživatel je opakovaně vyzýván, dokud nezadá platné souřadnice.

Po úspěšném zadání program vypíše souřadnice a určí, zda daný bod leží na severní, nebo jižní polokouli a na východní, nebo západní polokouli.
