# Open git diff results
with open("diff_result.txt") as file:
    result_list = file.readlines()

total_word_count = int(result_list[-1]) # original text word_count result
missing_words = [] # These words are in the original text but didn't write -
misspelled_words = [] # These words aren't in the original text but have written +
mistake_count = 0 # Just missing_words will be added


for line in result_list:
    if line[0] == "-" and (line[1] != "-"):
        mistake_count += 1
        missing_words.append(line[1:-1])

    if line[0] == "+" and (line[1] != "+"):
        # These words didn't count as mistake
        misspelled_words.append(line[1:-1])


correct_word_count = total_word_count - mistake_count

print("Total word counts: ", total_word_count)
print("Mistake Count: ", mistake_count)
print("Correct Count: ", correct_word_count)
print("Missing Words: ", missing_words)
print("Misspelled Words: ", misspelled_words)

import os
os.system('git checkout .')
