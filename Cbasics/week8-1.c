
//�㽭��ѧ��������c����
//��8����ҵ1����
/*
���ʳ��ȣ�4�֣�
��Ŀ���ݣ�
��ĳ���Ҫ����һ���ı��������Կո�ָ�Ϊ���ɸ����ʣ��ԡ�.��������
��Ҫ��������ı���ÿ�����ʵĳ��ȡ�����ĵ����������޹أ����԰������ַ��ţ�
���硰it's����һ�����ʣ�����Ϊ4��ע�⣬���п��ܳ��������Ŀո�

�����ʽ:
������һ���и���һ���ı����ԡ�.����������β�ľ�Ų��ܼ��������һ�����ʵĳ����ڡ�

�����ʽ��
��һ������������ı���Ӧ�ĵ��ʵĳ��ȣ�ÿ������֮���Կո��������ĩû�����Ŀո�

����������
It's great to see you here.

���������
4 5 2 3 3 4

*/
 #include <stdio.h>
 #include <string.h>
 #include <stdbool.h>
 int main(){
        char word[10000]="";
		//length of every word
        bool prnflag=false;

        while(true)
        {
           scanf("%s",word);
           //printf("%s\n",word);
           //printf("lenofword=%d\n",strlen(word));
           if (word[strlen(word)-1]!='.')
           {
                if (prnflag)
               {
                    printf(" %d",strlen(word));
               }
                else
                {
                    printf("%d",strlen(word));
                    prnflag=true;
                }
           }

           else
           {
                if (prnflag)
               {
                    if (strlen(word)>1)
                        printf(" %d",strlen(word)-1);
               }
                else
                {

                    if (strlen(word)>1)
                        printf("%d",strlen(word)-1);
                    prnflag=true;
                }
                break;

           }
        }

	}

