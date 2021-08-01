#include <stdio.h>
#include <stdbool.h>

void red(){
	printf("\033[41;37m");
}

void green(){
	printf("\033[42;30m");
}
void reset (){
  printf("\033[0m");
}
int main(int argc, char** argv) 
{
	bool prime=true;
	int num;
	int i;


	printf("Give us a number:\n--> ");
	scanf("%d", &num);

	for (i = 2; i < num; i++){
		if (num % i == 0){
			prime=false;
			break;
		}
		
	}

	if (prime == true){
		green();
		printf("%d", num);
		reset();
		printf(" is a prime number");
	}
	else{
		red();
		printf("%d", num);
		reset();
		printf(" is not a prime number");
	}

	printf("\n");

	return 0;
}
