#include <stdio.h>

void TOH(int n, char start_rod, char end_rod, char middle_rod);

int main(void) {
  int number_of_plates = 3;

  TOH(number_of_plates, 'A', 'C', 'B');

  return 0;
}

void TOH(int n, char start_rod, char end_rod, char middle_rod) {
  if (n > 0) {
    TOH(n - 1, start_rod, middle_rod, end_rod);
    printf("Move disk %d from rod %c to rod %c\n", n, start_rod, end_rod);
    TOH(n - 1, middle_rod, end_rod, start_rod);
  }
}
