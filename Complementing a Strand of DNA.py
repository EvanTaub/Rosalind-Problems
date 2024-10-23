complements = {"A" : "T" , "T": "A" , "C" : "G", "G" : "C"}
string = input("Enter a String: ")
complement_string = ""
for char in string:
    complement_string += complements[char]
complement_string = complement_string[::-1]
print(complement_string)