string = input("Enter a string: ")
newString = ""
for char in string:
    if char != "T":
        newString += char
    else:
        newString += "U"
print(newString)