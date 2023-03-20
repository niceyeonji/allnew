#include <stdio.h>
#include "libcheckeod.h"

void main() {
  int n;
  printf("Input Number : ");
  scanf("%d", &n);
  if(checkeod(n) == 0)
    printf("%d is even number~!! \n", n);
  else
    printf("%d is odd number~!! \n", n);
}
