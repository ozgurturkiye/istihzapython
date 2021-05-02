# Open and read raw_original.txt file
with open("raw_original.txt") as file:
    raw_text = file.read()


# Split raw_text
splitted_text = raw_text.split()


# Open empty original.txt file
with open("original.txt", "w") as file:
    # Write words line by line to original_file
    for word in splitted_text:
        #print(kelime)
        file.write(word + "\n")
    

with open("original.txt") as file:
    a = file.readlines()
    print("word len ", len(a))

