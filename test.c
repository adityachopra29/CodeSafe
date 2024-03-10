#define NULL 0
#include <stdio.h>

int main()
{
   int x = 4;
   int y = NULL;
   int *p = 0;
   int v = 5 * *p;
   // printf("Check %d", v);

   return 0;
}