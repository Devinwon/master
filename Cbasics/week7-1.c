
//�㽭��ѧ��������c����
//��7����ҵ1����

/*
����ʽ�ӷ�
*/
#include <stdio.h>
#include <stdbool.h>

int main()
{
    const int num=101;
    int m[num];         //�洢��
    int c[num];         //�洢ϵ��
   bool isnull=true;
    for(int i=0;i<=num;i++)
    {
        m[i]=0;
        c[i]=0;
    }

    int mx=0,cx=0;            //mx��,cxϵ��
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
       m[mx]=mx;          //�����±����ݵĶ�Ӧ�ԣ��洢
       c[mx]+=cx;
       if(mx==0)
       {
           myend++;
       }

    } while (myend!=2);        //mxΪ0������Ϊ0ʱ�˳���¼�����

    for(int i=mymax;i>1;i--)
    {
       if(c[i]!=0&&c[i]!=1)                          //ϵ��Ϊ0ʱ�Զ�������һ���ݴ�
       {
            if(c[i]>0)
            {
                if(isnull)
                {
                    printf("%dx%d",c[i],m[i]);  //����Ϊ+ʱ����ʡ��
                    isnull=false;
                }

                else
                {
                    printf("+%dx%d",c[i],m[i]); //������Ϊ+ʱ���Ų�ʡ��
                    isnull=false;
                }
            }
            else
            {

                    printf("%dx%d",c[i],m[i]);     //Ϊ-��Ҫ�����
                    isnull=false;
            }
       }
    else if(c[i]==1)    //ϵ��Ϊ1ʱ�������ϵ��1
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
    //ϵ��Ϊ0ʱ���������
    }

        if(c[1]!=0)         //����Ϊ1ʱ�������ǣ���x1
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

    if(c[0]!=0)         //����Ϊ0ʱ�������ǣ���x
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

