
#print(2 ** 3) = 8 this is how exponent works

def get_power(base_var, power):
    result = 1
    for index in range(power):
        result = result * base_var
    return result

print(get_power(2, 23))