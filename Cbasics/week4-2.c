
//浙江大学程序入门c语言
//第4周作业2代码
//注意C语言字符串的处理

/*念整数（5分）
题目内容：
你的程序要读入一个整数，范围是[-100000,100000]。然后，用汉语拼音将这个整数的每一位输出出来。
如输入1234，则输出：
yi er san si
注意，每个字的拼音之间有一个空格，但是最后的字后面没有空格。当遇到负数时，在输出的开头加上“fu”，如-2341输出为：
fu er san si yi

输入格式:
一个整数，范围是[-100000,100000]。

输出格式：
表示这个整数的每一位数字的汉语拼音，每一位数字的拼音之间以空格分隔，末尾没有空格。

输入样例：
-30

输出样例：
fu san ling
 *
 *
 * */
 #include <stdio.h>
 #include <string.h>
 int main(){

        int number1;
		int num;
		int sign=1;
		//int count=0;
		char conn[40]="";
		char  str[40]="";
        scanf("%d",&number1);

		if(number1<0)
		{
			sign=-1;
			printf("%s","fu ");
			number1=-number1;
		}

		do
		{

			num=number1%10;
			number1=number1/10;
			switch(num)
				{ case 0:
						strcpy(str,"ling");
						break;
				  case 1:
					  	strcpy(str,"yi");
					  	break;
				  case 2:
					  	strcpy(str,"er");
					  	break;
				  case 3:
					  	strcpy(str,"san");
					  	break;
				  case 4:
					  	strcpy(str,"si");
					  	break;
				  case 5:
					  	strcpy(str,"wu");
					  	break;
				  case 6:
					  	strcpy(str,"liu");
					  	break;
				  case 7:
					  	strcpy(str,"qi");
					  	break;
				  case 8:
					    strcpy(str,"ba");
					  	break;
				  case 9:
					   	strcpy(str,"jiu");
					  	break;
				}


			if(strlen(conn)==0)
			{
				strcpy(conn,str);
			}
			else
			{
				strcat(str," ");
				strcat(str,conn);
				strcpy(conn,str);
				//conn=str+" "+conn;

			}
		}while(number1!=0);

		printf("%s",conn);
	}

