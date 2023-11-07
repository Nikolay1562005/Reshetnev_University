#include <stdio.h>
#include <stdlib.h>
#include <math.h>


#include "const.h"
void find_len() {
	float n, running_time, wick_leight;

	printf("Выводит длину фитиля по желаймому пути отдаления:");
	printf("\nn = "); scanf_s("%f", &n);

	if (n >= 0) {
		running_time = n / running_speed;
		wick_leight = fire_speed * running_time;

		printf("\nдлина фитиля = %.2f ??\n", wick_leight);
	}
	else {
		printf("Ищет длину фитиля\n");
		find_len();
	};
}

//-------------------------------------------------

#define TWO 2
#define FOUR TWO*TWO //2; * 2;
#define PX printf("x = %i.\n", x);
#define FMT "x = %i.\n"
#define SQUARE(X) (X)*(X)

int Bad_function() {
	int x = TWO;
	PX;
	x = FOUR;
	printf(FMT, x);
	x = SQUARE(3 * 3 - 3);
	PX;
	return 0;
}