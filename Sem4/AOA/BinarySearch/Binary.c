#include<stdio.h>
#include<conio.h>

int binarysearch(int arr[],int low,int high,int search);


int main()
{
    int z,search,position;

    printf("Enter size of your array \n");
    scanf("%d",&z);

    int arr[z];

    printf("\nEnter your array elements in ascending order: ");

    for (int i = 0;i<z;i++)
    {
        scanf("%d",&arr[i]);
    }
    printf("Enter the element you want to search in array \n");

    scanf("%d",&search);

    position = binarysearch(arr,0,z-1,search);
    
    if(position == -1)
    {
        printf("Your element is not in array");
    }
    else
    {
        printf("Your element %d is present in array at position: %d",search,(position+1));
    }
   
    getch();
    return 0;
}


int binarysearch(int arr[],int low,int high,int search)
{
    if(low<=high)
    {
        int mid = (low+high)/2;
        if(arr[mid] == search)
            return mid;
        else if(arr[mid] > search)
            return binarysearch(arr,low,mid-1,search);
        else
            return binarysearch(arr,mid+1,high,search); 
    }
    else
        return -1;
}



