# Ezrhael R. Sicat
# BSCpE 1-5
# 04/27/2023
# Program 3: Write a text into a file

import pyfiglet
import colorama

print (colorama.Fore.GREEN + "=" * 100)
font = pyfiglet.figlet_format("Writing a text into a file", font = "big", justify = "center")
print (colorama.Fore.YELLOW + font)

# Introduction to the Program 
print (colorama.Fore.GREEN + "=" * 100)
user_name = input(colorama.Fore.BLUE + "Enter your username: ")
print (colorama.Fore.GREEN + "=" * 100)
print (colorama.Fore.WHITE + "Hello!", colorama.Fore.YELLOW + user_name)
print (colorama.Fore.WHITE + "Today, We are going to Write a text into a file")

# open a mylife text file
with open("mylife.txt", "w") as my_file:
    # create a loop for y/n
    while True:
        print (colorama.Fore.GREEN + "=" * 100)
        # ask the user to enter a line
        user_text = input(colorama.Fore.BLUE + "Enter line: ")
        # ask the user y/n for more lines
        user_line = input("Are there more lines? (y/n) ")
        # write the user text and user line in mylife file
        my_file.write("Enter line: " + user_text + "\n")
        my_file.write("Are there more lines? (y/n) " + user_line + "\n")
        # if no break the loop
        if user_line.lower() == "n":
            break

print (colorama.Fore.GREEN + "=" * 100)
print (colorama.Fore.YELLOW + "Thank you for using this program.")
print (colorama.Fore.GREEN + "=" * 100)