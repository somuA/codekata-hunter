#include<stdio.h>
void main()
{
char ch;
int a,i;
while(scanf("%c%d",&ch,&a)>0)
{
    if (a==1)
    {
for(i=0;i<a;i++)
printf("%c%d",ch,a);
    }
else{
        for(i=0;i<a;i++)
printf("%c",ch);

}
}
}
