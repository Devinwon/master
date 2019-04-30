
//浙江大学程序入门c语言
//第5周作业代码

/*
 *高精度小数
 *
 * */
#include <stdio.h>
int main()
{
    int a,b;
    scanf("%d/%d",&a,&b);

    int cnt=0;
    printf("0.");
    while(1)
    {
       if((a*10)%b==0)                  //除断，退出循环；
        {
            printf("%d",(a*10)/b);
            break;
        }
        else
        {
               int temp=(a*10)/b;  //商， 保留输出；
                printf("%d",temp);
                cnt++;
                if(cnt>199)
                {
                    break;
                }
                a=(a*10)%b;         //余数，作为被除数
        }
    }
    printf("\n");

    return 0;
}
