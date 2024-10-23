dna_strings = []
with open('filename2.txt','r') as File:
    lines = File.readlines()
    for line in lines:
        if line.startswith('>'):
            continue
        else:
            list = []
            for char in line.strip():
                list.append(char)
            dna_strings.append(list)

profile = {"A" : [], "C" : [], "G" : [], "T" : []}
for key in profile.keys(): # loops 4 times because need to make 4 x n grid
    for j in range(len(dna_strings[0])): #loops n times (dependent on length of strands)
        profile[key].append(0)

# profile = {"A": [0,0,0,0,0.....0] length n for all keys,
#            "C": [0,"           "],
#            "G": [0,"           "],
#            "T": [0,"           "]}


for i in range(len(dna_strings)): #loops m times
    for j in range(len(dna_strings[0])): #loops n times, the length of the first array of nucleotides
        profile[dna_strings[i][j]][j] += 1 #counts each time every key appears within a specific sequence



consensus = ""
for i in range(len(dna_strings[0])): # loops n times. Is the first loop because string must be of length n
    max_char = ""
    max_count = 0
    for key in profile.keys(): #loops 4 times
        if profile[key][i] > max_count: #checks which value within a specific index is the greatest and then stores it and its count to compare to the next key's value
            max_char = key # key is the codon that is most frequent
            max_count = profile[key][i]
    consensus+= max_char #adds the most frequent codon character within a specific index to the consensus string
print(consensus)


# prints out the profile
for key in profile.keys():
    string = ""
    for digit in profile[key]:
       string += str(digit) + " "
    print(key + ": " + string)


    


