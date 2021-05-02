import os


def make_original_text_to_lined():
    # Open and read raw_original.txt file
    with open("raw_original_text.txt") as file:
        raw_text = file.read()

    # Split raw_text
    splitted_text = raw_text.split()
    total_word_count = len(splitted_text)

    # Write words line by line to original.txt
    with open("original.txt", "w") as file:
        for word in splitted_text:
            file.write(word + "\n")

    os.system('git add original.txt')
    os.system('git commit -m "initial commit"')

    return total_word_count


def make_user_text_to_lined():
    # take user_input file
    with open("user_input.txt", "r") as file:
        user_text = file.read()

    # splitting user text to write file
    user_text_splitted = user_text.split()

    return user_text_splitted

# Deneme çalışması direk konsoldan bilgi girişi
def make_user_input_text_to_lined():
    
    print("Aşağıda gördüğünüz metni aynen yazınız ...3-2-1 \n")
    import time
    time.sleep(3)

    with open("raw_original_text.txt") as file:
        raw_text = file.read()

    user_text = input(raw_text + '\n')

    # splitting user text to write file
    user_text_splitted = user_text.split()

    return user_text_splitted


def overwrite_to_original_text(user_text_splitted):
    # Write words line by line to original_file
    with open("original.txt", "w") as file:
        for word in user_text_splitted:
            file.write(word + "\n")


def write_diff_result(total_word_count):
    bash_cmd = 'echo ' + str(total_word_count) + ' >> diff_result.txt'

    os.system('git diff original.txt > diff_result.txt')
    os.system(bash_cmd)


def show_result():
    # Open git diff results
    with open("diff_result.txt") as file:
        result_list = file.readlines()

    total_word_count = int(result_list[-1])  # original text word_count result
    missing_words = []  # These words are in the original text but didn't write -
    misspelled_words = []  # These words aren't in the original text but have written +
    mistake_count = 0  # Just missing_words will be added

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

    # os.system('git checkout .')
    os.system('git add .')
    os.system('git commit -m "last commit"')


if __name__ == '__main__':
    total_word_count = make_original_text_to_lined()
    #user_text_splitted = make_user_text_to_lined()
    user_text_splitted = make_user_input_text_to_lined()
    overwrite_to_original_text(user_text_splitted)
    write_diff_result(total_word_count)
    show_result()
