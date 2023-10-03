#include<stdio.h>
#include<sys/stat.h>
int main(){
    FILE *fptr;
    struct stat file_info ;
    if( stat("a.txt", &file_info)==0){
        printf("file size= %ld",file_info.st_size);
        printf("file last access time= %lo",file_info.st_atime);
    }
    else{
        printf("error");
    }
}