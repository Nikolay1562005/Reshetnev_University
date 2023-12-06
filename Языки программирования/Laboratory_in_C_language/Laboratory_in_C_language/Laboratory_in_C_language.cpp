#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <locale>
#include <iostream>


//Лабораторная 1
void Lab1();
void S();

//Лабораторная 2
void find_len();
void Bad_function();

//Лабораторная 3
void Lab3_calculator();
void Lab3_main_task();

//Лабораторная 4
void list_characters();
void funk();

//Лабораторная 5
int randint(int min, int max);
void sortedList();
void Lab5();

//Лабораторная 6
void Lab6();
void findTheeWords();

//Лабораторная 7
void Lab7();
void dynamicArray();

//Лабораторная 8
void Lab8();
void actionsForDynamicArray();

//Лабораторная 9
void workingWithFunction();

//Лабораторная последняя
void ex1();
void ex2();
void ex3();
void ex4();
void ex5();
void ex6();
void ex7();

int main(int argc, char* argv[], char* env[]) {
    setlocale(0, "");
    srand((unsigned)time(0));
    //Лабораторная 1
    //Lab1();
    //S();

    //Лабораторная 2
    //find_len();
    //Bad_function();

    //Лабораторная 3
    //Lab3_calculator();
    //Lab3_main_task();

    //Лабораторная 4
    //list_characters();
    //funk();

    //Лабораторная 5
    //printf("%i", randint(5, 20));
    //sortedList();
    //Lab5();

    //Лабораторная 6
    //Lab6();
    //findTheeWords();

    //Лабораторная 7
    //Lab7();
    //dynamicArray();

    //Лабораторная 8
    //Lab8();
    //actionsForDynamicArray();

    //Лабораторная 9
    //Lab9();
    workingWithFunction();
    //--------------------------------
    //printf("Количество аргументов командной строки %i \n", argc);

    //puts("\n\n");
    //printf("Аргументы командной строки: \n"); 
    //for (int i = 0; i < argc; i++) {
    //    printf("%s\n", argv[i]);
    //}
    //puts("\n\n");

    //printf("\nАргументы состояния среды: \n");
    //for (int i = 0; env[i] != NULL; i++) {
    //    printf("%s\n", env[i]);
    //}
    //----------------------------

    //float value1, value2;
    //char op;
    //if (argc >= 4) {
    //    value1 = atoi(argv[1]);
    //    op = argv[2][0];
    //    value2 = atoi(argv[3]);
    //    if (op == '+') {
    //        printf("%.2f\n", value1 + value2);
    //    }
    //    else  if (op == '-') {
    //        printf("%.2f\n", value1 - value2);
    //    }
    //    else  if (op == '/') {
    //        if (value2 == 0) {
    //            puts("You can't divide by zero!!!");
    //        }
    //        else {
    //            printf("%.2f\n", value1 / value2);
    //        }
    //    }
    //    else  if (op == '*') {
    //        printf("%.2f\n", value1 * value2);
    //    }
    //    else {
    //        puts("Unknown sign!!!");
    //    }
    //}

    //Лабораторная последняя
    //ex1();
    //ex2();
    //ex3();
    //ex4();
    //ex5();
    //ex6();
    //ex7();

    return 1;
}