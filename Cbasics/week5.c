
//�㽭��ѧ��������c����
//��5����ҵ����

/*
 *�߾���С��
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
       if((a*10)%b==0)                  //���ϣ��˳�ѭ����
        {
            printf("%d",(a*10)/b);
            break;
        }
        else
        {
               int temp=(a*10)/b;  //�̣� ���������
                printf("%d",temp);
                cnt++;
                if(cnt>199)
                {
                    break;
                }
                a=(a*10)%b;         //��������Ϊ������
        }
    }
    printf("\n");

    return 0;
}
