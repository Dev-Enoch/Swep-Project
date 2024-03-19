print(f"\n\t\tSwep Project")
# Correctly using input() to accept user input
print(f"Type 'yes' to continue or 'no' to stop")
user_input = input("Do you want to continue: ")
if user_input == "yes":
        print(f"\n\nDistinguishing Even & Odd Numbers")
        input1= input((f"Enter a number: "))
        number = int(input1)
        if number % 2 != 0:
            print(f"The Number, {number} is an Odd Number")
        else:
            print(f"The Number, {number} is an Even Number")
elif user_input == "no":
        pass
else:
    print("Invalid choice.")

# Printing the user input


    