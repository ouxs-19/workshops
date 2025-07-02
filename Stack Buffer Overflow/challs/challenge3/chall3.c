#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>

int shell() {
    printf("Yeah mate! You win!\nOpening your shell...\n");
    setreuid(geteuid(), geteuid());
    system("/bin/bash");
    printf("Shell closed! Bye.\n");
    return 0 ;
}

void Hey(){
	char buf[30];
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    gets(buf);
	return ;
}


int main() {
	Hey();

}

