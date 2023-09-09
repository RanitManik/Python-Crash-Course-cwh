# This is program 24
# This will generate an absence leave letter to the HOD getting input of student name and date
# by default the program will fill other credentials and reasons

# user's personal details go here ==>
date = input("Enter the date: ")
Your_Name = input("Enter your name: ")
Department = input("Enter your Department: ")
Roll_no = input("Enter your roll no: ")
City = input("Enter your city: ")
State = input("Enter your state: ")
ZIP = input("Enter your zip code: ")

# recipient's personal details go here ==>
Recipient_Name = input("Enter Recipient's name: ")
Recipient_City = input("Enter Recipient's city: ")
Recipient_State = input("Enter Recipient's state: ")
Recipient_ZIP = input("Enter Recipient's zip code: ")


# letter ==>
def print_letter():
    letter = f"""
    Date: {date}

    {Recipient_Name}
    {Recipient_City}, {Recipient_State}, {Recipient_ZIP}

    Dear {Recipient_Name},

    I hope this message finds you well. I am writing to request a leave of absence for personal reasons. Due to unforeseen circumstances, I find it necessary to take some time off from work to address these matters.
    
    I understand the importance of my responsibilities at [Department/Company Name], and I will make every effort to ensure a smooth transition during my absence. I am willing to delegate my tasks and responsibilities to a colleague or provide any necessary training to ensure that the team's productivity is not affected during my absence.
    
    I intend to be away from work for [mention the duration of your leave], starting from [start date] to [end date]. I assure you that I will stay reachable and will be available in case of any urgent matters that may require my attention.
    
    I am committed to returning to work promptly and will do my best to ensure that all pending work is completed or appropriately handed over before my departure.
    
    I would be grateful if you could consider and approve my request for leave of absence. I will be happy to provide any additional information or documentation if required.
    
    Thank you for your understanding and support. I look forward to your positive response.

    Sincerely,

    {Your_Name}
    
    {Your_Name}
    {Department}, {Roll_no}
    {City}, {State}, {ZIP}
    """

    print(letter)


# Call the function to print the letter
print_letter()
