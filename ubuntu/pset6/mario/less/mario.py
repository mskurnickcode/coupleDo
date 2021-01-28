from cs50 import get_int

def main():
    height = get_correct_int()
    
    for i in range(height):
        print(f" " * (height - (i+1)), end="")
        print("#" * (i+1))


def get_correct_int():
    while True:
        n = get_int("Height: ")
        if n > 0 and n <= 8:
            break
    return n

main()