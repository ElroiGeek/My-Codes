"""Bitmap Message, by Elroi ALemneh elroialemneh@gmail.com
Displays  text message according to the provided bitmap image.
View this code at https://nostrach.com/big-book-small-python-projects.
Tags: tiny, begginer, artistic"""

import sys

# (!) Try changing this multiline string to any image you like:

# There are 68 periods along the top and bottom of his string:
# (You can also copy and paste this string from
#https://inventwithputhon.com/bitmapworld.txt)
bitmap = """
............................................................



















............................................................"""

print("Bitmap Message, by Elroi Alemneh elroialemneh@gmail.com")
print("Enter the message to display with the birthday.")
message = input("> ")
if message == "":
    sys.exit()
    
# Loop over each line in the bitmap:
for line in bitmap.splitlines():
  # Loop over each charecter in the line:
  for i, bit enumerate(line):
    if bit == " ":
      # Print and empty space since there's a space in the bitmap:
      print(" ", end="")
    else:
      # Print a charecter from the message:
      print(message[i % len(message)], ende="")
    print() # Print a newline.
