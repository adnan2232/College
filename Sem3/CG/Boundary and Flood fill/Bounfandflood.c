#include<graphics.h>

#include<dos.h>  

#include<conio.h>   

void boundaryFill8(int x, int y, int fill_color,int boundary_color) 

{ 

    if(getpixel(x, y) != boundary_color && 

       getpixel(x, y) != fill_color) 

    { 

        putpixel(x, y, fill_color); 

        boundaryFill8(x + 1, y, fill_color, boundary_color); 

        boundaryFill8(x, y + 1, fill_color, boundary_color); 

        boundaryFill8(x - 1, y, fill_color, boundary_color); 

        boundaryFill8(x, y - 1, fill_color, boundary_color); 

        boundaryFill8(x - 1, y - 1, fill_color, boundary_color); 

        boundaryFill8(x - 1, y + 1, fill_color, boundary_color); 

        boundaryFill8(x + 1, y - 1, fill_color, boundary_color); 

        boundaryFill8(x + 1, y + 1, fill_color, boundary_color); 

    } 

}  

void main() 

{ 

    int gd = DETECT, gm; 

    initgraph(&gd, &gm, "c:\\Turboc3\\bgi");   

    

    rectangle(50, 50, 100, 100);   



    boundaryFill8(55, 55, 4, 15);   

    delay(10000);   

    getch();   



    closegraph(); 

}  