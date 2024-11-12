<div align="center">

| Podstawy sztucznej inteligencji | laboratorium |
|---------------------------------|--------------|
| SAN                             |              |
| Autor                           | Yaroslav Zubakha |
| E-mail                          | 121546@student.san.edu.pl / yar.zubaha@proton.me |
| Nr albumu                       | 121546       |
| Data                            | 12.11.2024   |
| Wersja                          | 1.0          |

<br>

# **Zadanie nr 3**

</div>

<br>

> ## Opis zadania
- Zaprojektować perceptron potrafiący poprawnie sklasyfikować punkty na płaszczyźnie.
    - Poprawne wyniki obliczeń.
    - Wyliczone wagi.
    - Przynajmniej 3 obiekty do klasyfikacji.

<br>

> ## Kod algorytmu
Znajduje się w pliku `./121546_PSI_zadanie3.c`

<br>

> ## Przebieg obliczeń i wyliczone wagi

W ramach zadania, użyto perceptronu do klasyfikacji punktów na płaszczyźnie z wykorzystaniem dwóch wag oraz wartości progowej (threshold). Punkty są klasyfikowane jako przynależne do klasy +1 lub klasy -1 w zależności od wartości obliczonej sumy ważonej.

1. **Użyte Wagi i Próg**:
    - **w1 = 1.0**: Waga dla współrzędnej x.
    - **w2 = 1.0**: Waga dla współrzędnej y.
    - **threshold = 1.5**: Próg klasyfikacyjny.

2. **Obliczenia dla Klasyfikacji Punktów**:
    - Formuła perceptronu: **s = w1 \* x + w2 \* y - threshold**
    - Jeśli **s >= 0**, punkt jest klasyfikowany jako +1; w przeciwnym przypadku jako -1.

3. **Przykładowe Punkty i Oczekiwane Klasy**:
    - **Punkt A (1, 1)**:
      - Obliczenie: **s = 1 \* 1 + 1 \* 1 - 1.5 = 0.5**
      - Wynik: Klasa +1 (poprawna klasyfikacja).
    - **Punkt B (2, 2)**:
      - Obliczenie: **s = 1 \* 2 + 1 \* 2 - 1.5 = 2.5**
      - Wynik: Klasa +1 (poprawna klasyfikacja).
    - **Punkt C (0, -1)**:
      - Obliczenie: **s = 1 \* 0 + 1 \* (-1) - 1.5 = -2.5**
      - Wynik: Klasa -1 (poprawna klasyfikacja).

4. **Podsumowanie**:
    - Wszystkie punkty zostały poprawnie sklasyfikowane na podstawie wyliczonych wag i wartości progowej.

### Przykładowe Wyjście Programu

```plaintext
Perceptron parameters:
w1 = 1.00, w2 = 1.00, threshold = 1.50

Point (1.00, 1.00): Expected Class = 1, Calculated Class = 1
Point (2.00, 2.00): Expected Class = 1, Calculated Class = 1
Point (0.00, -1.00): Expected Class = -1, Calculated Class = -1
