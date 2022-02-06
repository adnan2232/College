%{
	#include<stdio.h>
%}

%%
"Hii" {printf("Bye");}
.* {printf ("Wrong");}
%%
int main()
{
printf("Enter input: ");
yylex();
}

int yywrap()
{

	return 1;
}