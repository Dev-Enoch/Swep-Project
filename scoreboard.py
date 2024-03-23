print(f"\n\t\tScore Board to check if a Student pass/fails")
input_name= input(f"\nEnter your name: ")
print("Hi,",input_name.upper())
score = input("Enter your score: ")
if score >= "50":
    print(f"\n{input_name.upper()}, Weldone!, You scored, {score}%.")
else:
    print(f"\nYou Failed, You scored {score}%.")