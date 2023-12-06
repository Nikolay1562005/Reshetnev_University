#include <stdio.h>
#include <stdlib.h>
#include <iostream>


void Lab7() {
	int x = 5, y, * px = &x;

	y = *px + 2;
	printf("y = %i Значение указателя = %i\n", y, px);

	y = *px++;
	printf("y = %i Значение указателя = %i\n", y, px);

	px = &x;
	y = (*px)++;
	printf("y = %i Значение указателя = %i. Значение, адресуемое указателем *px = %i\n", y, px, *px);

	y = ++ * px;
	printf("y = %i Значение указателя = %i\n", y, px);
}


int randint(int min, int max);

using namespace std;
void dynamicArray() {
	// 26 - 15 = 11
	unsigned int N;
	cout << "Введите длину списка: "; 
	cin >> N;

	cout << '\n';

	float* array = new float[N];

	cout << "Список рандомных чисел:" << '\n';
	for (int i = 0; i < N; i++) {
		array[i] = (float) randint(1, 500) / randint(5, 80);
		cout << array[i] << " ";
	}
	cout << "\n\n";

	cout << "Список чисел и ссылки к ним:" << '\n';

	float* link = array;

	for (int i = 0; i < N; i++) {
		printf(" Ссылка: %i Значение: %f \n", link, *link);
		link++;
	}

	delete[] array;
}
