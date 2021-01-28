#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int k;

// take arguments in commandline
int main(int argc, string argv[])
{
    //check that correct number of arguments exist
    if (argc == 2)
    {
        //check that arg1 (key) is digits by returning if there is a letter
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            if (isalpha(argv[1][i]))
            {
                printf("Usage: ./caesar key \n");
                 return 1;
            }
        }
        
            
    //check for non-negative integer
    // turn argv1 into integer with atoi and then check if its positive
        k = atoi(argv[1]);
        if (k < 0)
        {
            printf("Usage: ./caesar key \n");
            return 1;
        }
                
        // if successful print success and then get plaintext string
        else
        {
            string plaintext = get_string("Plaintext: ");
                    
            printf("ciphertext: ");
            int c;
            for (c = 0; c < strlen(plaintext); c++)
            {
                // uppercase letters switched
                if ((plaintext[c] >= 65) && (plaintext[c] <= 90))
                {
                    printf("%c", (((plaintext[c] + k) - 65) % 26) + 65);  
                }
                        
                // lowercase letter switched
                else if ((plaintext[c] >= 97) && (plaintext[c] <= 122))
                {
                    printf("%c", (((plaintext[c] + k) - 97) % 26) + 97);  
                }
                        
                // keep non-alphabetics the same
                else 
                {
                    printf("%c", plaintext[c]);
                }
            }
            printf("\n");
            return 0;
        }
    }
    else
    {
        return 1;
    }
}


