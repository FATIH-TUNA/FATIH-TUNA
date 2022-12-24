#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
char cevap;
int main()
{
	FILE *fp;
	struct dene{
		int sicil;
		char ad[100];
		char soyad[100];
		int yas;
		int maas;
	}PERSON;
	fp=fopen("OKU.dat","w");
	if(fp==NULL)
	{
		cout<<"\nDOSYA ACILAMIYOR..."<<endl;
		exit(1);
	}
	do{
		cout<<"\nSICIL: "<<endl;
		cin>>PERSON.sicil;
		cout<<"\nAD: "<<endl;
		cin>>PERSON.ad;
		cout<<"\nSOYAD: "<<endl;
		cin>>PERSON.soyad;
		cout<<"\nYAS: "<<endl;
		cin>>PERSON.yas;
		cout<<"\nMAAS: "<<endl;
		cin>>PERSON.maas;
		fwrite(&PERSON,sizeof(PERSON),1,fp);
		cout<<"\nISLEM DEVAM ETSIN MI: "<<endl;
		cevap=getche();
	}while(cevap=='E' || cevap=='e');
	fclose(fp);
	fp=fopen("OKU.dat","r");
	if(fp==NULL)
	{
		cout<<"\nDOSYA OKUNUYOR..."<<endl;
		exit(1);
	}
	while(!feof(fp)&&fread(&PERSON,sizeof(PERSON),1,fp)==1)
	{
		cout<<"\n"<<endl;
		cout<<PERSON.sicil<<" "<<PERSON.ad<<" "<<PERSON.soyad<<" "<<PERSON.yas<<" "<<PERSON.maas<<endl;
	}
	fclose(fp);
	FILE *fp1;
	fp=fopen("OKU.dat","r");
	if(fp==NULL)
	{
		cout<<"\nDOSYA OKUNAMIYOR..."<<endl;
		exit(1);
	}
	fp1=fopen("DENE.dat","w");
	if(fp1==NULL)
	{
		cout<<"\nDOSYA ACILAMIYOR..."<<endl;
		exit(1);
	}
	while(!feof(fp)&&fread(&PERSON,sizeof(PERSON),1,fp)==1)
	{
		cout<<PERSON.sicil<<" "<<PERSON.ad<<" "<<PERSON.soyad<<" "<<PERSON.yas<<" "<<PERSON.maas<<endl;
		cout<<"\nKAYIT SILINECEK MI: "<<endl;
		cevap=getche();
		if(cevap=='E' || cevap=='e');
		else
		fwrite(&PERSON,sizeof(PERSON),1,fp1);
	}
	fclose(fp);
	fclose(fp1);
	remove("OKU.dat");
	rename("DENE.dat","OKU.dat");
	cout<<"\nYENILENMIS LISTE: "<<endl;
	fp=fopen("OKU.dat","r");
	if(fp==NULL)
	{
		cout<<"\nDOSYA OKUNAMIYOR..."<<endl;
		exit(1);
	}
	while(!feof(fp)&&fread(&PERSON,sizeof(PERSON),1,fp)==1)
	{
		cout<<"\n"<<endl;
		cout<<PERSON.sicil<<" "<<PERSON.ad<<" "<<PERSON.soyad<<" "<<PERSON.yas<<" "<<PERSON.maas<<endl;
	}
	fclose(fp);
	return 0;
}
