# Create a program that ask for an age of a person
# Display the life stage of the person.

#input validation
while True:
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Invalid input. Please enter your age in numbers.")
        continue
    else:
        break

if age > -1 and age <= 12:
    print("Kid")
elif age >= 13 and age <= 17:
    print("Teen")
elif age == 18:
    print("Debut")
else:
    print("Adult")

print("Done")