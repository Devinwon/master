//c���Գ�������
//��ĩ������
 #include <stdio.h>
 #include <string.h>

 int min(int a,int b)
 {
     return a<b?a:b;
 }
  int max(int a,int b)
 {
     return a>b?a:b;
 }
 int maxfactor(int a,int b)
 {
       int in=min(a,b);
       int ax=max(a,b);
       while (in!=0){
           int t=ax;
           ax=in;
           in=t%in;
       }
    return ax;
 }

 int main(){
    int x;
    int y;
    //ע��scanf()���治Ҫ��\n,����������û���ҳ���
    scanf("%d/%d",&x,&y);
   // printf("%d %d\n",x,y);

    int t=maxfactor(x,y);
    x=x/t;
    y=y/t;
    printf("%d/%d",x,y);

    //printf("%d",maxfactor(1,6));

}

