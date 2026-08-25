#include<iostream>
#include<fstream>
#include "usslum.h"
#include<string>
using namespace std;
int main()
{
	int x,y,z,a,b,toplam,adet,i;
	int dizi[]={153,90,890,9,407,213,324,457,879};
	adet=sizeof(dizi)/sizeof(dizi[0]);
	for(i=0;i<adet;i++)
	{
		a=dizi[i];
		b=dizi[i];
		toplam=0;
		z=0;
		while(a>0)
		{
			a=a/10;
			z++;
		}
		while(b>0)
		{
			x=b%10;
			b=b/10;
			toplam+=usal(x,z);
		}
		if(toplam==dizi[i])
		{
			cout<<dizi[i]<<" SAYISI BIR ARMSTRONG SAYISIDIR..."<<endl;
		}
		else{
			cout<<dizi[i]<<" SAYISI BIR ARMSTORNG SAYISI DEGILDIR..."<<endl;
		}
	}
	
	
}
