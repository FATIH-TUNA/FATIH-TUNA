#include<iostream>
#include "en_az_tekrar.h"
using namespace std;
int main()
{
	int a1,a2;
	int dizi_1[]={12,21,23,32,34,43,45,54,56,65,67,76};
	int dizi_2[]={90,12,12,23,32,32,32,32,21,21,65};
	a1=sizeof(dizi_1)/sizeof(dizi_1[0]);
	a2=sizeof(dizi_2)/sizeof(dizi_2[0]);
	ekle(dizi_1,a1,dizi_2,a2);
}
