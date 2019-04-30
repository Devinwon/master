
//浙江大学程序入门c语言
//第6周作业1代码

/*分解质因数（5分）
题目内容：
每个非素数（合数）都可以写成几个素数（也可称为质数）相乘的形式，
这几个素数就都叫做这个合数的质因数。比如，6可以被分解为2x3，而24可以被分解为2x2x2x3。

现在，你的程序要读入一个[2,100000]范围内的整数，然后输出它的质因数分解式；
当读到的就是素数时，输出它本身。

提示：可以用一个函数来判断某数是否是素数。
输入格式:
一个整数，范围在[2,100000]内。

输出格式：
形如：
n=axbxcxd
或
n=n
所有的符号之间都没有空格，x是小写字母x。abcd这样的数字一定是从小到大排列的。

输入样例：
18

输出样例：
18=2x3x3
 *
 *
 * */
 #include <stdio.h>


#include <stdbool.h>

bool isPrime(int a)

{

    bool isp=true;

    for(int i=2;i<a;i++)

    {

        if(a%i==0)

        {

            isp=false;

            break;

        }

    }

    return isp;

}

int main()

{

     int n;

    scanf("%d",&n);

    //判断输入的数字是否为素数；是的话直接输出；否则输出他的因子

    if(isPrime(n))

    {

        printf("%d=%d",n,n);

    }




    else

    {

        int ncopy=n;

        printf("%d=",n);    //n=

        int temp=2;

        do

        {

            if(isPrime(temp)&&ncopy%temp==0)    //存在因子

            {

                ncopy=ncopy/temp;           //改变被除数

                printf("%dx",temp);




            }

            else                            //被除数，有因子，上面没有找到，改变继续找

            {

                temp++;

            }




        }while(!isPrime(ncopy));    //被除数为素数结束循环




        printf("%d",ncopy);

    }

    return 0;

}

