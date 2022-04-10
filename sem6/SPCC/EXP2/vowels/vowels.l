%{    
    #include<string.h>
    int vowels = 0, not_vowels = 0;
%}
%%
[aeiouAEIOU] {vowels++; printf("%s vowel is triggered.\t\t\t Total vowels till now: %d\n",yytext,vowels);}
[\t ] /*Skipping whitespaces and tab*/;
. {not_vowels++; printf("%s normal character is triggered.\t Total normal charcaters till now: %d\n",yytext,not_vowels);}
\n {printf("Total vowels: %d \t Total characters: %d \n",vowels,not_vowels); return 0;}
%%

int yywrap(){
    return 0;
}

int main(){
    printf("Pass the string to count total vowels and normal characters in it: ");
    yylex();
    
}

