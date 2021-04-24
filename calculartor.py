

num1 = input(" Please Enter a Number: ")
num2 = input(" Please Enter another Number: ")

#resultx = num1 + num2 this statement will throw an error as Python By default takes as STRING 
#resultx = int(num1) + int(num2) You can only do operations with whole number ; 2 + 4 = 6  || 2.4 + 4.2 will encoter an error

result = float(num1) + float(num2)
print(result)
