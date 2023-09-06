#include<stdio.h>
#include<math.h>
int main(){
    int arr[20]={4,65,6,78,3,5,7,99,10};
    // int arr2[10]={};
    int max=-__INT_MAX__;
    int max2=-__INT_MAX__;
    int len=sizeof(arr)/sizeof(int);
    for(int i=0;i<len;i++){
        if (max<arr[i]){
            max=arr[i];
            max2=arr[i];
            // arr2[i]=max;
            // printf("%d \n\n",max);
        }
    }
    printf("max= %d\n",max);

    for(int i=0; i<len; i++)
    {
        if(arr[i] > max)
        {
            /*
             * If current element of the array is first largest
             * then make current max as second max
             * and then max as current array element
             */
            max2 = max;
            max = arr[i];
        }
        else if(arr[i] > max2 && arr[i] < max)
        {
            /*
             * If current array element is less than first largest
             * but is greater than second largest then make it
             * second largest
             */
            max2 = arr[i];
        }
    }
    printf("max= %d\n",max);
    printf("2nd max= %d\n",max2);

    // int lent=sizeof(arr2)/sizeof(int);
    // for (int i=0;i<lent;i++){
    //     printf("%d ",arr2[i]);
    // }
    // printf("2nd max= %d",arr2[3]);
}