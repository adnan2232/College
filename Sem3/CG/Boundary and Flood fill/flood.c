#include <graphics.h> 
#include <stdio.h> 
 
void flood(int x, int y, int new_col, int old_col) 
{ 
     
    if (getpixel(x, y) == old_col) { 
  
         
        putpixel(x, y, new_col); 
  
        
        flood(x + 1, y, new_col, old_col); 
  
        
        flood(x - 1, y, new_col, old_col); 
  
        
        flood(x, y + 1, new_col, old_col); 
  
        
        flood(x, y - 1, new_col, old_col); 
    } 
} 
  
int main() 
{ 
    int gm, gd = DETECT;
    int top,left,bottom,right;
    int x=51,y=51;
    int newcolor=12,oldcolor=0;
    initgraph(&gd, &gm, "c://turboc3//bgi");




    top = left = 50;
    bottom = right = 300;


    rectangle(left, top, right, bottom);





    flood(x, y, newcolor, oldcolor);
    getch();
    closegraph();
    return 0;
}