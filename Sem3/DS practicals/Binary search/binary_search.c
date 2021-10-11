#include<stdio.h>

#define MAX 6

int Q[MAX];
int rear =-1;
int front=-1;
void Enqueue(int);
void Dequeue();
void Display();

int main()
{
    int ch,n;
    do
    {
        printf("1.enqueue 2.dequeue 3.Display 4.Exit \n");
        scanf("%d",&ch);
        switch(ch)
        {
        case 1: printf("enter element you want to Enqueue \n");
                scanf("%d",&n);
                Enqueue(n);
                break;
        case 2: Dequeue();
                break;
        case 3: Display();
                break;
        case 4: printf("Exiting....");
                break;
        default: printf("Please Try again");
        }

    }while(ch!=4);
    return 0;
}


void Enqueue(int n)
{
    if((rear == MAX-1 && front == 0) || front == rear+1)
    {
        printf("Queue is Full");
        return ;
    }
    if(rear==MAX-1&&front!=0)
    {
        rear =0;
        Q[rear] = n;
        return;
    }
    if(front==-1)
        front++;
    Q[++rear]=n;
    return;
}

void Dequeue()
{
    if(front==-1)
    {
        printf("No element in queue");
        return;
    }
    if(front==MAX-1)
    {
        printf("Dequeue element  is %d",Q[front]);
        front = 0;
        return;
    }
    printf("Dequeue element  is %d",Q[front++]);
}

void Display()
{
    if (front>rear)
    {
        int i = front;
        while(i<MAX)
            printf("Element is %d",Q[i++]);
        i=0;
        while(i<=rear)
            printf("Element is %d",Q[i++]);
    }
    else{
        int i=front;
        while(i<=rear)
            printf("Element is %d ",Q[i++]);
    }
}
