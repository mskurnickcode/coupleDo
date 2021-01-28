#include <stdio.h>
#include <cs50.h>

int get_integer(string prompt);

int main(void)
{
    // get name
    int height = get_integer("Height: ");
    // return given name
}


int get_integer(string prompt)
{
    int n;
    do
    {
        n = get_int("%s", prompt);
    }
    while (n < 1 || n > 8);
    
    
    for (int i = 0; i < n; i++)
    {
        for (int j = n - 1; j > i ; j--)
        {
            printf(" ");
        }
        
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        
        printf("  ");
        
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
    printf("\n");
    }
    return n;
}