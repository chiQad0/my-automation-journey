# This program reads from a txt file

def read_txt(txt_file):
    with open(txt_file, "r") as file:
        
        for lines in file:
            print(lines.strip())
        
# read_txt("cmda.txt")

# This program reads from a txt file, count number of words in the txt file and write the result in another file.

def count_words_txt(txt_file):
    with open(txt_file, "r") as file:
        content= file.read()
        word_count = len(content.split())
    with open("len_words.txt", "w") as write_result:
        write_result.write(f"The number of words in \"{txt_file}\" is {word_count}")
                   

# count_words_txt("cmda.txt")

# This program reads from a txt file, count number of lines in a txt file and write the result in another file.

def count_lines_txt(txt_file):
    with open(txt_file, "r") as file:
        line_count = sum(1 for _ in file) 
        
    with open("len_lines.txt", "w") as write_result:
        write_result.write(f"The number of lines in \"{txt_file}\" is {line_count}")

count_lines_txt("cmda.txt")