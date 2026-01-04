# This program ask the name of the user and saves it to a text file

def get_name(greet="Hello User"):
    print(greet)

    name = input("What is your name? \n> ").strip()

    if not name:
        print("You did not enter a name. Please try again.")
        return get_name(greet)

    with open("name.txt", "a") as name_file:
        name_file.write(name + "\n")
        
    print(f"Your name '{name}' has been saved to 'name.txt' file.")


get_name()