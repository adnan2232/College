#include<stdio.h>

void quicksort(int arr[],int low,int high);
int pivot(int arr[],int start,int pi);
int main(){
    int n;
    printf("Enter number of elements you have in your array\n");
    scanf("%d",&n);
    int arr[n];
    printf("Enter Elements of your array \n");
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
        printf("\n");
    }
    quicksort(arr,0,n-1);
    for(int i=0;i<n;i++){
        printf("%d \t",arr[i]);
    }
    return 0;
}


void quicksort(int arr[],int low,int high){
    if(low<high){
        int pi = pivot(arr,low,high);
        quicksort(arr,low,pi-1);
        quicksort(arr,pi+1,high);
    }
    else
        return;
}

int pivot(int arr[],int low,int pi){
    int i = (low-1);
    int temp;
    for(int j=low;j<pi;j++)
    {
        if(arr[j]<arr[pi])
        {
            i++;
            temp = arr[j];
            arr[j] = arr[i];
            arr[i] = temp;
        }
    }
    temp = arr[i+1];
    arr[i+1] = arr[pi];
    arr[pi] = temp;
    return (i+1);
}
