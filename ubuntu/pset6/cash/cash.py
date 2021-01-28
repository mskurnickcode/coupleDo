from cs50 import get_float

def main():

    CoinCount = 0   
    quarter = 25
    dime = 10
    nickel = 5
    pennie = 1

    change = get_positive_change()
    
    c = round(change*100)

    while c >= quarter:
        c = c - quarter
        CoinCount += 1

    while c >= dime:  
        c = c - dime
        CoinCount += 1

    while c >= nickel:        
        c = c - nickel
        CoinCount += 1

    while c >= pennie:        
        c = c - pennie
        CoinCount += 1        
    
    print(f"{CoinCount}")
    
def get_positive_change():
    while True:
        n = get_float("Change owed: ")
        if n >= 0:
            break
    return n
    
main()
