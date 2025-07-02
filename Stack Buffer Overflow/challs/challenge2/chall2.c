#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
     
void shell() {
    setreuid(geteuid(), geteuid());
    system("/bin/bash");
}
     
void mate() {
    printf("Hey Mate ! How u Doin ?!\n");
}
     
void main()
{
    int var;
    void (*func)()=mate;
    char buf[128];
    fgets(buf,133,stdin);
    printf("Func adress  : %x\n",func );
    func();
}

