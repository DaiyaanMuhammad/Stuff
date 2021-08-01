#include <stdio.h>

int main(int argc, char** argv) {
	int i, j = 1;
	int result = 0;

	printf("\n");
	for (i=0;i<=7;i++) {
		for (j=0;j<=7;j++) {
			result = (8*i)+j;
			printf("\033[4%d;3%dm", i, j);
			printf("%3d", result);
		}
		printf("\n");
	}
			
	printf("\n");
	return 0;
}
