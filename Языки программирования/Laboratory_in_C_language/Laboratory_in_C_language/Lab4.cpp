#include <stdio.h>


void list_characters() {
    puts("Выводит список символов ASCII:");

    for (int i = 0; i < 255; i++) {
        printf("%i = %c \n", i, i);
    };
};


void funk() {
    double n1, n2, result = 1;
    puts("Программа считает произведение чисел не кратных 5 от n1 до n2");
    printf("n1 = "); scanf_s("%lf", &n1);
    printf("n2 = "); scanf_s("%lf", &n2);
    if (n2 < n1) {
        puts("Ошибка n2 не может быть меньше n1");
        funk();
    }
    for (int i = n1; i <= n2; i++) {
        if (i % 5 != 0) {
            result = (double) result * i;
        }
    }
    if (result != 1) {
        printf("Результат: %lf", result);
    }
}
