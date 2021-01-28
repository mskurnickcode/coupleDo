#include <stdio.h>
#include <cs50.h>



int main()
{

long number;
    // get card number
    do
    {
    number = get_long("Number: ");
    }
    while (number < 0);
    
    printf("%li\n", number);
    
    
    // determine card length
    
    long temp_number = number;
    int cardLength = 0;
    
    while (temp_number > 0)
    {
        temp_number = temp_number / 10;
        cardLength ++;
    }

// card length check
    printf("Card Length: %i \n", cardLength);   
    
    // check if card length is invalid
    if (cardLength != 15 && cardLength != 16 && cardLength != 13)
    {
        printf("INVALID\n");
    }
    else 
    {
    // turn card numbers into individual digits array
        int i;
        int lastDigit[cardLength];
    
        for (i = 0; i < cardLength; i++)
        {
            lastDigit[i] =  number % 10;
            number = number / 10;
        }
    
    // get *2 of every other digit and sum
        int k;
        int productDigitSum = 0;
        for (k = 1; k <= cardLength; k += 2)
        {
            if ((lastDigit[k] * 2) >= 10)
            {
                productDigitSum += ((lastDigit[k] * 2) % 10);
                productDigitSum += 1;
            }
            else 
            {
                productDigitSum += ((lastDigit[k] * 2) % 10);
            }
        }
        printf("ProductDigitsum: %i\n", productDigitSum);
        
        // get sum of non-summed digits above
        int l;
        int nonSummedNumbers = 0;
        for (l = 0; l <= cardLength; l+=2)
        {
            nonSummedNumbers += lastDigit[l];
        }
        
        // non summed digits check
        printf("Non Summed Digits: %i\n", nonSummedNumbers);
        
        int Total_Sums = productDigitSum + nonSummedNumbers;
        printf("Total of both loops: %i\n", Total_Sums);
          
        //check card type
        if ((Total_Sums % 10) == 0 && cardLength == 15)
        {
            if (lastDigit[14] == 3 && (lastDigit[13] == 4 || lastDigit[13] == 7))
            {
                printf("AMEX\n"); 
            }
            else
            {
                printf("INVALID\n");
            }
                
        } 
        else if ((Total_Sums % 10) == 0 && cardLength == 13)
        {
           printf("VISA\n"); 
        }
        else if ((Total_Sums % 10) == 0 && cardLength == 16)
        {
            if (lastDigit[15] == 5 && (lastDigit[14] == 1 || lastDigit[14] ==  2 || lastDigit[14] ==  3 || lastDigit[14] ==  4 || lastDigit[14] ==  5))
            {
                printf("MASTERCARD\n");
            }
            else if (lastDigit[15] == 4)
            {
                printf("VISA\n");
            }
            else 
            {
            printf("INVALID\n");
            }
        }
        else 
        {
            printf("INVALID\n");
        }
        
    }
    
}
