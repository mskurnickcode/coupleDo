#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    // check if correct number of command line inputs
    if (argc != 2)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    else 
    {
        // check if cypher is 26 characters
        if (strlen(argv[1]) != 26)
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
        else
        {
            // check that all characters are letters
            for (int i = 1, n = strlen(argv[1]); i <= n; i++)
            {
                if (isdigit(argv[1][i]))
                {
                    printf("Key must contain 26 letters.\n");
                    return 1;
                }
            }
            
        }
    }
    
    //check for no duplicate letters
    int matches = 0;
    for (char x = 'a'; x <= 'z'; x++)
    {
        for (int z = 0; z <= 26; z++)
        {
            if (tolower(argv[1][z]) == x)
            {
                matches++;
                break;
            }
        }
    }
        
    if (matches != 26)
    {
        printf("Key must contain 26 Unique letters.\n");
        return 1;
    }
    
    // get plaintext string
    string plaintext = get_string("plaintext: ");
    
    // print ciphertext
    printf("ciphertext: ");
    
    for (int c = 0, r = strlen(plaintext); c < r; c++)
    {
        int upper_cipher_char = (plaintext[c] - 65);
        int lower_cipher_char = (plaintext[c] - 97);
        
        //uppercase switch
        if ((plaintext[c] >= 65) && (plaintext[c] <= 90))
        {
            if (isupper(argv[1][upper_cipher_char]))
            {
                printf("%c", (argv[1][upper_cipher_char])); 
            }
            else
            {
                printf("%c", toupper((argv[1][upper_cipher_char])));
            }
        }
        
        // lowercase switch
        else if ((plaintext[c] >= 97) && (plaintext[c] <= 122))
        {
            if (islower(argv[1][lower_cipher_char]))
            {
                printf("%c", (argv[1][lower_cipher_char]));
            }
            else
            {
                printf("%c", tolower(argv[1][lower_cipher_char]));
            }
        }
        
        // non alphabetical
        else 
        {
            printf("%c", plaintext[c]);
        }
    }
    printf("\n");
    return 0;
}