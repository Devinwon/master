
//浙江大学程序入门c语言
//第4周作业1代码

/*
 * 素数和（5分）
题目内容：
我们认为2是第一个素数，3是第二个素数，5是第三个素数，依次类推。
现在，给定两个整数n和m，0<n<=m<=200，你的程序要计算第n个素数到第m个素数之间所有的素数的和，
包括第n个素数和第m个素数。

输入格式:
两个整数，第一个表示n，第二个表示m。

输出格式：
一个整数，表示第n个素数到第m个素数之间所有的素数的和，包括第n个素数和第m个素数。

输入样例：
2 4

输出样例：
15
 *
 * */
 #include <stdio.h>
 int main(){

        int number1;
		int number2;

		int count=0;
		int sum1=0;
		int sum=0;
		int i=2;
		int k;

		scanf("%d %d",&number1,&number2);
		//number2=scanf("%d",&number2);

		for( k=2;;k++)
		{
			i=2;
			do
			{

				if(k%i==0)
				{
					break;
				}
				else
				{
					i++;
				}

			}while(i<k);

			if(i==k)
			{
			count=count+1;
			sum=sum+k;
				if(count==number1)
				{
					sum1=sum-k;
				}

			//System.out.println(k+" is prime:"+count);
			}

			else
			{
			//System.out.println(k +" NOT a Prime");

			}

			if(count>=number2)
			{
				break;
			}
		}
        printf("%d",sum-sum1);

	}

