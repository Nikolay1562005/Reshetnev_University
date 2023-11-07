#include <stdio.h>
#include <stdlib.h>
#include <math.h>



void Lab3_calculator() {
    float value1, value2;
    char op;

    puts("Enter without spaces: number sign number\n for example: 45*89\n");
    scanf_s("%f%c%f", &value1, &op, &value2);

    if (op == '+') {
        printf_s("%.2f\n", value1 + value2);
    }
    else  if (op == '-') {
        printf_s("%.2f\n", value1 - value2);
    }
    else  if (op == '/') {
        if (value2 == 0) {
            puts("You can't divide by zero!!!");
        } else {
            printf_s("%.2f\n", value1 / value2);
        }
    }  
    else  if (op == '*') {
        printf_s("%.2f\n", value1 * value2);
    }
    else {
        puts("Unknown sign!!!");
    }
};

//--------------------------------------

void Lab3_main_task() {
    const int rows = 2;
    const int columns = 3;
    float boxs[rows][columns];

    
    puts("Эта программа считает поместится ли коробка в посылку");

    puts("Введите размер посылки:");
    printf("l = "); scanf_s("%f", &boxs[0][0]);
	printf("b = "); scanf_s("%f", &boxs[0][1]);
	printf("h = "); scanf_s("%f", &boxs[0][2]);

    puts("Введите размер коробки:");
    printf("l = ");scanf_s("%f", &boxs[1][0]);
    printf("b = ");scanf_s("%f", &boxs[1][1]);
    printf("h = ");scanf_s("%f", &boxs[1][2]);

    for (int number_box = 0; number_box < rows; number_box++) {
        for (int i = 0; i < columns; i++) {
            for (int j = 0; j < columns - 1; j++) {
                if (boxs[number_box][j] < boxs[number_box][j + 1]) {
                    float storage = boxs[number_box][j];
                    boxs[number_box][j] = boxs[number_box][j + 1];
                    boxs[number_box][j + 1] = storage;
                }
            }
        }
    }
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            printf("%f ", boxs[i][j]);
        };
        puts("\n");
    }
    if (boxs[1][0] <= boxs[0][0] && boxs[1][1] <= boxs[0][1] && boxs[1][2] <= boxs[0][2]) {
        puts("Поместится!!!");
    } else {
        puts("Непоместится!!!");
    }
}