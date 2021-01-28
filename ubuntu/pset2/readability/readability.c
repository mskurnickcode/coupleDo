#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <string.h>

int i;
int n;
int letter_count;
int sentence_count;
int word_count = 1;
float grade;

int main(void)
{
    string s = get_string("Text: ");
    
    for (i = 0, n = strlen(s); i < n; i++)
    {
        if ((s[i] >= 'A' && s[i] <= 'Z') || (s[i] >= 'a' && s[i] <= 'z'))
        { 
            letter_count += 1;   
        }
    }
    
    for (i = 0, n = strlen(s); i < n; i++)
    {
        if (s[i] == '?' || s[i] == '.' || s[i] == '!')
        {
            sentence_count += 1;
        }
    }
    
    for (i = 0, n = strlen(s); i < n; i++)
    {
        if (s[i] == ' ')
        {
            word_count += 1;
        }
    }
    
    grade = 0.0588 * (100 * (float) letter_count / (float) word_count) - 0.296 * (100 * (float) sentence_count / (float) word_count) - 15.8;
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int) round(grade));
    }
}
