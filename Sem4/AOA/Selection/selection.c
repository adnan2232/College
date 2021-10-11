#include<stdio.h>
#include<conio.h>

void select(int arr[],int z);

int main()
{
    int z;
    printf("Enter size of your array \n");
    scanf("%d",&z);
    int arr[z];
    printf("\nEnter your array elements: ");
    for (int i = 0;i<z;i++)
    {
        scanf("%d",&arr[i]);
    }
    select(arr,z);
    printf("\nArray after sorting:");
    for (int i = 0;i<z;i++)
    {
        printf("\t%d",arr[i]);
    }
    getch();	
    return 0;
}

void select(int arr[],int z)
{
    for(int i=0;i<z;i++)
    {
        int min=i;
        for(int j = i+1;j<z;j++)
        {
            if (arr[j]<arr[min])
                min=j;
        }
        int temp = arr[min];
        arr[min] = arr[i];
        arr[i] = temp;
    }
}
