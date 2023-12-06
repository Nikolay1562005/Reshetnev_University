#include <stdio.h>
#include <stdlib.h>


void Lab6() {
	int age;
	char name[100], str[100];

	puts("Введите Ваше имя : "); gets_s(name, 100);
	printf("Введите Ваш возраст : \n");
	scanf_s("%i", &age);
	sprintf_s(str, "Здраствуйте %s. Ваш возраст %i лет", name, age);
	puts(str);
}


void findTheeWords() {
	char line[100], lineVowel[20] = "уеыаоэяиюёeyuioa";
	puts("Программа удаляет все гласные из строки");
	puts("Введите строку:");
	gets_s(line, 100);
	for (int i = 0; i < 100; i++) {
		bool flag = 1;
		for (int j = 0; j < 20; j++) {
			if (line[i] == lineVowel[j]) {
				flag = 0;
			}
		}
		if (flag == 1) {
			printf("%c", line[i]);
		}
	}
}