#include<stdio.h>
 
int main()
{
	int a,b,c;
	printf("enter the variable1: \n");
	scanf("%d",&a);
	printf("enter the variable2; \n");
	scanf("%d",&b);
	printf("the first variable is %d and second variable is %d \n",a,b);
	printf("swap is occurring \n");
	c=a;
	a=b;
	b=c;
	printf("now the first variable is %d and second variable is %d \n",a,b);

	return 0;
}



