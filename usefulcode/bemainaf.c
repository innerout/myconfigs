#include <stdio.h>
__attribute__((constructor)) static void _bar() { printf("bar\n"); }
int main(){
	printf("HELLO\n");
	printf("HELLO\n");

}
__attribute__((destructor)) static void _bar2() { printf("bar\n"); }
