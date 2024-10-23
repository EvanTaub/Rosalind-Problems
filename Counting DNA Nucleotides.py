nucleotides = {"A": 0 , "C":  0, "G" : 0, "T" : 0}
# with open('filename.txt','r') as File:
#     string = File.readlines()
string = input("Enter a string: ")
for key in nucleotides.keys():
    for char in string:
        if key == char:
            nucleotides[key] +=1
for key in nucleotides.keys():
    print(nucleotides[key], end = " ")
