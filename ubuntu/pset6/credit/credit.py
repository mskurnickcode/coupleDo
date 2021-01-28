from cs50 import get_int
import sys

def main():
    
    card = get_card()
    
    # check that we have card number
    #print(f"Card Number: {card}")
    
    # turn card number into a string for length and digit manipulation
    card_string = str(card)
    card_length = len(card_string)
    
    if (card_length != 15) and (card_length != 16) and (card_length != 13):
        print("INVALID")
        sys.exit(1)
       
    # declare product sum
    productSum = 0    
    
    #Find the sum of digits of every second number starting from 1 from the last
    for x in range((card_length - 2), -1, -2):
        product = int(card_string[x]) * 2
        if product >= 10:
            #print(f"{product}")
            last_digit= product % 10
            productSum += (1 + last_digit)
            
        else:
            #print(f"{product}")
            productSum += product
    
    #print(f"Second Number Digits {productSum}")
    
    #find the sum of non-previously summed digits
    for y in range((card_length - 1), -1, -2):
        product = int(card_string[y])
        productSum += product
        
    #print(f"Card passed productSum test with {productSum} which modulo 10s to: {productSum % 10}")
    
    if (productSum % 10) != 0:
        print("INVALID")
        sys.exit(0)
    
    else:
        if (int(card_string[0]) == 3 and int((card_string[1]) == 4 or int(card_string[1]) == 7)):
            print("AMEX")
        
        elif (int(card_string[0]) == 4):
            print("VISA")
            
        elif (int(card_string[0]) == 5 and (int(card_string[1]) == 1 or int(card_string[1]) == 2 or int(card_string[1]) == 3 or int(card_string[1]) == 4 or int(card_string[1]) == 5)):
            print("MASTERCARD")
            
        else:
            print("INVALID")
    
    
    
    
def get_card():
    while True:
        n = get_int("Number: ")
        if n > 0:
            break
    return n
    
    
main()