
#if write the file and file not present at the location, new file will be created.

file_text = open("file_handling/file_text.txt", "w")

# to check if file is writable
print(file_text.writable())
file_text.write('Hello, this text has been written using file write code')

# we can write filw with any extention
file_text = open("file_handling/fileTest.html", "w")

print(file_text.writable())
file_text.write('<h1> Hello, there! </h1>')


file_text.close()