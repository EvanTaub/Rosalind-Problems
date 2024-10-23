sequences = {}
with open('filename.txt', 'r') as File:
    lines = File.readlines()
    current_key = lines[0][1:len(lines[0]) - 1]
    for line in lines:
        if line.startswith('>'):
            current_key = line[1:len(line)]
            sequences[current_key]  = ""
        else:
            print(line.strip())
            sequences[current_key] += line.strip() #needed to use .strip() to remove newline characters \n because it was messing up calculation
print(sequences)
max_gc_string = ""
max_gc_content = 0
for key in sequences.keys():
    gc_count = 0
    for char in sequences[key]:
        if char in "GC":
            gc_count += 1
    gc_content = (gc_count/len(sequences[key])) * 100
    if gc_content > max_gc_content:
        max_gc_content = gc_content
        max_gc_string = key
print(max_gc_string , max_gc_content)