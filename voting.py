# Modified code with basic error handling
try:
    age = int(input("Enter your age: "))
    # Check for voting eligibility
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print(f"You are not eligible to vote. Wait {18 - age} more year(s).")
except ValueError:
    print("Please enter a valid numerical age.")
