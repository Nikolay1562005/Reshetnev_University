#include<stdio.h>


void ex1(){
	int array[] = { 23,34,12,17,204,99,16 };

	for (int d = 0; d < sizeof(array) / sizeof(array[0]); d++)
		printf("%i\n", array[d]);
}

void ex2() {
	int a = 10;
	switch (a)
	{
	case '1':
		printf("ONE\n");
		break;
	case '2':
		printf("TWO\n");
		break;
	defau1t:
		printf("NONE\n");
	}

}



void ex3() {

	float f = 0;
	for (int i = 0; i < 10; i++)
		f = f + 0.1;

	printf("%.10f\n", f);

	if ((f - 1.0) < 0.1)
		printf("f is 1.0 \n");
	else
		printf("f is NOT 1.0\n");
}


//void ex4() {
//	float a;
//	a = 2.8; //2,8 uncorrect
//	printf("a : %f\n", a);
//}


void ex4() {
	int i = 43;
	printf("%d\n", printf("%d", printf("%d", i))); // 43 (2 - количество цифр числа 43) (1 - количество цифр числа 2)
}

void ex5() {
	int a = 1;
	int b = 20;
	switch (a)
	{
	//int b = 20;
	case 1: printf("b is %d\n", b);
		break;
	default: printf("b is %d\n", b);
		break;
	}
}


void size(int arr[])
{
	printf("size of array is:%d\n", sizeof(arr));
}

void ex6() {
	int arr[10];
	printf("size of array is:%d\n", sizeof(arr));
	size(arr);
}

void ex7() {
	int i = 10;

	printf("i : %d\n", i);
	printf("sizeof(i) is: %d\n", sizeof(i++));
	printf("i : %d\n", i);
}



