#ifndef karart_h
#define karart_h
#include<iostream>
using namespace std;
int ekle(int dizi_1[],int a1,int dizi_2[],int a2)
{
	int i,j,a,b,c,d,e,g;
	d=a2+1;
	for(i=0;i<a1;i++)
	{
		a=0;
		b=0;
		for(j=0;j<i;j++)
		{
			if(dizi_1[i]==dizi_2[j])
			{
				a++;
				break;
			}
		}
		if(a!=0)
		{
			continue;
		}
		for(c=0;c<a2;c++)
		{
			if(dizi_1[i]==dizi_2[c])
			{
				b++;
			}
		}
		if(b>0&&b<d)
		{
			d=b;
		}
	}
	for(i=0;i<a1;i++)
	{
		a=0;
		b=0;
		for(j=0;j<i;j++)
		{
			if(dizi_1[i]==dizi_1[j])
			{
				a++;
				break;
			}
		}
		if(a!=0)
		{
			continue;
		}
		for(c=0;c<a2;c++)
		{
			if(dizi_1[i]==dizi_2[c])
			{
				b++;
			}
		}
		if(b==d)
		{
			cout<<dizi_1[i]<<" SAYISI DIZI_2 ICINDE "<<b<<" DEFA TEKRAR EDIYOR..."<<endl;
		}
	}
	return 0;
}
#endif
