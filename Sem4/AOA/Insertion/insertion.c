#include<stdio.h>
#include<conio.h>

void insert(int arr[],int z);

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
    insert(arr,z);
    printf("\nArray after sorting:");
    for (int i = 0;i<z;i++)
    {
        printf("\t%d",arr[i]);
    }
    getch();
    return 0;
}

void insert(int arr[],int z)
{
    for(int i=1;i<z;i++)
    {

        int min = arr[i];
        int j = i-1;
        while(j>=0&&arr[j]>min)
        {
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1] = min;

    }
}
