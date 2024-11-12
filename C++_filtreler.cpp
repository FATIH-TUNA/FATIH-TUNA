#include<iostream>
#include<opencv2/highgui.hpp>
#include<opencv2/imgcodecs.hpp>
#include<opencv2/imgproc.hpp>

using namespace std;
using namespace cv;
char secim;
int main()
{
	Mat img,bilateralfilter,gaussianblur,medianblur,erodenet,diladenet,kernel,sobel;
	string veri, path;
	cout << "\n1---WEBCAM---" << endl;
	cout << "\n2---FOTO---" << endl;
	cout << "\nBIR ISLEM SECINIZ: " << endl;
	cin >> secim;
	switch (secim)
	{
	case '1': {
		VideoCapture cap(0);
		while (true)
		{
			cap.read(img);
			bilateralFilter(img, bilateralfilter, 15, 90, 90);
			GaussianBlur(img, gaussianblur, Size(15, 15), 1);
			medianBlur(img, medianblur, 15);
			kernel = getStructuringElement(MORPH_RECT, Size(15, 15), Point(-1, -1));
			erode(img, erodenet, kernel, Point(-1, -1), 1);
			dilate(img, diladenet, kernel, Point(-1, -1), 1);
			Sobel(img, sobel, CV_64F, 0, 1, 3, 1, 1);
			imshow("STANDART", img);
			imshow("BILATERALFILTER", bilateralfilter);
			imshow("GAUSSIANBLUR", gaussianblur);
			imshow("MEDIANBLUR", medianblur);
			imshow("EROTION", erodenet);
			imshow("DILATION", diladenet);
			imshow("SOBEL", sobel);
			waitKey(10);
			
		}
		break;
	}
	case '2': {
		cout << "\nBIR VERI GIRINIZ: " << endl;
		cin >> veri;
		path = "C:\\Users\\LENOVO\\Desktop\\fotograflar\\" + veri + ".jpg";
		img = imread(path);
		bilateralFilter(img, bilateralfilter, 15, 90, 90);
		GaussianBlur(img, gaussianblur, Size(15, 15), 1);
		medianBlur(img, medianblur, 15);
		kernel = getStructuringElement(MORPH_RECT, Size(15, 15), Point(-1, -1));
		erode(img, erodenet, kernel, Point(-1, -1), 1);
		dilate(img, diladenet, kernel, Point(-1, -1), 1);
		Sobel(img, sobel, CV_64F, 1, 1, 3, 1, 1);
		imshow("STANDART", img);
		imshow("BILATERALFILTER", bilateralfilter);
		imshow("GAUSSIANBLUR", gaussianblur);
		imshow("MEDIANBUR", medianblur);
		imshow("EROTION", erodenet);
		imshow("DILATION", diladenet);
		imshow("SOBEL", sobel);
		waitKey(0);
		break;
	}
	}
}