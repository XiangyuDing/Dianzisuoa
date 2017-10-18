#include <stdio.h>

int main() {
	printf("%s\n", "hello world from inside controller 2");

	int status = system("java keypad");

	 status = system("python lock.py");

	return status;
}

