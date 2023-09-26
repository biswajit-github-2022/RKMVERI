#include<stdio.h>
#include<string.h>
int main(){
    FILE* fptr;
 
    // opening the file in read mode
    fptr = fopen("donut.c", "r");
    // printf("%p",fptr);
    char memory[1000];
    int  num= fread(memory,1,300,fptr);

    // printf("%s",memory);
    int i=0;
    while(strlen(memory)>i){
        if(*(memory)+i =='A'){
            printf("A found\n");
            break;
        }
        i+=1;
    }

    // char * a=strchr(memory,'A');
    // printf("%s\n",a); 

    for (int j=0;j<strlen(memory);j++){
        if (strchr(memory,'A')){
            printf("A is found\n");
            break;
        }
    }

    // char * a=strstr(memory,"sin");
    // printf("%s\n",a); 

    for (int j=0;j<strlen(memory);j++){
        if (strstr(memory,"sin")){
            printf("sin is found\n");
            break;
        }
    }

    

}