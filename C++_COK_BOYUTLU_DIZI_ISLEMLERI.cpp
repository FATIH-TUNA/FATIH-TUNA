#include<iostream>
#include<conio.h>
using namespace std;
char cevap;
int main()
{
	int x,y,i,j,z,a,b;
	cout<<"\nBIR X DEGERI GIRINIZ: "<<endl;
	cin>>x;
	cout<<"\nBIR Y DEGERI GIRINIZ: "<<endl;
	cin>>y;
	int dizi[x][y];
	for(i=1;i<=x;i++)
	{
		for(j=1;j<=y;j++)
		{
			cout<<"\nSAYI = "<<endl;
			cin>>dizi[i][j];
		}
		cout<<"\n";
	}
	for(i=1;i<=x;i++)
	{
		for(j=1;j<=y;j++)
		{
			cout<<dizi[i][j]<<"\t";
		}
		cout<<"\n";
	}
	cout<<"\n";
	for(i=1;i<=x;i++)
	{
	    z=0;
		for(j=1;j<=y;j++)
		{
			z=z+dizi[i][j];
		}
		cout<<i<<". NCI SATIRIN ELEMANLARI TOPLAMI = "<<z<<endl;
	}
	cout<<"\n"<<endl;
	for(j=1;j<=y;j++)
	{
		z=0;
		for(i=1;i<=x;i++)
		{
			z=z+dizi[i][j];
		}
		cout<<j<<". NCI SUTUNUN ELEMANLARI TOPLAMI = "<<z<<endl;
	}
	do{
	cout<<"\nSATIR NUMARASI GIRINIZ: "<<endl;
	cin>>a;
	cout<<"\nSSUTUN NUMARASI GIRINIZ: "<<endl;
	cin>>b;
	cout<<"\nBULUNAN DEGER = "<<dizi[a][b]<<endl;
	cout<<"\n"<<endl;
	cout<<"\nISLEM DEVAM ETSIN MI: "<<endl;
	cevap=getche();
}while(cevap=='E' || cevap=='e');
	
}
