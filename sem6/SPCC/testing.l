%{
	#include<stdio.h>
%}

%%

	"Hi" {printf("Hello");}
	"Hello" {printf("Hi");}
	.* {printf("I am only capable of Hi and Hello");}
%%

int main(){
	printf("Program starts here");

	yylex();

}

int yywrap(){
	retrun 1;
}

