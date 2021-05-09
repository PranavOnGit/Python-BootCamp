

def trasnlate(phrase):
    trasnlation = ''
    for letter in phrase:
        if letter.lower() in "aioue": # checks each letter in string
            if letter.isupper():
                trasnlation = trasnlation + 'X'    
            else:
                trasnlation = trasnlation + 'x'

        else:
            trasnlation = trasnlation + letter
    return trasnlation

print(trasnlate(input('Please enter the word: ')))