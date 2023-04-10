#include<stdio.h>
int main()
{
	printf("This is a calculator: ");
	int a,b;
	double c;
	printf("Enter number 1 ");
	scanf("%d",&a);
	printf("Enter number 2 ");
	scanf("%d",&b);
	printf("The sum is f %d \n",a+b);
	printf("The difference is %d \n",a-b);
	printf("the product is %d \n",a*b);
	c=a/b;
	printf("The division of the two numbers is %f \n",c);
	printf("The modulo operation is %d \n",a%b);
	return 0;
}
