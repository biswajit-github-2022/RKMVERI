#include<stdio.h>
#include<stdlib.h>
int main(){
    int milk_price[]={50,60,70,80,90};
    int i =0,sum=0;
    int len=sizeof(milk_price)/sizeof(int);
    while(i<len){
        sum+=milk_price[i];
        i+=1;
    }
    printf("sum=%d",sum);

    sum=0;
    i=0;
    while(i<len){
        sum+=milk_price[i];
        i=i+2;
    }
    printf("odd sum=%d",sum);
}