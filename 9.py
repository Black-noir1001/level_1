def checker_sum_odd_or_even(list):
    sum = 0
    for i in list :
        sum += i
    if sum % 2 == 0 :
        return "even"
    else :
        return "odd"

print(checker_sum_odd_or_even([1,2,3])) # even