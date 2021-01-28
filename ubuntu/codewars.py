names = ["matt", "steven"]

def main():
    likes(names)

def likes(names):
    #your code here
    length = len(names)
    if (length == 0):
        results= print("no one likes this")
    if (length == 1):
        results = print(f"{names[0]} likes this")
    if (length == 2):
        results = print(f"{names[0]} and {names[1]} like this")
    if (length == 3):
        results = print(f"{names[0]}, {names[1]} and {names[2]} like this")
    elif (length > 3):
        results = print(f"{names[0]}, {names[1]} and {(len(names) - 2)} others like this")
        
        
main()