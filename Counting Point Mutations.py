string1 = input("Enter a String: ")
string2 = input("Enter another String: ")
hamming_distance = 0
# this loop assumes that both strings are of equal length
for i in range(len(string1)):
    if string1[i] != string2[i]:
        hamming_distance +=1

print(hamming_distance)