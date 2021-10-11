#include<stdio.h>
#include<conio.h>
#include<graphics.h>
void main()
{
int ch,x[10],y[10],z[10],a,b,c,j,xr[10],yr[10],zr[10];
int gd=DETECT,gm;
printf("\n\n parallel projection");
printf("\n\n to enter coordinates\n\n") ;
printf("\n else any other value would lead to default value \t:");
scanf("%d",&ch);
if(ch==1)
{
printf("\n follow these steps");
for(int i=0;i<8;i++)
scanf("%d",&x[i],&y[i],&z[i]);
}
else
{
x[0]=y[0]=z[0]=0;
x[1]=80;y[1]=z[1]=0;
x[2]=y[2]=80;z[2]=0;
x[3]=0;y[3]=80;z[3]=0;
x[4]=0;y[4]=z[4]=80;
x[5]=y[5]=0;z[5]=80;
x[6]=80;y[6]=0;z[6]=80;
x[7]=y[7]=z[7]=80;
printf("\n default values have been set");
}
printf("\n\n now enter the projection vector \t");
scanf("%d%d%d",&a,&b,&c);
for(int i=0;i<8;i++)
{
xr[i]=x[i]-(a*z[i]/c);
yr[i]=y[i]-(b*z[i]/c);
zr[i]=0;
}
initgraph(&gd,&gm,"");
setcolor(CYAN);
line(300,0,300,480);
line(0,240,600,240);
setcolor(YELLOW);
for(i=0,j=i+1;i<8;i++,j=(j+1)/8);
line(xr[i]+300,240-yr[i],xr[j]+300,240-yr[i]);
getch();
closegraph();
}