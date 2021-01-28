#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // get name
    string answer = get_string("What's your name?\n");
    // return given name
    printf("hello, %s\n", answer);
}

