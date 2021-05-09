

# comparison operators are <=, >=, ==, !=

def max_find(num1, num2, num3):
    if num1 >= num3 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_find(103, 9, 6))
     

def min_find(num1, num2, num3):
    if num1 <= num3 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3

print(min_find(3, 2, 6))


def find_animal(animal):
    if 'dog' == animal or 'Dog' == animal:
        print('yes, its Dog')
    elif 'cat' == animal or 'Cat' == animal:
        print('yes, its Cat')
    elif 'cat' != animal or 'Cat' != animal or 'dog' != animal or 'Dog' != animal:
        print('Nope, not Cat, not Dog!')

find_animal('dog')