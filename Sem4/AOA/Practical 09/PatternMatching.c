#include <stdio.h>
#include <string.h>

int main (){
   char txt[] = "1011101110";
   char pat[] = "111";
   int M = strlen (pat);
   int N = strlen (txt);
   int i;
   for(i = 0; i <= N - M; i++){
      int j;
      for (j = 0; j < M; j++)
         if (txt[i + j] != pat[j])
      break;
      if (j == M)
         printf ("Pattern matches at index %d \n", i);
   }
      

   return 0;

}
