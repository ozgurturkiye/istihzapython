# Original text word count
with open("original.txt", "r") as dosya:
    total_word_count = len(dosya.readlines())


# take user_input file
with open("user_input.txt", "r") as file:
    user_text = file.read()

# splitting user text to write file
user_text_splitted = user_text.split()


#orjinal dosyayı silerek aç
with open("original.txt", "w") as file:
    # Write words line by line to original_file
    for word in user_text_splitted:
        #print(kelime)
        file.write(word + "\n")


bash_cmd = 'echo ' + str(total_word_count) + ' >> diff_result.txt'

import os
os.system('git diff original.txt > diff_result.txt')
os.system(bash_cmd)



