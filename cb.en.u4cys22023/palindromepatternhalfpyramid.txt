#include<stdio.h>
int main(){
    printf("Enter a value to print a palindrome pyramid \n");
    int inp1;
    scanf("%d",&inp1);
    printf("*\n*");
    for(int i=1;i<=inp1;i++){
        for(int w=1;w<i;w++){
            if(w==1){
                printf("*%d",w);
            }
            else{
                printf("%d",w);
            }
            
        }
        
        for(int r=i;r>=1;r--){
            if(r==1){
                printf("%d*",r);
            }
            else{
                printf("%d",r);
            }
            
        }
        
       printf("\n");
    }

    for(int j=inp1-1;j>=1;j--){
        for(int w=1;w<=j;w++){
            if(w==1){
                printf("*%d",w);
            }
            else{
                printf("%d",w);
            }
        }
        
        for(int r=j-1;r>=1;r--){
            if(r==1){
                printf("%d*",r);
            }
            else{
                printf("%d",r);
            }
            
        }
        if (j!=1){
             printf("\n");
        }
       
       
    }
     printf("*\n*");
}
