# This is program 15
# dictionaries are mutable
a = input("Enter the word: ")
dict1 = {"good": "something pleasant", "fetch": "to bring", "1": "the number 1"}
print(dict1[a])
b = (input("Enter the name: "))
marks = {"Harshit": "92", "Ranit": "F", "Harry": "98", "Puja": "92", "Diksha": "95"}
print(marks[b])
# "good","Harry" ==> these are keys and "something pleasant","98" are the corresponding values to the keys
# dictionaries are mutable ==> This makes dictionaries Special
marks["Priyanka"] = 34
print(marks)
# This way you can add more and more keys and their corresponding values
print(marks.get("Priyanka Chopra"))  # This will print ==> none as the corresponding value to Priyanka Chopra is none
# .get method will not show the error message if the keys are not present
