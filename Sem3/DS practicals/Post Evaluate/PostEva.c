#include<stdio.h>
#include<math.h>
#define MAX 30
int top = -1;
int stack[MAX];
char arara[MAX];

int eva(char arr[]);

void push_1(int );
int main()
{
    printf("Enter your Expression \n");
    gets(arara);
   int z = eva(arara);
   printf("Your Expression answer is %d",z);
}

int eva(char exp[])
{   int i=0;
    char ch;
    while(exp[i])
    {
        ch = exp[i];
        if(exp[i]=='*'||exp[i]=='+'||exp[i]=='/'||exp[i]=='-'||exp[i]=='^')
        {
            int x = stack[top--];
            int z =stack[top--];
            switch(ch)
            {
                case '*':  push_1(z*x);
                           break;
                case '+': push_1(z+x);
                          break;
                case '/': push_1(z/x);
                          break;
                case '-': push_1(z-x);
                          break;
                case '^': push_1(pow(z,x));
                          break;
            }
            i++;
            continue;
        }
        push_1(exp[i++]-'0');
    }
    return (stack[top]);
}



void push_1(int c)
{

    stack[++top] = c;
}
