
//�㽭��ѧ��������c����
//��4����ҵ1����

/*
 * �����ͣ�5�֣�
��Ŀ���ݣ�
������Ϊ2�ǵ�һ��������3�ǵڶ���������5�ǵ������������������ơ�
���ڣ�������������n��m��0<n<=m<=200����ĳ���Ҫ�����n����������m������֮�����е������ĺͣ�
������n�������͵�m��������

�����ʽ:
������������һ����ʾn���ڶ�����ʾm��

�����ʽ��
һ����������ʾ��n����������m������֮�����е������ĺͣ�������n�������͵�m��������

����������
2 4

���������
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

