

#same as object, holds key-value pair

dictionary_of_months = {
    'Jan': 'January', 'Feb': 'February', 'Mar': 'March',
    'Apr': 'April', 'May': 'May', 'Jun': 'June',
    'Jul': 'July', 'Aug': 'August', 'Spe': 'September',
    'Oct': 'October','Nov': 'November','Dec': 'December',

    1 : 'January',
    2 : 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}

print(dictionary_of_months[4])
print(dictionary_of_months['Feb'])

print(dictionary_of_months.get('May')) 

#.get() default NONE if no values found
print(dictionary_of_months.get('Luv')) 

#.get() default NONE if no values found (we can provide default after ,)
print(dictionary_of_months.get('Luv', 'value does not exist!')) 