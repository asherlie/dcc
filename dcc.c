#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>

#if !1
there will be a thread waiting for commands
commands will simply be book/author names

@search commands will be sent with these exact strings
the most relevant result will be recorded

the relevant command will be sent

another thread will wait for dcc messages

we can store a hashing structure with book names - hashing the exact search term
might be the best option
this hashing structure will be `fwrite`n to the disk after each insertion
#endif

int main(int a, char** b){
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    connect(); to the server specified
    then /join
    inet_addr
    gethostbyname
}
