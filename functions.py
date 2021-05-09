
# def is used to define functions.
# code after : will be considerd as function block. 
# indentation is important.
# _ is used if there are two words in name and needs to be in small case.

#simple
def hello_there():
    print('hello!')

hello_there()     

#parameterised
def hello_there(name):
    print("Hello, "+name)

hello_there('Pranav')


def addition(a, b):
    print("Addition is: "+ str(a + b))

addition(1, 3)

