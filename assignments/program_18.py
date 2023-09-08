# This is program 18
# Write a program to print table of a number which lies between 1 and 10

# Get user input for the number
number = int(input("Enter a number between 1 and 10: "))

# Check if the input is within the valid range
if 1 <= number <= 10:
    for i in range(1, 11):
        ans = number * i
        print(f"{number} x {i} = {ans}")
else:
    print("Invalid input. Please enter a number between 1 and 10.")
