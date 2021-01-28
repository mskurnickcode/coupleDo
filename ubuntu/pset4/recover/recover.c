#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    // define byte size
    typedef uint8_t BYTE;
    
    // define global jpeg count
    int jpeg_count = 0;
    //declare filename for continuous use
    FILE *outptr = NULL;
    FILE *inptr = NULL;
    BYTE buffer[512];
    
    // define file name form command line argument
    char *infile = argv[optind];
    
    // if incorrect number of arguments return error
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
    
    //if correct number of arguments move forward
    if (argc == 2)
    {
        // define input file and reject if file name isn't available
        inptr = fopen(infile, "r");
        
        if (inptr == NULL)
        {
            fprintf(stderr, "Could not open %s.\n", infile);
            return 2;
        }
        
        while (fread(buffer, 512, 1, inptr) == 1 && feof(inptr) == 0)
        {
            if (outptr == NULL && buffer[0] != 0xff && buffer[1] != 0xd8 && buffer[2] != 0xff && (buffer [3] & 0xf0) != 0xe0)
            {
                continue;
            }
            // check if a jpeg for first jpeg
            if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer [3] & 0xf0) == 0xe0)
            {
                if (jpeg_count > 0)
                {
                    fclose(outptr);
                    char filename[8];
                    sprintf(filename, "%03d.jpg", jpeg_count);
                    outptr = fopen(filename, "w");
                    fwrite(buffer, sizeof(BYTE), 512, outptr);
                    jpeg_count ++;
                }
                
                // first jpeg found outptr was set to NULL as global
                if (jpeg_count == 0)
                {
                    char filename[8];
                    sprintf(filename, "%03d.jpg", jpeg_count);
                    outptr = fopen(filename, "w");
                    fwrite(buffer, sizeof(BYTE), 512, outptr);
                    jpeg_count ++;
                }
            }
            
            else if (jpeg_count > 0)
            {
                fwrite(buffer, sizeof(BYTE), 512, outptr);
            }
        }
    }
    
    if (outptr != NULL)
    {
        fclose(outptr);
    }
    fclose(inptr);
    
    return 0;
}
