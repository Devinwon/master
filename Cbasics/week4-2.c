
//�㽭��ѧ��������c����
//��4����ҵ2����
//ע��C�����ַ����Ĵ���

/*��������5�֣�
��Ŀ���ݣ�
��ĳ���Ҫ����һ����������Χ��[-100000,100000]��Ȼ���ú���ƴ�������������ÿһλ���������
������1234���������
yi er san si
ע�⣬ÿ���ֵ�ƴ��֮����һ���ո񣬵��������ֺ���û�пո񡣵���������ʱ��������Ŀ�ͷ���ϡ�fu������-2341���Ϊ��
fu er san si yi

�����ʽ:
һ����������Χ��[-100000,100000]��

�����ʽ��
��ʾ���������ÿһλ���ֵĺ���ƴ����ÿһλ���ֵ�ƴ��֮���Կո�ָ���ĩβû�пո�

����������
-30

���������
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

