

# IF 
is_red = True;

if is_red:
    print("Your Mobile is Red")

# IF ELSE
is_red = False;
if is_red:
    print("Your Mobile is Red")
else:
    print("Your Mobile is not Red")


# IF ELSE with Two conditions 
is_red = True
is_small = False
if is_red or is_small:
    print("Your Mobile is either RED or Small or both")
else:
    print("Your Mobile is not Red OR Small")


# IF ELSE with Two conditions 
is_red = True
is_small = True
if is_red and is_small:
    print("Your Mobile is RED and Small")
else:
    print("Your Mobile is eitther RED or Small or not both")


# IF ELSE IF 
# elif keyword is used for else if
# not() is used to negate

is_man = False
is_alpha = True

if is_man:
    print('the persone is Man')
elif is_alpha:
    print('the persone is Alpha')
elif is_alpha and not(is_man):
    print('the persone is Alpha AND not Man')
elif is_alpha and is_man:
    print('the persone is Alpha AND Man')
elif is_alpha or is_man:
    print('the persone is Alpha OR Man')
else:
    print('not Male not Alpha')

