
//浙江大学程序入门c语言
//第7周作业2代码

/*
寻找鞍点
*/
#include <stdio.h>
#include <stdbool.h>
int main()

{

    int N;
    scanf("%d",&N);
    int num[N][N];
    int Xmax;

    int X,Y;

    bool  isFound;
    //init num

    for(int i=0;i<N;i++)

        {

            for(int k=0;k<N;k++)

            {

                scanf("%d",&num[i][k]);

            }

        }

   int i=0;

        do

        {

           isFound=true;

           Xmax=num[i][0];

           X=i;

           Y=0;

           //find maxnum in line i

            for(int k=1;k<N;k++)

            {

               if(num[i][k]>Xmax)

               {

                   Xmax=num[i][k];

                   Y=k;

               }

            }

           // printf("Xmax in line %d=%d\n",i,Xmax);

           //列中比较

            for(int j=0;j<N;j++)

            {

                if(num[j][Y]<Xmax)

                {

                    isFound=false;

                    break;

                }

            }

        }while(++i<N&&!isFound);

        //printf("last i=%d\n",i);

            if(isFound)

            {

                printf("%d %d",X,Y);

            }

            else

            {

               printf("NO");

            }

    return 0;

}
