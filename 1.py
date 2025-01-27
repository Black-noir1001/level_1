def power_numbers(num , powr):
    result = 1
    for index in range(powr) :
       result *=   num 
    return result

print(power_numbers(5,2)) # result  = 25