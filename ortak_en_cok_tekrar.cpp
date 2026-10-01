#include<iostream>
using namespace std;
class ekleme;
class deneme{
	private:
		int dizi1[14]={12,21,23,32,34,43,45,54,56,65,32,32,12,12};
		int a1=sizeof(dizi1)/sizeof(dizi1[0]);
		public:
			int hesapla(ekleme&);
};
class ekleme{
	private:
		int dizi2[23]={90,80,99,88,12,12,23,67,76,77,66,120,130,321,345,32,32,32,12,12,12,12,12};
		int a2=sizeof(dizi2)/sizeof(dizi2[0]);
		public:
			friend class deneme;
};
int deneme::hesapla(ekleme&tuna)
{
	int i,j,a,b,c,d=0,e;
	for(i=0;i<a1;i++)
	{
		a=0;
		b=0;
		for(j=0;j<i;j++)
		{
			if(dizi1[i]==dizi1[j])
			{
				a++;
				break;
			}
		}
		for(c=0;c<tuna.a2;c++)
		{
			if(dizi1[i]==tuna.dizi2[c])
			{
				b++;
			}
		}
		if(b>d)
		{
			d=b;
			e=dizi1[i];
		}
	}
	cout<<e<<" SAYISI DIZI2 ICINDE "<<d<<" DEFA GECIYOR..."<<endl;
}

int main()
{
	deneme dene;
	ekleme ekle;
	dene.hesapla(ekle);
}
