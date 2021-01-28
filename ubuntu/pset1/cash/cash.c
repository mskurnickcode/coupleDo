#include <stdio.h>
#include <cs50.h>
#include <math.h>

float change;
int coins;
int cents;
int quarters;
int dimes;
int nickels;
int pennies;

int main(void)
{
    // get change
    do
    {
      change = get_float("Change owed: "); 
    }
    while (change < 0);
    
    //Change received check
    printf("Change: %f\n", change);
    
    //turn into cents
    cents = round(change * 100);
    
    // Check cents work
    printf("Cents: %i \n", cents);
    
    // count number of quarters and subtract from cents
    while (cents >= 25)
    {
        cents = cents - 25;
        quarters += 1;
    }
    
    // count number of dimes
    while (cents >= 10)
    {
        cents = cents - 10;
        dimes += 1; 
    }
    
    while (cents >= 5)
    {
        cents = cents - 5;
        nickels += 1;
    }
        
    while (cents > 0)
    {
        cents = cents - 1;
        pennies += 1;
    }
        
    coins = quarters + dimes + nickels + pennies;
        
        
    printf("%i\n", coins);
}

