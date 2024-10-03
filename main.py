def myfunction():
    b = input("ENTER A BINARY NUMBER: ")
    00
    if not all(char in '01' for char in b):
        print("INVALID BINARY NUMBER")
        return
    
    decimal_number = int(b, 2)
    print("The decimal number is", decimal_number)

myfunction()