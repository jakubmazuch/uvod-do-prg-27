# Cvičení 1 (1. 10. 2026) – Úvodní seminář, Python a Visual Studio Code

## 1. Seznámení s organizací kurzu

Seznamte se s požadavky kurzu, způsobem odevzdávání úloh, pravidly hodnocení a umístěním studijních materiálů.

V počítači vytvořte složku pro celý kurz a v ní podsložku `cviceni-01`. Do této podsložky budete ukládat dnešní programy.

## 2. Instalace Pythonu 3.14

Stáhněte a nainstalujte Python 3.14 z oficiální stránky:

<https://www.python.org/downloads/>

Při instalaci ve Windows zaškrtněte možnost **Add Python to PATH**. Po dokončení instalace otevřete terminál a ověřte verzi příkazem:

```text
python --version
```

Pokud příkaz `python` není dostupný, vyzkoušejte:

```text
py --version
```

Výstup musí uvádět Python řady 3.14.

## 3. Instalace a základní nastavení Visual Studio Code

Nainstalujte Visual Studio Code:

<https://code.visualstudio.com/>

Pokud instalaci nelze provést, lze dočasně použít webovou verzi:

<https://vscode.dev/>

V prostředí Visual Studio Code:

1. nainstalujte rozšíření **Python** od společnosti Microsoft;
2. otevřete složku `cviceni-01`;
3. vytvořte soubor `prvni_program.py`;
4. vyberte nainstalovaný interpret Pythonu 3.14;
5. otevřete integrovaný terminál.

## 4. První program

Do souboru `prvni_program.py` zapište program, který vypíše text:

```text
Ahoj, světe!
Začínám programovat v Pythonu.
```

Program spusťte tlačítkem pro spuštění i z integrovaného terminálu:

```text
python prvni_program.py
```

Vyzkoušejte změnit text, program znovu uložte a spusťte. Sledujte rozdíl mezi zdrojovým souborem a výstupem programu v terminálu.

## 5. Proměnné a jednoduchý výstup

Vytvořte soubor `vizitka.py`. Do proměnných uložte své jméno, studijní obor a ročník. Program údaje vypíše v několika přehledných řádcích.

Poté doplňte dvě číselné proměnné a vypište jejich součet, rozdíl, součin a podíl. Všímejte si, že operátor `+` pracuje s textem a čísly odlišně.

## 6. Vstup od uživatele

Vytvořte soubor `pozdrav.py`. Program se pomocí funkce `input()` zeptá uživatele na jméno a obor a následně jej osobně pozdraví.

**Příklad běhu programu:**

```text
Jak se jmenujete? Jana
Jaký obor studujete? Geografie
Ahoj, Jano! Vítejte v kurzu programování pro obor Geografie.
```

Nemusíte zatím řešit správné skloňování jména.

## 7. Samostatný závěrečný úkol

Vytvořte soubor `prevod_teploty.py`. Uživatel zadá teplotu ve stupních Celsia a program vypíše odpovídající teplotu ve stupních Fahrenheita podle vztahu

$$
F = \frac{9}{5}C + 32.
$$

Pro převod načteného textu na číslo použijte funkci `float()`.

