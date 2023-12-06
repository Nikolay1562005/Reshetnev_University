#include <stdio.h>
#include <stdlib.h>
#include <iostream>



int* deleteEvenValues(int oldArray[], int countElements) {\

	int countNotEvenValues = 0;
	for (int i = 0; i < countElements; i++) {
		if (oldArray[i] % 2 == 1) {
			countNotEvenValues += 1;
		}
	}

	int* newArray = new int[countNotEvenValues];
	newArray[0] = countNotEvenValues;
	int count = 1;
	for (int i = 0; i < countElements; i++) {
		if (oldArray[i] % 2 == 1) {
			newArray[count] = oldArray[i];
			count++;
		}
	}
	return newArray;
}

int randint(int min, int max);

using namespace std;
void workingWithFunction() {
	// 26 - 15 = 11
	unsigned int N;
	cout << "Введите длину списка: ";
	cin >> N;

	cout << '\n';

	int* array = new int[N];

	cout << "Список рандомных чисел:" << '\n';
	for (int i = 0; i < N; i++) {
		array[i] = randint(1, 500) / randint(5, 80);
		cout << array[i] << " ";
	}
	cout << "\n\n";
	int* newArray = deleteEvenValues(array, N);
	for (int i = 1; i < newArray[0] + 1; i++) {
		cout << newArray[i] << " ";
	}
}