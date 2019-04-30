
//浙江大学程序入门c语言
//第7周作业1代码

/*
多项式加法
*/
#include <stdio.h>
#include <stdbool.h>

int main()
{
    const int num=101;
    int m[num];         //存储幂
    int c[num];         //存储系数
   bool isnull=true;
    for(int i=0;i<=num;i++)
    {
        m[i]=0;
        c[i]=0;
    }

    int mx=0,cx=0;            //mx幂,cx系数
    int cnt=0;
    int mymax=0;
    int myend=0;
    do
    {
       scanf("%d %d",&mx,&cx);
       cnt++;
       if(cnt==1)
       {
           mymax=mx;
       }
       m[mx]=mx;          //利用下表与幂的对应性，存储
       c[mx]+=cx;
       if(mx==0)
       {
           myend++;
       }

    } while (myend!=2);        //mx为0，即幂为0时退出，录入完毕

    for(int i=mymax;i>1;i--)
    {
       if(c[i]!=0&&c[i]!=1)                          //系数为0时自动进入下一个幂次
       {
            if(c[i]>0)
            {
                if(isnull)
                {
                    printf("%dx%d",c[i],m[i]);  //首项为+时符号省掉
                    isnull=false;
                }

                else
                {
                    printf("+%dx%d",c[i],m[i]); //非首项为+时符号不省掉
                    isnull=false;
                }
            }
            else
            {

                    printf("%dx%d",c[i],m[i]);     //为-需要输出；
                    isnull=false;
            }
       }
    else if(c[i]==1)    //系数为1时不用输出系数1
    {
        if(isnull)
        {
            printf("x%d",m[i]);
            isnull=false;
        }
        else
        {
            printf("+x%d",m[i]);
            isnull=false;
        }
    }
    //系数为0时不输出即可
    }

        if(c[1]!=0)         //幂数为1时单独考虑，无x1
        {

            if(c[1]>0&&c[1]!=1)
            {
                if(isnull)
                {
                   printf("%dx",c[1]);
                   isnull=false;
                }
                else
                {
                    printf("+%dx",c[1]);
                    isnull=false;
                }

            }

            else if(c[1]==1)
            {
                if(isnull)
                {
                printf("x",c[1]);
                isnull=false;
                }
                else
                {
                printf("+x",c[1]);
                isnull=false;
                }

            }
            else if(c[1]==-1)
            {
                printf("-x",c[1]);
                isnull=false;
            }

            else if(c[1]<0&&c[1]!=-1)
            {
                   printf("%dx",c[1]);
                   isnull=false;
            }

        }

    if(c[0]!=0)         //幂数为0时单独考虑，无x
    {

        if(c[0]>0)
        {
            if(isnull)
            {
                printf("%d",c[0]);
                isnull=false;
            }
            else
            {
                printf("+%d",c[0]);
                isnull=false;
            }

        }
        else
        {
                printf("%d",c[0]);
                isnull=false;
        }

    }

    if(isnull)
    {
        printf("0");
    }

    return 0;
}

