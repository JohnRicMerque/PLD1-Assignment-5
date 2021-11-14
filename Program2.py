# the program will ask for 3 numbers. 
# then displays the lowest number

# ask for input and input validation
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

# function to get the lowest number
def getLowestN(Num1, Num2, Num3):
    if Num1 < Num2 and Num1 < Num3:
        return Num1
    elif Num2 < Num1 and Num2 < Num3:
        return Num2
    else:
        return Num3

# start
num_1, num_2, num_3 = getNum()
lowestNumber = getLowestN(num_1, num_2, num_3)

print(f"The lowest number is {lowestNumber}")
