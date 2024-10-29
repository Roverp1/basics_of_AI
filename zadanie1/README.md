<div align="center">

| Podstawy sztucznej inteligencji | laboratorium |
|---------------------------------|--------------|
| SAN                             |              |
| Autor                           | Yaroslav Zubakha |
| E-mail                          | 121546@student.san.edu.pl / yar.zubaha@proton.me |
| Nr albumu                       | 121546       |
| Data                            | 29.10.2024   |
| Wersja                          | 1.0          |

<br>

# **Zadanie nr 1** 

</div>

<br>

> ## Opis zadania
- Program rozwiązujący problem wież Hanoi.
- Minimum 3 krążki
- Przebieg obliczeń (nie wystarczy sam kod)

<br>

> ## Kod algorytmu
Znajduje się w pliku `./121546_PSI_zadanie1.c`

<br>


> ## Przebieg obliczeń

The goal is to move all disks from rod **A** to rod **C** using rod **B** as an auxiliary.

1. **Move 2 disks** from rod **A** to rod **B** using rod **C** as auxiliary.
    - 1.1. **Move 1 disk** from rod **A** to rod **C** using rod **B** as auxiliary.
        - Output: `Move disk 1 from rod A to rod C`
    - 1.2. **Move disk 2** from rod **A** to rod **B**.
        - Output: `Move disk 2 from rod A to rod B`
    - 1.3. **Move 1 disk** from rod **C** to rod **B** using rod **A** as auxiliary.
        - Output: `Move disk 1 from rod C to rod B`

2. **Move disk 3** from rod **A** to rod **C**.
    - Output: `Move disk 3 from rod A to rod C`

3. **Move 2 disks** from rod **B** to rod **C** using rod **A** as auxiliary.
    - 3.1. **Move 1 disk** from rod **B** to rod **A** using rod **C** as auxiliary.
        - Output: `Move disk 1 from rod B to rod A`
    - 3.2. **Move disk 2** from rod **B** to rod **C**.
        - Output: `Move disk 2 from rod B to rod C`
    - 3.3. **Move 1 disk** from rod **A** to rod **C** using rod **B** as auxiliary.
        - Output: `Move disk 1 from rod A to rod C`

### Full Output

When you run the program with `number_of_plates = 3`, the output will be:

```plaintext
Move disk 1 from rod A to rod C
Move disk 2 from rod A to rod B
Move disk 1 from rod C to rod B
Move disk 3 from rod A to rod C
Move disk 1 from rod B to rod A
Move disk 2 from rod B to rod C
Move disk 1 from rod A to rod C
