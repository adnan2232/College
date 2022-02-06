%{
#include<stdio.h>
int i;
%}

%%
">"|"<"|"<="|">="|"="|"!=" {printf("Relational operator =%s",yytext);}
.* {printf ("wrong");}
%%
int yywrap(){}

/* Driver code */
int main()
{

	yylex();
	return 0;
}
