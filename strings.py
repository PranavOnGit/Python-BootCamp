

message = "Pranav\nis"
print(message+" cool guy!")

message = "Pranav Chavan"
print(message.lower()) #make lower case

message = "Aadita Chavan"
print(message.upper().isupper()) #True

print(len(message)) #character length 

print(message[0]) #get character at in string
print(message.index("d")) #get index of char in string

print(message.index("hav")) #get index of char in string // Will throw an error if doesnt exist.

print(message.replace("Aadita", "Pranav")) #replace the string
