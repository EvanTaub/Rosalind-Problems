string1 = input("Enter first String: ")
string2 = input("Enter second String: ")
locations = []
for i in range(len(string1)):
    if string2 == string1[i: i + len(string2)]: #checks each slice of the string based on the given string
        locations.append(i+1) #Solution set uses an index count that starts from index[1] not index[0] like in python






for index in locations:
    print(index, end = " ")