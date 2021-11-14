# the program will ask for 3 numbers. 
# then displays the lowest number

# input validation
def getNum():
    while True:
        try:
            Num1 = int(input("Enter 1st number: "))
            Num2 = int(input("Enter 2nd number: "))
            Num3 = int(input("Enter 3rd number: "))
        except ValueError:
            print("Invalid Input. Please enter a number.")
            continue
        else:
            break
    return Num1, Num2, Num3

num_1, num_2, num_3 = getNum()
