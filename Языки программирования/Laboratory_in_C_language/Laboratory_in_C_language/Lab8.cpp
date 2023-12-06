#include <stdio.h>
#include <stdlib.h>
#include <iostream>


int randint(int min, int max);

void Lab8() {
	int rows = 2;
	int const cols = 5;

	int** rooms;

	// создание указателей
	rooms = new int *[rows];
	for (int i = 0; i < rows; i++) {
		rooms[i] = new int[cols + i];
	}

	// инициализация указателей
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			rooms[i][j] = randint(1, 100);
		}
	}

	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			printf("%i ", rooms[i][j]);
		}
		puts("");
	}

	// уничтожение
	for (int i = 0; i < rows; i++) {
		delete[] rooms[i];
	}

	delete[] rooms;
}


int randint(int min, int max);

using namespace std;
void actionsForDynamicArray() {
	// Вариант 16
	unsigned int k;
	cout << "Введите длину списка: ";
	cin >> k;

	cout << '\n';
	//int* X = (int*)malloc(50*sizeof(int));
	//free(X);
	int* X = new int[k];
	int sumAllValues = 0;

	int numberMaxValue = 0;
	int maxValue = X[0];

	for (int i = 0; i < k; i++) {
		X[i] = randint(1, 500) / randint(5, 80);
		sumAllValues += X[i];
		if (X[i] > maxValue) {
			maxValue = X[i];
			numberMaxValue = i;
		}
	}
	cout << "\n\n";


	cout << "среднее арифметическое элементов всего массива: "
		<< endl
		<< (float)sumAllValues / k
		<< endl;

	cout << "Список рандомных чисел:" << endl;
	for (int i = 0; i < k; i++) {
		cout << X[i] << " ";
	}
	cout << endl;



	int* newX = new int[numberMaxValue + 1];
	
	int sumValues = 0;

	for (int i = 0; i < numberMaxValue + 1; i++) {
		newX[i] = X[i];

		sumValues += newX[i];

		if (i <= numberMaxValue) {
			sumValues += X[i];
		}
	}


	cout << "среднее арифметическое элементов массива до максимального элемента(включительно): "
		<< endl
		<< (float)sumValues / (numberMaxValue + 1)
		<< endl;


	for (int i = 0; i < numberMaxValue + 1; i++) {
		cout << newX[i] << " ";
	}
	delete[] newX;
	delete[] X;
}