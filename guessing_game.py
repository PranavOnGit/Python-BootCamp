

# The for Guessing the word

secrate_variable = 'motivepost'
guess = ''
guess_count = 0
guess_limit = 5
out_of_guesses = False


while guess != secrate_variable and not(out_of_guesses):
    if guess_count < guess_limit:
        print('You have '+str(guess_limit -  guess_count)+' chances left')
        guess = input('Your guess: ')
        guess_count += 1
    else:
        out_of_guesses = True
    

if out_of_guesses:
    print('Out of chances, You Lost')
else:
    print('Hoorey! You Win!')

