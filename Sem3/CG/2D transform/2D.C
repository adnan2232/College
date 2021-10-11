#include <graphics.h>
#include <stdlib.h>
#include <stdio.h>
#include <conio.h>
#include<math.h>
void main()
{
	    int gm;
	    int gd=DETECT;
	    int x1,x2,x3,y1,y2,y3;
	    int nx1,nx2,nx3,ny1,ny2,ny3;
	    float sx,sy,xt,yt,r;
	    float t;
	    int c;
	    initgraph(&gd,&gm,"c:\\turboc3\\bgi");
	    printf("\t Program for basic transactions");
	    printf("\n\t Enter the points of triangle");
	    setcolor(1);
	    scanf("%d%d%d%d%d%d",&x1,&y1,&x2,&y2,&x3,&y3);
	    line(x1,y1,x2,y2);
	    line(x2,y2,x3,y3);
	    line(x3,y3,x1,y1);
	    getch();
	    do
	    {
	    printf(" 1.Translation 2.Rotation 3.Scaling 4.Reflection  5.exit ");
	    printf("Enter your choice:");
	    scanf("%d",&c);
	    switch(c)
	    {
			case 1:	    cleardevice();
				    printf("Enter the translation factor");
				    scanf("%f%f",&xt,&yt);
				    nx1=x1+xt;
				    ny1=y1+yt;
				    nx2=x2+xt;
				    ny2=y2+yt;
				    nx3=x3+xt;
				    ny3=y3+yt;

				    line(nx1,ny1,nx2,ny2);
				    line(nx2,ny2,nx3,ny3);
				    line(nx3,ny3,nx1,ny1);
				    getch();
				    cleardevice();
				    break;

			case 2:      cleardevice();
				    printf(" Enter the angle of rotation");
				    scanf("%f",&r);
				    t=3.14*r/180;
				    nx1=abs(x1*cos(t)-y1*sin(t));
				    ny1=abs(x1*sin(t)+y1*cos(t));
				    nx2=abs(x2*cos(t)-y2*sin(t));
				    ny2=abs(x2*sin(t)+y2*cos(t));
				    nx3=abs(x3*cos(t)-y3*sin(t));
				    ny3=abs(x3*sin(t)+y3*cos(t));
								    line(nx1,ny1,nx2,ny2);
				    line(nx2,ny2,nx3,ny3);
				    line(nx3,ny3,nx1,ny1);
				    getch();
				    cleardevice();
				    break;

			case 3:      cleardevice();
				    printf(" Enter the scaling factor");
				    scanf("%f%f",&sx,&sy);
				    nx1=abs(x1*sx);
				    ny1=abs(y1*sy);
				    nx2=abs(x2*sx);
				    ny2=abs(y2*sy);
				    nx3=abs(x3*sx);
				    ny3=abs(y3*sy);

				    line(nx1,ny1,nx2,ny2);
				    line(nx2,ny2,nx3,ny3);
				    line(nx3,ny3,nx1,ny1);
				    getch();
				    cleardevice();
				    break;

			case 4:      cleardevice();
				    nx1 =abs(x1-140);
				    ny1=abs(y1+140);
				    nx2=abs(x2-140);
				    ny2=abs(y2+140);
				    nx3=abs(x3-140);
				    ny3=abs(y3+140);

				    line(nx1,ny1,nx2,ny2);
				    line(nx2,ny2,nx3,ny3);
				    line(nx3,ny3,nx1,ny1);
				    getch();
				    cleardevice();
				    break;
			case 5:
				    break;
			default:
				    printf("Enter the correct choice");
				    break;
				    }
				    }while(c!=5);
				    closegraph();
				    }