from cs50 import get_string

def main():
    text = get_string("Text: ")
    
    text_length = len(text)
    
    space_count = 0
    sentences = 0
    letter_count = 0
    
    for i in range(text_length):
        if str.isalpha(text[i]) == True:
            letter_count += 1
        if str.isspace(text[i]) == True:
            space_count += 1
        if (text[i] == '.') or (text[i]=='!') or (text[i]=='?'):
            sentences += 1
    
    grade = 0.0588 * (100 * letter_count / (space_count + 1)) - 0.296 * (100 * sentences / (space_count + 1)) - 15.8
    
    if (grade < 1):
        print("Before Grade 1")
    elif (grade > 16):
        print("Grade 16+")
    else:
        print(f"Grade {round(grade)}")

main()