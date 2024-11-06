<div align="center">

| Podstawy sztucznej inteligencji | laboratorium |
|---------------------------------|--------------|
| SAN                             |              |
| Autor                           | Yaroslav Zubakha |
| E-mail                          | 121546@student.san.edu.pl / yar.zubaha@proton.me |
| Nr albumu                       | 121546       |
| Data                            | 03.11.2024   |
| Wersja                          | 1.2          |

<br>

# **Zadanie nr 2**

</div>

<br>

> ## Opis zadania
- Stworzyć tabelę decyzyjną z min. 8 obiektami, 4 atrybutami, w tym jednym decyzyjnym.
- Dla stworzonej tabeli znaleźć zestaw reguł minimalnych.
    - Tablicę decyzyjną (8 rekordów, 4 cech).
    - Wyznaczone reguły minimalne.

<br>

> ## Solution
### 1. Przykładowa Tabela Decyzyjna: Zasady Wypożyczeń w Bibliotece

W tej tabeli oceniamy, czy użytkownik może wypożyczyć książkę na podstawie poniższych atrybutów:

- **Typ użytkownika**: „Student” lub „Pracownik naukowy”
- **Status książki**: „Dostępna” lub „Zarezerwowana”
- **Książki zaległe**: „Tak” lub „Nie”
- **Ważność członkostwa**: „Ważne” lub „Wygasłe”
- **Decyzja**: „Może wypożyczyć” lub „Nie może wypożyczyć”

| Obiekt | Typ użytkownika | Status książki | Książki zaległe | Ważność członkostwa | Może wypożyczyć |
|--------|------------------|----------------|------------------|---------------------|-----------------|
| 1      | Student         | Dostępna       | Nie             | Ważne              | Tak             |
| 2      | Student         | Dostępna       | Tak             | Ważne              | Nie             |
| 3      | Pracownik       | Zarezerwowana  | Nie             | Ważne              | Tak             |
| 4      | Pracownik       | Dostępna       | Nie             | Wygasłe            | Nie             |
| 5      | Student         | Zarezerwowana  | Nie             | Ważne              | Nie             |
| 6      | Pracownik       | Dostępna       | Nie             | Ważne              | Tak             |
| 7      | Student         | Dostępna       | Nie             | Wygasłe            | Nie             |
| 8      | Pracownik       | Dostępna       | Tak             | Ważne              | Nie             |

<br>

### 2. Zestaw Minimalnych Reguł

Na podstawie tabeli decyzyjnej, opracowano następujące minimalne reguły:

1. **Jeśli `Typ użytkownika = Student` oraz `Status książki = Dostępna` oraz `Książki zaległe = Nie` oraz `Ważność członkostwa = Ważne`, to Może wypożyczyć = Tak**
2. **Jeśli `Typ użytkownika = Student` oraz `Książki zaległe = Tak`, to Może wypożyczyć = Nie**
3. **Jeśli `Typ użytkownika = Pracownik` oraz `Status książki = Zarezerwowana` oraz `Ważność członkostwa = Ważne`, to Może wypożyczyć = Tak**
4. **Jeśli `Ważność członkostwa = Wygasłe`, to Może wypożyczyć = Nie**
5. **Jeśli `Typ użytkownika = Student` oraz `Status książki = Zarezerwowana`, to Może wypożyczyć = Nie**
6. **Jeśli `Typ użytkownika = Pracownik` oraz `Status książki = Dostępna` oraz `Książki zaległe = Nie` oraz `Ważność członkostwa = Ważne`, to Może wypożyczyć = Tak**
7. **Jeśli `Książki zaległe = Tak`, to Może wypożyczyć = Nie**

<br>

> ## Przebieg obliczeń

### Krok 1: Macierz Nierozróżnialności

Macierz nierozróżnialności pokazuje pary obiektów o identycznych wartościach atrybutów, które różnią się wyłącznie atrybutem decyzyjnym.

|       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|-------|---|---|---|---|---|---|---|---|
| **1** | Ø |   |   |   |   |   |   |   |
| **2** |   | Ø |   |   |   |   |   |   |
| **3** |   |   | Ø |   |   |   |   |   |
| **4** |   |   |   | Ø |   |   |   |   |
| **5** |   |   |   |   | Ø |   |   |   |
| **6** |   |   |   |   |   | Ø |   |   |
| **7** |   |   |   |   |   |   | Ø |   |
| **8** |   |   |   |   |   |   |   | Ø |


### Krok 2: Macierz Rozróżnialności

Macierz rozróżnialności pokazuje różnice między obiektami, co pozwala zidentyfikować minimalne reguły. Każda litera oznacza atrybut, który różni się między parami obiektów:

|       | 1   | 2   | 3     | 4    | 5   | 6    | 7    | 8    |
|-------|-----|-----|-------|------|-----|------|------|------|
| **1** | Ø   | K   | TS    | TS   | S   | T    | W    | TS   |
| **2** | K   | Ø   | TS    | TS   | KS  | T    | WS   | TS   |
| **3** | TS  | TS  | Ø     | W    | T   | W    | TSW  | W    |
| **4** | TS  | TS  | W     | Ø    | TS  | T    | WS   | TS   |
| **5** | S   | KS  | T     | TS   | Ø   | TS   | W    | TS   |
| **6** | T   | T   | W     | T    | TS  | Ø    | TSW  | W    |
| **7** | W   | WS  | TSW   | WS   | W   | TSW  | Ø    | TS   |
| **8** | TS  | TS  | W     | TS   | TS  | W    | TS   | Ø    |

W macierzy tej:
- `T` oznacza `Typ użytkownika`
- `S` oznacza `Status książki`
- `K` oznacza `Książki zaległe`
- `W` oznacza `Ważność członkostwa`

### Krok 3: Utworzenie Zestawu Reguł Minimalnych

Na podstawie macierzy rozróżnialności oraz nierozróżnialności wyznaczono minimalne reguły, które opisano powyżej.

