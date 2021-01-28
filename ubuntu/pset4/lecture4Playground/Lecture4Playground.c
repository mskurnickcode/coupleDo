#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    int entries = get_int("How many entries: ");
    
    FILE *file = fopen("phonebook.csv", "a");
    
    for (int i = 0; i < entries; i++)
    {
        char *name = get_string("Name: ");
        char *number = get_string("Number: ");
    
        fprintf(file, "Name: %s, Number: %s\n", name, number);    
    }
    
    fclose(file);
}



if (jpeg_count > 0 && buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer [3] & 0xf0) == 0xe0)
            {
                // close previous file
                fclose(outptr);
                outptr = NULL;
                 
                 //increment count with new jpeg
                jpeg_count ++;
                char filename[8];
                sprintf(filename, "%03d.jpg", jpeg_count);
                outptr = fopen(filename, "w");
                
                if (outptr == NULL)
                    {
                        printf("Output file %s not found\n", filename);
                        return 3;
                    }
                    
                    //if outptr exists, write buffer into file
                    fwrite(buffer, sizeof(BYTE), 512, outptr);
                    
                
                
            }