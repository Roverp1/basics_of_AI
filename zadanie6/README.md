| Podstawy sztucznej inteligencji | laboratorium                                     |
| ------------------------------- | ------------------------------------------------ |
| SAN                             |                                                  |
| Autor                           | Yaroslav Zubakha                                 |
| E-mail                          | 121546@student.san.edu.pl / yar.zubaha@proton.me |
| Nr albumu                       | 121546                                           |
| Data                            | 22.01.2025                                       |
| Wersja                          | 1.0                                              |

# **Zadanie nr 6**

## Opis zadania

- Suma zbiorów
- Przecięcie zbiorów
- Iloczyn zbiorów
- Rozmyte podejmowanie decyzji.
  - Poprawne wyniki obliczeń.
  - Przynajmniej 3 kryteria (G).
  - Wskazanie podjętej decyzji.

## Solution

### 1. Przykładowa Tabela Decyzyjna: Wybór Latarki

W tej tabeli oceniamy trzy opcje latarki na podstawie poniższych kryteriów:

- **Siła światła (lm)**: wyższe wartości są lepsze.
- **Masa (kg)**: niższe wartości są lepsze.
- **Koszt (zł)**: niższe wartości są lepsze.

| Obiekt | Siła światła (lm) | Masa (kg) | Koszt (zł) |
| ------ | ----------------- | --------- | ---------- |
| x1     | 420               | 0.22      | 255        |
| x2     | 450               | 0.29      | 290        |
| x3     | 430               | 0.25      | 240        |

### 2. Funkcje Przynależności dla Kryteriów

**Siła światła (lm):**

Obliczenia dla każdego obiektu:

- x1: \((420 - 400) / 100 = 0.2\)
- x2: \((450 - 400) / 100 = 0.5\)
- x3: \((430 - 400) / 100 = 0.3\)

**Masa (kg):**

Obliczenia dla każdego obiektu:

- x1: \((0.3 - 0.22) / 0.1 = 0.8\)
- x2: \((0.3 - 0.29) / 0.1 = 0.1\)
- x3: \((0.3 - 0.25) / 0.1 = 0.5\)

**Koszt (zł):**

Obliczenia dla każdego obiektu:

- x1: \((300 - 255) / 100 = 0.5\)
- x2: \((300 - 290) / 100 = 0.1\)
- x3: \((300 - 240) / 100 = 0.6\)

### 3. Obliczone Wartości Przynależności

| Obiekt | μLM | μW  | μC  |
| ------ | --- | --- | --- |
| x1     | 0.2 | 0.8 | 0.5 |
| x2     | 0.5 | 0.1 | 0.1 |
| x3     | 0.3 | 0.5 | 0.6 |

### 4. Operacje na Zbiorach

#### Suma zbiorów

`μA ∪ B(x) = max(μA(x), μB(x))`

- Dla `μLM` i `μW`:
  - `x1: max(0.2, 0.8) = 0.8`
  - `x2: max(0.5, 0.1) = 0.5`
  - `x3: max(0.3, 0.5) = 0.5`

#### Przecięcie zbiorów

`μA ∩ B(x) = min(μA(x), μB(x))`

- Dla `μLM` i `μW`:
  - `x1: min(0.2, 0.8) = 0.2`
  - `x2: min(0.5, 0.1) = 0.1`
  - `x3: min(0.3, 0.5) = 0.3`

#### Iloczyn zbiorów

`μA × B(x) = μA(x) * μB(x)`

- Dla `μLM` i `μW`:
  - `x1: 0.2 * 0.8 = 0.16`
  - `x2: 0.5 * 0.1 = 0.05`
  - `x3: 0.3 * 0.5 = 0.15`

### 5. Rozmyte Podejmowanie Decyzji

Zbiór decyzji `D`:
`μD(x) = min(μLM(x), μW(x), μC(x))`

- `x1: min(0.2, 0.8, 0.5) = 0.2`
- `x2: min(0.5, 0.1, 0.1) = 0.1`
- `x3: min(0.3, 0.5, 0.6) = 0.3`

### Decyzja

Największy stopień przynależności: `x3`.

**Wybór**: Latarka `x3` (430 lm, 0.25 kg, 240 zł).

## Wnioski

1. Operacje na zbiorach rozmytych pozwalają łączyć i analizować różne kryteria w procesie podejmowania decyzji.
2. Zastosowanie funkcji przynależności umożliwia ocenę wartości jakościowych w sposób ilościowy.
3. Dla przykładowych danych najlepszym wyborem jest latarka `x3` dzięki najwyższemu stopniowi przynależności.
