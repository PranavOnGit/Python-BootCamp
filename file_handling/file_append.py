
# a - Add after last line 

from os import write


file_fruites = open("file_handling/fruites.txt", "a")

#append in the file
file_fruites.write('Grapes - Green/Black')
file_fruites.close()
