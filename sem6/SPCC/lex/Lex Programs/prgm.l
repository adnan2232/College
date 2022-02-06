%{
#include<stdio.h>
/*Global variables*/
int tchar=0,tword=0,tspace=0;		
%}


%%


" " {tspace++;tword++;}				
[\t\n] tword++;						
[^\n\t] tchar++;

%%

/*call the yywrap function*/
int yywrap()
{
return 1;
}

int main()
{

yyin=fopen("in.txt","r");
yylex();							
printf("Number of character: %d \n Number of words: 
%d \n Number of spaces: %d \n",tchar,tword,tspace);

return 0;
}