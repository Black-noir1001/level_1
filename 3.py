def sum_of_postive_numbers(list):
    sum = 0
    for i in list :
        if i > 0:
            sum += i 
    return sum 

print(sum_of_postive_numbers([1,2,-6,4,-9])) # 7