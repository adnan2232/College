%{
int lines=0;
int chars=0;
int tabs=0;
int words=0;
int blanks=0;
int num=0;
%}

%%
""  ++words;++blanks;
\t {++tabs;++words;++blanks;}
\n {++words;++lines;}
.  ++chars;
([0-9])+ ++num;
end return 0;
%%

int yywrap() {}
int main(int argc,char **argv)

{
extern FILE *yyin,*yyout;
yyin=fopen("abc.text","r");
yyout=fopen("output.text","w"); 
yylex();
printf("NUMBER OF LINES: %d\n NUMBER OF CHARACTERS: %d\n NUMBER OF TABS: %d\n NUMBER OF WORDS: %d\n NUMBER OF BLANKS: %d\n NUMBER OF NUMBERS:%d\n",lines,chars,tabs,words,blanks,num);
return 0;
}