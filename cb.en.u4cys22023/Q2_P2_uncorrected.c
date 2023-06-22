#include<stdio.h>
int main(){
int temp=1;
for (int i=0;i<8;i++){
  for(int j=1;j<=15;j++){
     if(i+j==8||j-i==8){
        printf("%d",1);
        }
     else if(j-1>8||i+j==8)
         printf("  ");




