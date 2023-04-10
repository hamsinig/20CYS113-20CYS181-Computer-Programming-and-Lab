#include<stdio.h>

int main()
{
	int a,b;
	double c;
	printf("Enter height of triangle \n");
	scanf("%d",&a);
	printf("Enter base of triangle \n");
	scanf("%d",&b);
	c=0.5*a*b;
	printf("the area of triangle is %f",c);

	return 0;
}
