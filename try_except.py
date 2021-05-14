
# try-except block is used for catch the error.

try:
    num = int(input('Please enter the number: '))
    print(num)
except:
    print('invalid input')

# We can use mutiple except blocks for on try
# We can catch different errors using exception type as well. 
# we can use 'as' with variable name to store error

try:
    num1 = 123/0
    num = int(input('Please enter the number: '))
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)