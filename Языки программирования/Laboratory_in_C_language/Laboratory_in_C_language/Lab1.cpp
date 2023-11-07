#include <stdio.h>
#include <stdlib.h>
#include <math.h>



void Lab1() {

	float x, numerator, denominator, y, z;

	printf("Функция считает: y, z");
	printf("\nВведите x");
	printf("\nx = "); scanf_s("%f", &x);

	numerator = (float)pow(x, 2) + 2 * x - 3 + (x + 1) + sqrtf(pow(x, 2) - 9);
	denominator = (float)pow(x, 2) + 2 * x - 3 + (x - 1) + sqrtf(pow(x, 2) - 9);
	y = (float)numerator / denominator;
	printf("\ny = %f", y);

	z = (float)sqrt((x + 3) / (x - 3));
	printf("\nz = %f\n", z);
};

//---------------------------------------------

void S() {


	float a, b, c, p, S;

	puts("Программа считает S треугольника по формуле герона");
	printf("\na = "); scanf_s("%f", &a);
	printf("\nb = "); scanf_s("%f", &b);
	printf("\nc = "); scanf_s("%f", &c);

	p = (float)(a + b + c) / 2;
	S = (float)sqrt(p * (p - a) * (p - b) * (p - c));

	printf("\nПлощадь треугольника = %f\n", S);
}