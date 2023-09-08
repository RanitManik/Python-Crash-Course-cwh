# This is program 21
# This program will keep taking input until you enter '0'
while True:
    num = int(input("Enter the number: "))
    print("You have entered: ", num)
    if num == 0:
        print("You are out of loop...")
        break
