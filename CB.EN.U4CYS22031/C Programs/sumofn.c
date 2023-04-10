#include<stdio.h>
int main()
{
	int n,sum;
	printf("enter the integer to find sum \n: ");
	scanf("%d", &n);
	sum=(n*(n+1))/2;
	printf("the sum of integers till %d is %d",n,sum);
	return 0;
}
