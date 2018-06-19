#include <stdio.h>
//#include "Conio.h"
int main(void)
{    int m,n,temp,x,y;
     int max,a;
     //printf("Enter a fraction :(a/b)");
     scanf("%d/%d",&m,&n);
     x = m;y = n;
   if (m < n)
     {
          temp = m;
          m = n;
          n = temp;
     }
     if (n == 0)
          max = m;
     else
     {
     while(1)
          {
          a = m % n;
          m = n;
          n = a;
          max = m;
          if(n == 0)
                     break;
          }
      }
      x /= max;
      y /= max;
      printf("%d/%d",x,y);
  //getch();
  return 0;
}
