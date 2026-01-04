"""
This program reads a text file, 
calculates the number of lines, words and 
characters and save all results into one report file
"""
# Chatgpt

# def analyze_text_file(txt_file):
#     try:
#         with open(txt_file, "r") as file:
#             lines = file.readlines()
#             content = "".join(lines)

#         line_count = len(lines)
#         word_count = len(content.split())
#         character_count = len(content.strip())

#         with open("report_file.txt", "w") as report_file:
#             report_file.write(f"Report for: {txt_file}\n")
#             report_file.write("-" * 30 + "\n")
#             report_file.write(f"Lines: {line_count}\n")
#             report_file.write(f"Words: {word_count}\n")
#             report_file.write(f"Characters: {character_count}\n")

#         print("Report generated successfully")

#     except FileNotFoundError:
#         print(f"Error: '{txt_file}' not found")
#     except Exception as e:
#         print(f"Unexpected error: {e}")


# analyze_text_file("cmda.txt")

def analyze_text_file(txt_file):
    try:
        with open(txt_file, "r") as file:
            lines = file.readlines()
            content = "".join(lines)

        line_count = len(lines)
        word_count = len(content.split())
        character_count = len(content.strip())

        with open("report_file.txt", "w") as report_file:
            report_file.write(f"Report anaysis for: '{txt_file}'\n")
            report_file.write("*" * 30 + "\n")
            report_file.write(f"Lines: {line_count} \n")
            report_file.write(f"Words: {word_count} \n")
            report_file.write(f"Characters: {character_count} \n")

        print("Report generated successful")

    except FileNotFoundError:
        print(f"Error: '{txt_file}' not found")
    except Exception as e:
        print(f"Unexpected error: {e}")


analyze_text_file("read_txt.py")
