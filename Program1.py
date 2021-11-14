# the program will ask for grade percentage 
# then displays the equivalent Grade/Mark and Description

# input validation
while True:
        try:
            gradeP = float(input("Enter Grade Percentage: "))
        except ValueError:
            print("Invalid input. Please enter a Grade Percentage (e.g. 98)")
            continue
        else:
            break

# conditions
if gradeP >= 97 and gradeP <= 100:
    print("Grade/Mark: 1.0\nDescription: Excellent")
elif gradeP >= 94 and gradeP <= 96:
    print("Grade/Mark: 1.25\nDescription: Excellent")
elif gradeP >= 91 and gradeP <= 93:
    print("Grade/Mark: 1.5\nDescription: Very Good")
elif gradeP >= 88 and gradeP <= 90:
    print("Grade/Mark: 1.75\nDescription: Very Good")
elif gradeP >= 85 and gradeP <= 87:
    print("Grade/Mark: 2.00\nDescription: Good")
elif gradeP >= 82 and gradeP <= 84:
    print("Grade/Mark: 2.25\nDescription: Good")
elif gradeP >= 79 and gradeP <= 81:
    print("Grade/Mark: 2.5\nDescription: Satisfactory")
elif gradeP >= 76 and gradeP <= 78:
    print("Grade/Mark: 2.75\nDescription: Satisfactory")
elif gradeP == 75:
    print("Grade/Mark: 3.00\nDescription: Passing")         
elif gradeP >= 65 and gradeP <= 74:
    print("Grade/Mark: 5.00\nDescription: Failure")   
else:
    print("Grade/Mark: Inc./W/D\nDescription: Incomplete/Withdrawn/Dropped")
     