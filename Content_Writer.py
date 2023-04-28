# Ezrhael R. Sicat
# BSCpE 1-5
# 04/27/2023
# Program 3: Write a text into a file

# open a mylife text file
with open("mylife.txt", "w") as my_file:
# create a loop for y/n
# ask the user to enter a line
    user_text = input("Enter line: ")
    my_file.write("Enter line: " + user_text + "\n")
# ask the user y/n for more lines
    user_line = input("Are there more lines? (y/n) ")
    my_file.write("Are there more lines? (y/n) " + user_line + "\n")
# write the user text and user line in mylife file
# if no break the loop