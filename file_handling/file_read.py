

# It's best proctices when we open any file, don't forget to close the same file
# r - read
# w - write
# a - append
# r+ _ read and write 

file_fruites = open("file_handling/fruites.txt", "r")

# check of the file is readable
print(file_fruites.readable())

# reads 1st line
print(file_fruites.readline()) 
# reads 2nd line
print(file_fruites.readline()) 

#read all lines and put them in the list [ -, -, - ]
print(file_fruites.readlines())

#reads first from the list
print(file_fruites.readlines()[1])

#loop through all lines
for fruites in file_fruites.readlines():
    print(fruites)

#closing the file
file_fruites.close()

