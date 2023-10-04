# This is program 28
s = "Ranit is a great guy"
with open("test.txt", "w") as f:
    f.write(s)
# here you don't need to close the file as the context manager take care of that part
# s, f ==> variable
