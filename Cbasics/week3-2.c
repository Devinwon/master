
//浙江大学程序入门c语言
//第3周作业2代码

/*
 * 见网站说明，比较长
 *
 *
 * */
 #include <stdio.h>
 #include <math.h>
 int main(){

		int number;
		int num;
		int count=1;
		int factor=0;

		//Scanner input =new Scanner(System.in);
		//number=input.nextInt();
        scanf("%d",&number);
		do{
			num=number%10;

			if((num+count)%2==0)
			{
				//System.out.println(factor+":"+count);
				factor=factor+(int)(pow(2,count-1));
			}

			number=number/10;
			count=count+1;

		}while(number>0);

		printf("%d",factor);
		//System.out.println(factor);
	}

