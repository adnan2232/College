%{
int nlines,nwords,nchars;
%}

%%
\n {
	nchars++;nlines++; fprintf(yyout,"%s",yytext);
	}
 
[^ \n\t]+ {nwords++, nchars=nchars+yyleng; fprintf(yyout,"%s",yytext);}
. {nchars++; fprintf(yyout,"%s",yytext);}
%%
int yywrap(void)  
{
 return 1;
}
int main(int argc, char*argv[]) 
{
	yyin = fopen(argv[1],"r");
    yyout = fopen(argv[2],"w");
 yylex();
 fclose(yyin);
 fclose(yyout);
 printf("Lines = %d\nChars=%d\nWords=%d",nlines,nchars,nwords);

 return 0;
} 