#include<stdio.h>

void merge(int arr[],int low,int mid,int high);
void mergesort(int arr[],int low,int high);

int main(){
    int n;
    printf("Enter number of elements you have in your array\n");
    scanf("%d",&n);
    int arr[n];
    printf("Enter Elements of your array \n");
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    mergesort(arr,0,n-1);

    printf("Sorted array: \n");
    for(int i=0;i<n;i++){
        printf("%d \t",arr[i]);
    }
    return 0;
}

void mergesort(int arr[],int low,int high)
{
    if(low<high)
    {
        int mid = (low+high)/2;
        mergesort(arr,low,mid);
        mergesort(arr,mid+1,high);
        merge(arr,low,mid,high);
    }
}

void merge(int arr[],int low,int mid,int high)
{
    int n1 = mid-low+1, n2 =high-mid;
    int L1[n1],L2[n2];
    for(int i=0;i<n1;i++)
        L1[i] = arr[i+low];
    for(int i=0;i<n2;i++)
        L2[i] = arr[i+mid+1];
    int i=0,j=0;
    for(int k=low;k<=high;k++)
    {
        if(L1[i]>L2[j])
        {
            arr[k] = L2[j++];
        }
        else{
            arr[k] = L1[i++];
        }
    }
}