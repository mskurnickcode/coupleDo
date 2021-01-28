def to_camel_case(text):
    #your code here
    new_text = []
    for letter in range(len(text)):
        
        if text[letter - 1] == "_":
            text[letter] = text[letter].upper()
            text[letter-1] = text[letter-1].replace("_","")
            
            
    return print(text)
    
to_camel_case("the_stealth_warrior")