%{
    #include<stdio.h>
%}
%%

^[0-9]+$ {
    if(atoi(yytext)%2) printf("%s is odd\n",yytext);
    else printf("%s is even\n",yytext);
}
[a-zA-Z0-9_]+ {printf("Please enter a number");}

%%

int yywrap(){
    return 0;
}

int main(){
    printf("Enter your input from here: ");
    yylex();
}