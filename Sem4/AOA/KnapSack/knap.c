#include<stdio.h>
#include <Windows.h>
#define MAX(x,y) x>y?x:y

enum{true = 1, false = 0}bool;

int knapsack(int items[],int weight[],int W,int profit,int n);

int fractknapsack(int items[],int weight[],int W,int profit,int n);


int main()
{
    int n;
    printf("Enter number of items you have\n");
    scanf("%d",&n);
    int items[n], weight[n],cases,profit,W; 
    printf("Enter the weight of KnapSack \n");
    scanf("%d",&W);
    printf("Enter the items profit and their corresponding weight \n");
    for(int i = 0; i<n; i++)
    {
        scanf("%d %d",&items[i],&weight[i]);
    }
    
    while(true)
    {   
        printf("1.0/1 KnapSack \n2.Fractional Knapsack \n3.Exit\n");
        scanf("%d",&cases);
        switch (cases)
        {
        case 1:
            knapsack(items,weight,W,profit,n);
            
            break;
        case 2:
            fractknapsack(items,weight,W,profit,n);
            break;
        case 3:
            printf("Aborting in 2 seconds");
            Sleep(2000);
            return 0;

        default:
            printf("You entered wrong key please try again\n");
            break;
        }
    }
    return 0;
}

int fractknapsack(int items[],int weight[],int W,int profit,int n)
{
    float dense[n],max_profit = 0,X[n];
    int L=W;
    for(int i=0;i<n;i++)
    {
        dense[i] = items[i]/weight[i];
        X[i] = 0;
    }
    for(int i=1;i<n;i++)
    {

        int mind = dense[i],mini = items[i],minw = weight[i];
        int j = i-1;
        while(j>=0&&dense[j]>mini)
        {
            dense[j+1]=dense[j];
            weight[j+1] = weight[j];
            items[j+1] = items[j];
            j--;
        }
        weight[j+1] = minw; 
        dense[j+1] = mind;
        items[j+1] = mini;
    }
    for(int i=0;i<n;i++)
    {
        if(L-weight[i]>=0)
        {
            max_profit += items[i];
            L -=weight[i];
            X[i] = 1;
        }
        else
        {
            X[i] = dense[i]*L;
            max_profit += (dense[i]*L);
            break;
        }
    }
    printf("Max Profit= %f \n",max_profit);
    printf("Items: \n");
    for(int i=0;i<n;i++)
    {
        if(X[i]==1)
            printf("Profit: %d \t Weight: %d \n",items[i],weight[i]);
        else if(X[i]>0)
            printf("Profit: %f \t Weight: %d \n",X[i],L);
        else 
            break;
    }
    return 0;
}

int knapsack(int items[],int weight[],int W,int profit,int n)
{
    int v[n+1][W+1],X[n],k,max_profit = 0;
    for(int i = 0;i<n;i++)
            {
                    X[i] = 0;
            }

            for(int i = 0;i<=n;i++)
            {
                    v[i][0] = 0;
            }

            for(int i = 0;i<=W;i++)
            {
                v[0][i] = 0;
            }
            for(int i=1;i<=n;i++)
            {
                for(int j=1;j<=W;j++)
                {
                    k = j-weight[i-1];
                    if(k<0)
                        v[i][j] = v[i-1][j];
                    else{
                        v[i][j] = MAX(v[i-1][j],(items[i-1]+v[i-1][k]));
                    }
                }
            }
            max_profit = v[n][W];
            int remain_profit = max_profit,L=n,M=W;
            while(remain_profit>0 || L>0 || M>0)
            {
                if(v[L][M]>v[L-1][M])
                {   
                    if(remain_profit >=v[L][M])
                    {
                        X[L-1]++;
                        remain_profit -= items[L-1];
                        L--;
                    }
                    else
                        M --;
                }
                else
                {
                    L--;
                }
                
            }
            max_profit = v[n][W];
            printf("Max Profit= %d \n",max_profit);
            printf("Items: \n");
            for(int i=0;i<n;i++)
            {
                if(X[i]==1)
                    printf("Profit: %d \t Weight: %d \n",items[i],weight[i]);
            }
}


