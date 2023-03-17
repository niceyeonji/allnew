#include <stdio.h>

int main() {
  int x=1;

  if(*(char *)&x = 1) {
    printf(" Result : %d \n", *(char *)&x);
    printf(" This system is Little-Endian \n");
  } else {
    printf(" Result : %d \n", *(char *)&x);
    printf(" This system is Big-Endian \n");
  }
}
